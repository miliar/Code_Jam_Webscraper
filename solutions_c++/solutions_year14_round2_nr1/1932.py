#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define pb push_back
#define clean(a,b) memset(a,b,sizeof(a))
#define oo 1<<20
#define dd double
#define ll int
#define ull unsigned long long
#define ff float
#define EPS 10E-10
#define fr first
#define sc second
#define MAXX 100000
#define PRIME_N 1000000
#define INFI 1<<30
#define SZ(a) ((int)a.size())
#define all(a) a.begin(),a.end()
#define MODD 1000000007

//int rx[] = {0,-1,0,1,1,-1,-1,0,1}; //four direction x
//int ry[] = {0,1,1,1,0,0,-1,-1,-1};   //four direction y
//int rep[] = {1,1,4,4,2,1,1,4,4,2}; //repet cycle for mod
//void ullpr(){printf("range unsigned long long : %llu\n",-1U);} //for ull
//void ulpr(){printf("range unsigned long : %lu\n",-1U);} //for ull
//void upr(){printf("range unsigned : %u\n",-1U);} //for ull

vector<string>v;
int st[110];

int main()
{
    freopen("inp.txt" , "r+" , stdin);
    freopen("out.txt" , "w+" , stdout);
    int tcase,cas=1;
    int n;

    scanf(" %d",&tcase);

    while(tcase--)
    {
        scanf(" %d" ,&n);
        clean(st,0);
        v.clear();
        string str;
        int sol = 0;
        int nosol = 0;
        for(int i = 0 ; i<n ; i++)
        {
            cin>>str;
            v.pb(str);
        }

        for(int i = 0 ; i<SZ(v[0]) && !nosol ; i++)
        {
            int cntmx = -1 , cntmin = -1;

            for(int j = 1 ; j<SZ(v) && !nosol ; j++)
            {
                int k;
                int cnt = 0;
                for(k = st[j] ; k<SZ(v[j]) ; k++)
                {
                    if(v[j][k]!=v[0][i])
                    {
                        break;
                    }
                    else cnt++;
                }
                st[j] = k;
                if(cnt ==0) nosol =1;
                if(cntmin==-1 || cntmin>cnt) cntmin = cnt;
                if(cntmx==-1 || cntmx<cnt) cntmx = cnt;
            }
            int j = i;
            int cnt = 0;
            while(v[0][j]==v[0][i] && j<SZ(v[0]))
            {
                j++;
                cnt++;
            }
            i = j-1;
            if(cntmin==-1 || cntmin>cnt) cntmin = cnt;
            if(cntmx==-1 || cntmx<cnt) cntmx = cnt;

            sol += (cntmx-cntmin);
        }

        if(nosol==0)
        {
            for(int i =1  ; i<SZ(v) && !nosol ; i++)
            {
                if(st[i]==SZ(v[i]))continue;
                else nosol = 1;
            }
        }

        printf("Case #%d: ",cas++);
        if(!nosol) printf("%d\n",sol);
        else printf("Fegla Won\n");
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
