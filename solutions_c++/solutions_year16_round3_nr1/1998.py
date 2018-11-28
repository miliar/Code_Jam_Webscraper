#include<bits/stdc++.h>
#define sc(v) v.size()
#define eb push_back
#define pb pop_back
#define f(i,a,b) for(int i=a;i<b;i++)
#define TC() int t;cin>>t;while(t--)
#define all(x) x.begin(),x.end()
#define mk make_pair
#define fi first
#define se second
#define endl "\n"
#define eps 1e-9
#define pw(x) (1ll<<(x))
#define trace1(x)                cout <<#x<<": "<<x<<endl;
#define trace2(x, y)             cout <<#x<<": "<<x<<" | "<<#y<<": "<<y<< endl;
#define trace3(x, y, z)          cout <<#x<<": "<<x<<" | "<<#y<<": "<<y<<" | "<<#z<<": "<<z<<endl;
#define trace4(a, b, c, d)       cout <<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl;
#define trace5(a, b, c, d, e)    cout <<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<<": "<<e<<endl;
using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

inline bool EQ(double a,double b) { return fabs(a - b) < 1e-9; }
inline void set_bit(int & n, int b) { n |= pw(b); }
inline void unset_bit(int & n, int b) { n &= ~pw(b); }

const int N = 28;
int ar[N];
int main()
{
    #ifndef ONLINE_JUDGE
        //freopen("input.txt","r",stdin);
        //freopen("output.txt","w",stdout);
    #endif
    clock_t tStart = clock();
    priority_queue< pair<int,char> > pq;
    int tc = 1, n, sum;
    TC() {
        printf("Case #%d: ",tc++);
        scanf("%d",&n);
        while(!pq.empty())
            pq.pop();
        sum = 0;
        f(i,0,n) {
            scanf("%d",&ar[i]);
            sum += ar[i];
            char x = (char)('A' + i);
            pq.push(mk(ar[i],x));
        }
        while(!pq.empty()) {
            pair<int,char> a = pq.top();
            pq.pop();
            pair<int,char> b = mk(-1,'0');
            if(!pq.empty()) {
                b = pq.top();
                pq.pop();
            }
            if(b.fi == -1) {
                printf("%c",a.se);
                a.fi--;
                if(a.fi > 0) {
                    a.fi--;
                    printf("%c",a.se);
                }
                //trace1(a.fi);
                if(a.fi > 0)
                    pq.push(a);
                printf(" ");
            }
            else if(a.fi - b.fi >= 1) {
                printf("%c%c ",a.se,a.se);
                a.fi -= 2;
                if(a.fi > 0)
                    pq.push(a);
                pq.push(b);
            }
            else if(a.fi == b.fi) {
                printf("%c%c ",a.se,b.se);
                a.fi--;
                b.fi--;
                if(a.fi > 0)
                    pq.push(a);
                if(b.fi > 0)
                    pq.push(b);
            }
        }
        printf("\n");
    }
    //printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}


