//#include <bits/stdc++.h>
//using namespace std;
//typedef long long LL;
//typedef long double LD;
//typedef unsigned long long ULL;
//typedef pair<int, int> PI;
//typedef pair<PI, PI > PII;
//const double eps=1e-5;
//const LL mod=1e9+7;
//const double pi=acos(-1.0);
//const int MAXN=201000;
//const int MAXM=299900;
//const int N=1e6+5;
//int n,m,a[12345];
//int main()
//{
//    int t;
//    cin>>t;
//    while(t--)
//    {
//        cin>>n>>m;
//        for(int i=0;i<m;i++)
//        {
//            scanf("%d",&a[i]);
//        }
//
//    }
//    return 0;
//}

#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair<int, int> PI;
typedef pair<PI, PI > PII;
const double eps=1e-5;
const int inf=1e5;
const LL mod=1e9+7;
const double pi=acos(-1.0);
const int N=1e3+5;
int n,k;
int prim[23]={2,3,5,7,11,13,17,19,23};
vector<int>omg;
vector<int>out[1000];
int yes(LL w)
{
    omg.clear();
    int wei[123];
    for(LL i=2;i<=10;i++)
    {
        LL x=w;
        LL now=0,hh=1,c=0;
        while(x)
        {
            wei[c++]=x%2;
            if(x%2)
                now+=hh;
            hh*=i;
            x/=2;
        }
        int ans=0;
        for(int j=0;j<9;j++)
        {
            if(now%prim[j]==0){
                ans=1;
                omg.push_back(prim[j]);
                break;
            }
        }
        if(ans==0) return 0;
    }
    for(int i=n-1;i>=0;i--)
        printf("%d",wei[i]);
    for(int i=0;i<omg.size();i++)
    {
        printf(" %d",omg[i]);
    }
    puts("");
    return 1;
}
int main()
{
    freopen("C:/Users/Kewowlo/Desktop/1.in","r",stdin);
    freopen("C:/Users/Kewowlo/Desktop/2.out","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        printf("Case #%d:\n",cas++);
        LL now = 1<<(n-1);
        now +=1;
        for(int i=0;i<k;i++)
        {
            while(!yes(now))
            {
                now+=2;
            }
            now+=2;
        }
    }
    return 0;
}
/*
+-+-+-++--
*/
