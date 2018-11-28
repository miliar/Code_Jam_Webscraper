#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<assert.h>
#define f_input freopen("a.txt","r",stdin)
#define f_output freopen("output.txt","w",stdout)
#define mem(x,y) memset(x,y,sizeof(x))
#include<iostream>
#define pb push_back
#define eps 1e-4
#define pp pair<int,int>
using namespace std;
typedef vector<int>vint;
typedef vector<long long int>vlong;
typedef vector<string>vstr;
typedef queue<int>Qint;
typedef map<int,int>Mii;
typedef map<string,int>Msi;
typedef map<int,string>Mis;
typedef long long int llint;
typedef stack<int>stk;
int fair[1000+5];
int rev_num(int n)
{
    int rev=0;
    while(n)
    {
        rev=rev*10+(n%10);
        n/=10;
    }
    return rev;
}
bool check(int n)
{
    int temp=n;
    int rev=0;
    int sq=sqrt(n);
    if(sq*sq==n)
    {
        if(rev_num(sq)==sq&&rev_num(n)==n)
        {
            return true;
        }
    }
    return false;
}
int main()
{
    f_input;
    f_output;
    fair[1]=1;
    for(int i=2;i<=1000;i++)
    {
        fair[i]=fair[i-1];
        if(check(i))
        {
            fair[i]++;
        }
    }
    int test,t;
    scanf("%d",&test);
    for(t=1;t<=test;t++)
    {
        int a,b;
        cin>>a>>b;
        printf("Case #%d: %d\n",t,fair[b]-fair[a-1]);
    }
    return 0;
}
