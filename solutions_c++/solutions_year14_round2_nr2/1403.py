/*
ID: amr.f.eldfrawy
LANG: C++
*/
#include <fstream>
#include <string>
#include<iostream>
#include<stdio.h>
#include<vector>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<math.h>
#define INF 1000000
#define MOD  1000000007
#define MAX 100000
using namespace std;

int main()
{
    freopen("S.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n , m , k,t;
    cin >> t;

    int s ;
    for(int h = 1 ; h <=t; h++)
    {
        long long  ans = 0 ;
        cin >> n >> m >> k;
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<m; j++)
            {
                s=0;
                s = i&j;
                if(s<k)
                    ans++;
            }
        }
        printf("Case #%d: %lld\n",h,ans);
    }






    return 0;

}
