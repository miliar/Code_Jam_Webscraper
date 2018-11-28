#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DEBUG
#define REP(i,a) for(i=0;i<a;i++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define VE vector<int>
#define SZ size()
#define PB push_back
#define all(i) (i).begin(), (i).end()
#define PI acos(-1.0)
#define ii pair<int,int>
#define inf_ll (((1LL<<62)-1)<<1)+1
#define inf_i 1<<31-1


int main()
{
/*
   freopen("A-small-attempt0.in","r",stdin);
   freopen("output.txt","w",stdout);
*/
    int i,test;
    long long int r,t;
    scanf("%d",&test);
    REP(i,test)
    {
        cin>>r>>t;

        long long int s=0,aux=r;
        int cnt=0;
        while(s<=t)
        {
            s+=(long long int)(2*aux+1);
            if(s<=t)
                cnt++;
            aux+=2;
        }
        printf("Case #%d: %d\n",i+1,cnt);
    }

/*
	fclose(stdin);
	fclose(stdout);
*/
   return 0;
}
