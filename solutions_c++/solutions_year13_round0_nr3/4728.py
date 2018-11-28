#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>


//#define DEBUG

using namespace std;

bool palindrome(long long n){
    ostringstream ss;
    ss << n;
    string a = ss.str();
    int l = a.length(); 
    for(int i = 0; i <= l/2; i++){
        if(a[i] == a[l-i-1])
            continue;
        else
            return false;
    }
    return true;
}

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main(){
	#ifndef DEBUG
		freopen("C-large-1.in", "r", stdin);
		freopen("C-large-1.out", "w", stdout);
	#endif
    vector<long long> fairsquares;
    for(long long i = 1; i*i <= 100000000000000L; i++){
        if(palindrome(i) && palindrome(i*i)){
            fairsquares.push_back(i*i);
        } 
    }
    long long T;
    cin >> T;
    for (int test = 0; test < T; test++) {
        long long A, B;
        cin >> A >> B;
        int count = 0;
        for(int i = 0; i < fairsquares.size(); i++){
            if(fairsquares[i] >= A && fairsquares[i] <= B)
                count++;
        }
        cout << "Case #" << test+1 << ": ";//Output Answer:
        cout << count << endl;
    }

	return 0;
}
