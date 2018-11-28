#include<bits/stdc++.h>
using namespace std;
struct point {int x;int y;};
bool operator <(const point &a,const point &b){return (a.x<b.x);}
int compare (const void * a, const void * b){return ( *(int*)a - *(int*)b );}
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) REP(i,0,b)
#define si(n) scanf("%d",&n)
//#define sort(arrr,n) qsort(arrr,n,sizeof(int),compare)
int gcd(int a, int b){return (b==0)?a:gcd(b,a%b);}
int main()
{
    int tc,i,j,u,val[16],a[16],b[16],r1,r2,ans;
    cin >> tc;
    rep(u,tc)
    {
        rep(i,16)
            val[i]=0;
        si(r1);
        rep(i,16)
        {
            si(a[i]);
            if(i/4 == (r1-1))
                val[a[i]-1]++;
        }
        si(r2);
        rep(i,16)
        {
            si(b[i]);
            if(i/4 == (r2-1))
                val[b[i]-1]++;
        }
        int cnt=0;
        rep(i,16)
            if(val[i]==2)
            {
                ans=i+1;
                cnt++;
            }
        cout << "Case #" << u+1 << ": ";
        if(cnt==1)
            cout << ans << endl;
        if(cnt>1)
            cout << "Bad magician!\n";
        if(cnt==0)
            cout << "Volunteer cheated!\n";
    }
	return 0;
}
