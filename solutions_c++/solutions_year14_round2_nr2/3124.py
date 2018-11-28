/*
 ID: sarahwo1
 PROG: humble
 LANG: C++
 */
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <cctype>
#include <streambuf>
#include <string>
#include <sstream>
#include <cmath>
#include <stack>
//#include <queue>
#include <ctime>
#include <time.h>
#include <iomanip>
#include <set>

using namespace std;
#define INF (2147483630);
bool seen[2000];

void reset()
{
    for(int i = 0; i < 2000; i ++) seen[i] = false;
}

int main()
{
    ofstream cout("/Users/sarahwooders/Desktop/money.txt");
    ifstream cin("/Users/sarahwooders/Desktop/castle.txt");
    
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; i ++)
    {
        int A;
        int B;
        int K;
        cin >> A;
        cin >> B;
        cin >> K;
        
        int c = 0;
        for(int a = 0; a < A; a ++)
        {
            for(int b = 0; b < B; b ++)
            {
                int x = a & b;
                if(x < K) c ++;
            }
        }
        cout << "Case #" << i + 1 << ": " << c << endl;
    }
}

