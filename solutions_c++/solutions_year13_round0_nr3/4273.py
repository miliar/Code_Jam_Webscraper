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


vector<long long> v1;

bool isPal(long long n)
{
    long long rem,s=0,temp;
    temp=n;
    while(n)
    {
        rem=n%10;
        s=(s*10)+rem;
        n/=10;
    }
    if(s==temp)
        return true;
    else
        return false;
}

void pre(long long int n)
{
    long long i;
    for(i=1;i*i<n;i++)
    {
        if(isPal(i))
        {
            long long aux=pow(i,2);
            if(isPal(aux))
            {
                //cout<<aux<<endl;
                v1.PB(aux);
            }
        }
    }
}

int main()
{
/*
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
*/
    long long i,t,a,b;
    scanf("%lld",&t);
    pre((long long int)100000000000000);
    REP(i,t)
    {
        scanf("%lld %lld",&a,&b);
        if(a>b)
            swap(a,b);
        vector<long long>:: iterator it1,it2;
        it1=lower_bound(v1.begin(),v1.end(),a);
        it2=lower_bound(v1.begin(),v1.end(),b);
        int cnt=0;
        cnt+=(it2-it1);
        //cout<<cnt<<" "<<(*it2)<<endl;
        if((*it1)==a && (*it2)==b)
            cnt++;
        else if((*it2)==b)
            cnt++;
        printf("Case #%d: ",i+1);
        printf("%d\n",cnt);
    }

/*
	fclose(stdin);
	fclose(stdout);
*/
   return 0;
}
