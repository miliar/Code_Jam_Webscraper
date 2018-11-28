/**
Prashant Gupta(GHOST_YO)
IIITA
**/
#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(i=a;i<b;i++)
#define Ford(i,a,b) for(i=a;i>=b;i--)
#define Rep(i,c) for(__typeof(c.begin()) it(c.begin());i!=c.end();i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define modul 1000000007
#define infi 99999999
#define BUG(x) {cout<<#x<<" = "<<x<<endl;}
#define PR(x,a,b) {For(i,a,b+1)cout<<x[i]<<' ';cout<<endl;}
#define FILL(a,x) memset(a,x,sizeof(a));
#define sc(a) scanf("%d", &a)
#define pii pair<int,int>
#define ll long long
#define PI acos(-1)
#define gc getchar
#define pc putchar
#define TIN {cout<<"Time started\n";time_t __t_v=clock();
#define TOUT cout<<"Time Taken : "<<(clock()-__t_v)/(double)CLOCKS_PER_SEC<<"\n";}

inline void scanint(int &x){register int c=0;x=0;int flag=0;for(;((c!=45)&&(c<48||c>57));c=gc());
for(;((c==45)||(c>47&&c<58));c=gc()){if(c==45)flag=1;else x=(x<<1)+(x<<3)+c-48;}if(flag)x=-x;}

int has[11];

int fnc(int n)
{
    while(n > 0) {
        has[n%10] = 1;
        n/=10;
    }
}

bool check()
{
    int i;
    For(i, 0, 10)
        if(!has[i])
            return true;
    return false;
}

int main()
{
    freopen("inp1.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	int t,n,i;
	int id = 1;
	sc(t);

	while(t--) {
        FILL(has, 0);
        sc(n);

        if(n == 0) {
            cout << "Case #" << id++ << ": INSOMNIA\n";
            continue;
        }
        int x = n;
        fnc(n);
        while(true) {
            fnc(n);
            if(!check())
                break;
            n += x;
        }

        cout << "case #" << id++ << ": " << n << endl;
	}
	return 0;
}
