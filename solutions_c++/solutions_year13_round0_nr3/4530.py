#include<stdio.h>
#include<string.h>
#include<string>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#define vvi vector<vector<int> >
#define pii pair<int,int>
#define vpii vector< vector<pair<int,int> > >
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define ABS(a) (a<0?-1*(a):a)
#define pi 2 * acos (0.0)


using namespace std;
bool palindram(long long t)
{
    string s,s1;
    while(t)
    {
        s+=t%10+'0';
        t/=10;
    }
    s1=s;
    reverse(s1.begin(),s1.end());
    if(s==s1)   return true;
    return false;
}
int main()
{
    int tcase,co=1;
    long long l,h,i,k;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out_small.txt","w",stdout);
    scanf("%d",&tcase);
    while(tcase--)
    {
        scanf("%lld %lld",&l,&h);
        int c=0;
        for(i=l;i<=h;i++)
        {
            if(palindram(i))
            {
                k=sqrt(i);
                if(k*k==i && palindram(k))
                    c++;
            }
        }
        printf("Case #%d: %d\n",co++,c);
    }
    return 0;
}
