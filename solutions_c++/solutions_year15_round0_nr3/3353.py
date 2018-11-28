/****************************************  Author:       Sharad Gupta                       ***************************************************/
/****************************************  Institution:  IIIT - Hyderabad                   ***************************************************/

#include <bits/stdc++.h>
using namespace std;
#define VI vector < int >
#define VVI(A,N,M) vector< VI > A( N, VI (M) )
#define LL long long
#define LLU unsigned long long
#define PI acos(-1)
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int) (x).size()) 
#define SORT(c) sort(ALL(c)) 
#define FIT(it,v) for (typeof(v.begin()) it = v.begin(); it != v.end(); it++)
#define FITD(it,v) for (typeof(v.rbegin()) it = v.rbegin(); it != v.rend(); it++)
#define FOR(i,start,end) for(int i=start;i<end;i++)
#define IATOV(a) ({vector<int> v(a,a+sizeof(a)/sizeof(int));v;})
#define CATOV(a) ({vector<char> v(a,a+sizeof(a)/sizeof(char));v;})
#define sieve(a) ({int b=ceil(sqrt(a));VI d(a,0);VI e;int f=2;e.pb(2);e.pb(3);for(int x=1;x<b+1;x++){for(int y=1;y<b+1;y++){int n=(4*x*x)+(y*y);if(n<=a&&(n%12==1||n%12==5)){d[n]^=1;}n=(3*x*x)+(y*y);if(n<=a&&n%12==7){d[n]^=1;}n=(3*x*x)-(y*y);if(x>y&&n<=a&&n%12==11){d[n]^=1;}}}for(int r=5;r<b+1;r++){if(d[r]){for(int i=r*r;i<a;i+=(r*r)){d[i]=0;}}}for(int c=5;c<a;c++){if(d[c]){e.pb(c);}}e;})
#define INF 1000000007
#define EPS 1e-9
#define mt(x, y, z) mp(mp(x,y),z)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define setbits(x) __builtin_popcount(x) //tell number of 1's in binary form
#define GC getchar_unlocked
#define out_c(start,end) copy(start, end, ostream_iterator< typeof(*start) >(cout, " "));
template<class T>inline T modinv(T a,T n){T i=n,v=0,d=1;while(a>0){T t=i/a,x=a;a=i%x;i=x;x=d;d=v-t*x;v=x;}return (v+n)%n;}
LL modpow(LL n ,LL k,LL mod){LL ans=1;while(k>0){if(k&1)ans=(ans*n)%mod;k>>=1;n=(n*n)%mod;}return ans%mod;}
//template<class T>inline void output(T a){if(a){T v=a%10;output(a/10);putchar((char)(v+'0'));}}
//template<class T>inline T input(T x){char c=GC();x=0;T s=1;while(c<48||c>57){if(c=='-')s=-1;c=GC();}while(c>=48&&c<=57){x=(x<<3)+(x<<1)+c-48;c=GC();}return x*s;}

template <class T> string str(T Number){
	string Result;          // string which will contain the result
	ostringstream convert;   // stream used for the conversion
	convert << Number;      // insert the textual representation of 'Number' in the characters in the stream
	Result = convert.str();
	return Result;
}
int StringToNumber ( const string &Text )
{
     istringstream ss(Text);
     int result;
     return ss >> result ? result : 0;
}
template<class T> inline vector<pair<T,int> > FACTORISE(T n){vector<pair<T,int> >R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
template<class T> inline T TOTIENT(T n) {vector<pair<T,int> > R=FACTORISE(n);T r=n;for (int i=0;i<R.size();i++)r=r/R[i].first*(R[i].first-1);return r;}
template<class T>inline T gcd(T a,T b){return b?gcd(b,a%b):a;}
double rnd(float d) //for rounding values
{
	          return floor(d + 0.49);
}
int main(){
	int t;
	cin>>t;
	map<char,int> a;
	a['1']=0;
	a['i']=1;
	a['j']=2;
	a['k']=3;
	vector<vector<pair<int,char> > > A;
	vector<pair<int,char> > q;
	q.pb(mp(1,'1'));q.pb(mp(1,'i'));q.pb(mp(1,'j'));q.pb(mp(1,'k'));
	A.pb(q);
	q.clear();
	q.pb(mp(1,'i'));q.pb(mp(-1,'1'));q.pb(mp(1,'k'));q.pb(mp(-1,'j'));
	A.pb(q);
	q.clear();
	q.pb(mp(1,'j'));q.pb(mp(-1,'k'));q.pb(mp(-1,'1'));q.pb(mp(1,'i'));
	A.pb(q);
	q.clear();
	q.pb(mp(1,'k'));q.pb(mp(1,'j'));q.pb(mp(-1,'i'));q.pb(mp(-1,'1'));
	A.pb(q);
	q.clear();
	FOR(i,0,t)
	{
		int L,X;
		cin>>L>>X;
		string d,e;
		cin>>d;
		e=d;
		FOR(j,0,X-1)
		{
			e+=d;
		}
		int flag=0;
		char z=e[0];
		int signz=1;
		FOR(j,1,sz(e))
		{

			if(z=='i'&&signz==1)
			{
					char y=e[j];
					int signy=1;
					FOR(k,j+1,sz(e))
					{	
						if(y=='j'&&signy==1)
						{
								char x=e[k];
								int signx=1;
								FOR(l,k+1,sz(e))
								{
									int v=a[x];
									char f=e[l];
									int u=a[f];
									pair<int,char> w=A[v][u];
									x=w.second;
									signx*=w.first;
								}
								if(x=='k'&&signx==1)
								{
									flag=1;
									cout<<"Case #"<<i+1<<": YES"<<endl;
								}
								break;
						}

						int v=a[y];
						char f=e[k];
						int u=a[f];
						pair<int,char> w=A[v][u];
						y=w.second;
						signy*=w.first;

					}
					break;
			}
			
			int v=a[z];
			char f=e[j];
			int u=a[f];
			pair<int,char> w=A[v][u];
			z=w.second;
			signz*=w.first;
			
		}
		if(!flag)
		cout<<"Case #"<<i+1<<": NO"<<endl;

	}
	return 0;
}