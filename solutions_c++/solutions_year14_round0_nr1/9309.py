/*
 
 Hossam Ghareeb (hossam.ghareb@gmail.com)
 
 */

#include <cstring>
#include <string.h>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <set>
#include <vector>
#include <complex>
#include <list>
#include <map>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <deque>
#include <queue>

using namespace std;


#define all(v) v.begin(),v.end()
#define forloop(i,m) for(int i=0;i<(int)(m);i++)
#define forloop2(i,n,m) for(int i=n;i<(int)(m);i++)
#define printCase(i) printf("Case #%d: ", i)
#define printEndLine cout << endl


typedef vector<string> vs;
typedef  stringstream ss;
typedef vector<int> vi;
typedef istringstream iss;


#define SMALL

#define SMALL_FILE_IN "A-small-attempt0.in"
#define SMALL_FILE_OUT "A-small-attempt0.out"
#define LARGE_FILE_IN "A-large-practice.in"
#define LARGE_FILE_OUT "A-large-practice.out"

int main(int argc, const char * argv[])
{
    
    
#ifdef SMALL
	freopen(SMALL_FILE_IN, "rt", stdin);
	freopen(SMALL_FILE_OUT, "wt", stdout);
#endif
#ifdef LARGE
	freopen(LARGE_FILE_IN, "rt", stdin);
	freopen(LARGE_FILE_OUT, "wt", stdout);
#endif
    
    int row1[4];
    int row2[4];
    
    
    int N;
    
    int answer1;
    int answer2;
    
    cin >> N;
    string line;
    getline(cin, line);
    forloop2(i, 1, N + 1)
    {
        cin >> answer1;
        getline(cin, line);
        
        forloop2(x, 1, 5)
        {
            getline(cin, line);
            if (x == answer1) {
                iss stream(line);
                stream >> row1[0] >> row1[1] >> row1[2] >> row1[3];
            }
        }
        
        cin >> answer2;
        getline(cin, line);
        
        forloop2(x, 1, 5)
        {
            getline(cin, line);
            if (x == answer2) {
                iss stream(line);
                stream >> row2[0] >> row2[1] >> row2[2] >> row2[3];
            }
        }
        
        int similarity = 0;
        int solution = 0;
        forloop(a, 4)
        {
            forloop(b, 4)
            {
                if (row1[a] == row2[b]) {
                    similarity++;
                    solution = row1[a];
                }
            }
        }
        
        
        printCase(i);
        if (similarity == 0) {
            cout << "Volunteer cheated!" << endl;
        }
        else
        {
            if (similarity == 1) {
                cout << solution << endl;
            }
            else
            {
                cout << "Bad magician!" << endl;
            }
        }
        
        
    }
    return 0;
}