#include<stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
using namespace std;
#define DEBUG
#define REP(i,a) for(i=0;i<a;i++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define VE vector<int>
#define SZ size()
#define PB push_back
int main()
{
    long long int t,n,flag,co,b,i,j;
    freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    cin>>t;
    for(int o=1;o<=t;o++)
    {
        flag=0;
        cin>>n;
        co=0;
        string str;
        cin>>str;
        for(int i=0;i<=n;i++)
        {
            if(co>=i)
            {
                int jk = str[i] - '0';
                co=co+jk;
            }
            else
            {
                flag++;
                co=co+1;
                co=co+(str[i] - '0');
            }
        }
        printf("Case #%d: %d\n",o,flag);

    }
   return 0;
}
