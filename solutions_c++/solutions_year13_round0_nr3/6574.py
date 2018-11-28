#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <iostream>
#include <sstream>
#include <bitset>
using namespace std;

bool isPalindrome (long val) {
    string str;
    while (val) {
        str += val % 10 + '0';
        val /= 10;
    }
    
    string rev = str;
    reverse(rev.begin(), rev.end());
    
    int comp = str.compare(rev);
    return comp == 0 ? true : false;
}

int main()
{
	
	
	FILE *fp1 = fopen ("C-small-attempt0.in", "r");
	FILE *fp2 = fopen ("output31.txt", "w");
	//FILE *fp1 = fopen ("A-large.in", "r");
	//FILE *fp2 = fopen ("output2.txt", "w");
	
	int T, A, B;
	fscanf (fp1, "%d\n", &T);
    long long result;
    set<int> mySet;
    
	for (int i = 0; i < T; ++i) {
        fscanf (fp1, "%d %d\n", &A, &B);
        result = 0;
        mySet.clear();
        
        if (1 >= A && 1 <= B)
            result++;
        
        for (int j = 2; j <= B; ++j) {
            if (mySet.find(j) != mySet.end())
                continue;
            
            if (!isPalindrome(j))
                continue;
            mySet.insert(j);
            
            long long square = j * j;
            while (square <= B) {
                mySet.insert(square);
                //printf ("%lld\n", square);
                
                if (isPalindrome(square)) {
                    if (square >= A && square <= B)
                        result++;
                    square *= square;
                }
                else
                    break;
            }
            
            
        }
        
        //print out
        fprintf (fp2, "Case #%d: %lld\n", i + 1, result);
        
        
    }
    
    return 0;
}


