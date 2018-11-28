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
#define ll long long
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

int ind[100];

int main()
{
    freopen("inp.txt" , "r+" , stdin);
    freopen("out.txt" , "w+" , stdout);
    int tcase,cas=1;

    scanf(" %d" ,&tcase);

    while(tcase--)
    {
        int ans;
        scanf(" %d" , &ans);
        clean(ind, 0);
        for(int i = 1 ; i<=4 ; i++)
            for(int j = 1 ; j<=4 ; j++)
            {
                int val;
                scanf(" %d",&val);
                if(i==ans) ind[val]++;
            }

        scanf(" %d" , &ans);
        for(int i = 1 ; i<=4 ; i++)
            for(int j = 1 ; j<=4 ; j++)
            {
                int val;
                scanf(" %d",&val);
                if(i==ans) ind[val]++;
            }

        int cnt = 0;
        int sol = -1;

        for(int i = 1 ; i<=16 ; i++)
        {
            if(ind[i]==2)
            {
                cnt++;
                sol = i;
            }
        }
        printf("Case #%d: ",cas++);

        if(cnt==0)
            printf("Volunteer cheated!\n");
        else if(cnt==1)
            printf("%d\n" , sol);
        else printf("Bad magician!\n");
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
