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
    ifstream cin("/Users/sarahwooders/Desktop/text.txt");
    
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; i ++)
    {
        
        vector<double> n;
        vector<double> k;
        int num;
        cin >> num;
        for(int i = 0; i < num; i ++)
        {
            double x;
            cin >> x;
            n.push_back(x);
        }
        int war = num;
        int fakewar = 0;
        for(int i = 0; i < num; i ++)
        {
            double x;
            cin >> x;
            k.push_back(x);
        }
        sort(n.begin(), n.end());
        sort(k.begin(), k.end());
        
        for(int a = 0; a < num; a ++)
        {
            double maxbeat = -1;
            int maxindex = -1;
            for(int b = 0; b < num; b ++)
            {
                if(k[a] > n[b] && n[a] > maxbeat && !seen[b])
                {
                    maxbeat = n[b];
                    maxindex = b;
                }
            }
            if(maxindex > -1)
            {
                seen[maxindex] = true;
                war --;
            }
        }
        reset();
        
        for(int a = 0; a < num; a ++)
        {
            double maxbeat = -1;
            int maxindex = -1;
            for(int b = 0; b < num; b ++)
            {
                if(k[b] < n[a] && k[b] > maxbeat && !seen[b])
                {
                    maxbeat = k[b];
                    maxindex = b;
                }
            }
            if(maxindex > -1)
            {
                seen[maxindex] = true;
                fakewar ++;
            }
        }
        reset();
        cout << "Case #" << i + 1 << ": " << fakewar << " " << war << endl;
        
    }
}

