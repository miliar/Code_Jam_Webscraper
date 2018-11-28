#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>
#include<queue>
#include<cmath>
#include<map>
#include<stack>
#include<bitset>
using namespace std;
#define REPF( i , a , b ) for ( int i = a ; i <= b ; ++ i )
#define REP( i , n ) for ( int i = 0 ; i < n ; ++ i )
#define CLEAR( a , x ) memset ( a , x , sizeof a )
typedef long long LL;
typedef pair<int,int>pil;
const int INF = 0x3f3f3f3f;
const int maxn=11000;
int t,L,X;
string str;
map<char,int>p;
int sum[maxn];
int cal(int a,int b)
{
    int flag=1;
    if(a<0)
    {
        flag=-flag;
        a=-a;
    }
    if(b<0)
    {
        flag=-flag;
        b=-b;
    }
    if(a==b)  return -1*flag;
    if(a==2&&b==3) return  4*flag;
    if(a==2&&b==4) return -3*flag;
    if(a==3&&b==2) return -4*flag;
    if(a==3&&b==4) return  2*flag;
    if(a==4&&b==2) return  3*flag;
    if(a==4&&b==3) return -2*flag;
    return flag*a*b;
}
int main()
{
//    freopen("D:\\360Downloads\\C-small-attempt4.in","r",stdin);
//    freopen("F:\\ANS\\out.txt","w",stdout);
    p['1']=1;p['i']=2;
    p['j']=3;p['k']=4;
    string temp;int cas=1;
    cin>>t;int a,b,c;
    while(t--)
    {
        int f1,f2,f3;
        cin>>L>>X;X=min(X,X%4+12);
        cin>>str;temp=str;
        L=X*L;
        for(int i=0;i<X-1;i++)
           str=str+temp;
        for(int i=0;i<L;i++)
        {
           if(i==0)  sum[i]=p[str[i]];
           else sum[i]=cal(sum[i-1],p[str[i]]);
        }
        int flag=0;
        for(int i=0;i<L;i++)
        {
            for(int j=i+1;j<L-1;j++)
            {
                f1=f2=f3=1;
                f1=sum[i];
                f2=cal(-sum[i],sum[j]);
                f3=cal(-sum[j],sum[L-1]);
                if(f1==2&&f2==3&&f3==4)
                {
                    flag=1;
                    break;
                }
            }
            if(flag)  break;
        }
        if(flag)  printf("Case #%d: YES\n",cas++);
        else  printf("Case #%d: NO\n",cas++);
    }
    return 0;
}
