#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <iterator>
#include <map>
#include <cstring>
#include <climits>
#include <time.h>

using namespace std;

#define READ() 	freopen("in.txt","r",stdin)
#define WRITE() freopen("out.txt","w",stdout)
#define sf(n) 	scanf("%d",&n)
#define lsf(n) 	scanf("%lld", &n)
#define pb(n) 	push_back(n)
#define EPS 	1e-10
#define NL 		printf("\n")
#define INF INT_MAX
#define MAX INT_MAX
#define MOD 1000000007
#define LL long long

string s;
int len;

int main()
{
    READ();
    WRITE();

    int t;
    cin >> t;

    int TC = 0;

    while(t--)
    {
        cin >> s;
        len = s.size();

        cout << "Case #" << ++TC << ": ";

        int chkMin = 0;
        for(int i=0;i<len && s[i] == '-';i++)chkMin++;

        if(chkMin == len)
        {
            cout << 1 << endl;
        }
        else
        {
            bool fm = false;
            bool fp = false;

            LL cnt = 0;

            for(int i=0;i<len;i++)
            {
                if(s[i] == '-')
                {
                    fm = true;
                    if(fp && (i+1>=len || s[i+1] == '+'))
                    {
                        cnt += 2;
                        fm = false;
                    }
                }
                else if(s[i] == '+')
                {
                    fp = true;
                    if(fm && (i+1>=len || s[i+1] == '-'))
                    {
                        cnt += 1;
    //                    fp = false;
                    }
                }
            }

            cout << cnt << endl;
        }


    }


    return 0;
}

