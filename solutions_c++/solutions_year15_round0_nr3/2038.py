#include<bits/stdc++.h>

using namespace std;

#define ll long long int 
#define ss1(a) scanf("%d",&a)
#define ss2(a,b) scanf("%d %d",&a,&b)
#define ss3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define loop(i,a,b) for(int i=a;i<b;i++)
#define loope(i,a,b) for(int i=a;i<=b;i++)
#define loopd(i,a,b) for(int i=a;i>=b;i--)
#define Loop(i,a,b) for(ll i=a;i<b;i++)
#define Loope(i,a,b) for(ll i=a;i<=b;i++)
#define Loopd(i,a,b) for(ll i=a;i>=b;i--)

#define pii pair<int,int>
typedef vector<int> vi; 
typedef vector< vi > vvi;  
#define setzero(a) fill(a,a+sizeof(a),0);
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp(a,b) make_pair(a,b)
#define F first
#define S second
#define DEBUG if(0)

ll gcd(ll a,ll b){ return (b==0)?a:gcd(b,a%b); } ll lcm(ll a, ll b) { return (a*b)/gcd(a,b); }
ll modpow(ll a, ll n, ll mod){ ll res=1; while(n){ if(n&1)res=(res*a)%mod; a=(a*a)%mod; n>>=1; } return res; }
ll lpow(ll a, ll n){ ll res=1; while(n){ if(n&1)res*=a; a*=a; n>>=1; } return res; }
/*******************************MAIN CODE STARTS*******************************/

ll l,X;
string s;
int h[10010];
int invh[10010];
map < char,int > m1;
int m2[5];
int mul[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int cnt[10][10];
int bs;

void pre()
{
	m1['1']=1; 
	m1['i']=2; 
	m1['j']=3; 
	m1['k']=4; 
	
}

int Mul(int x,int y)
{
	return (x/abs(x))*(y/abs(y))*mul[abs(x)][abs(y)];
}

void Scan()
{
	cin>>l>>X>>s;
	
	int x=1,y;
	for(int i=0;i<sz(s);i++)
	{
		y=m1[s[i]];
		x=Mul(x,y);
		h[i]=x;
		//cout<<h[i]<<" ";
	}
	bs=x;	m2[0]=1; m2[1]=bs; m2[2]=-1; m2[3]=-bs;
	//cout<<endl;
	
	y=1;
	for(int i=sz(s)-1;i>=0;i--)
	{
		x=m1[s[i]];
		y=Mul(x,y);
		invh[i]=y;
	}
	
	//assert(bs==y);
	
	for(int i=0;i<=8;i++) for(int j=0;j<=9;j++) cnt[i][j]=0;
	return;
}


int simple()
{
	string S;
	while(X--)
	{
		S+=s;
	}
	int p=-1,q=-1;
	int x=1,y;
	for(int i=0;i<sz(S);i++)
	{
		y=m1[S[i]];
		x=Mul(x,y);
		if(x==2) 
		{
			p=i;
			break;
		}	
	
	}
	
	y=1;
	for(int i=sz(S)-1;i>=0;i--)
	{
		x=m1[S[i]];
		y=Mul(x,y);
		if(y==4)
		{
			q=i;
			break;
		}
	}
	
	if(p==-1 || q==-1) return 0;
	if(p+1>=q) return 0;
	x=1;
	for(int i=p+1;i<q;i++)
	{
		y=m1[S[i]];
		x=Mul(x,y);
	}
	if(x==3) return 1;
	else return 0;
}

int Out()
{
	if(X*l<=10000)
	//if(X<=9) 
		return simple();
	string S;
	for(int i=0;i<4;i++)
	{
		S+=s;
	}
	int p=-1,q=-1;
	int x=1,y,xt=1,yt=1;
	for(int i=0;i<sz(S);i++)
	{
		y=m1[S[i]];
		x=Mul(x,y);
		if(x==2) 
		{
			p=i;
			x=1;
			break;
		}	
	}
	for(int i=p+1;i<sz(S);i++) xt=Mul(xt,m1[S[i]]);
	
	y=1;
	for(int i=sz(S)-1;i>=0;i--)
	{
		x=m1[S[i]];
		y=Mul(x,y);
		if(y==4)
		{
			q=i;
			y=1;
			break;
		}
	}
	for(int i=0;i<q;i++) 
	{
		yt=Mul(yt,m1[S[i]]);
	}	
	
	if(p==-1 || q==-1) return 0;
	int cmid=X-8,mod=4; if(bs==1 || bs==-1) mod=2;
	int mid=m2[cmid%mod];
	
	//cout<<p<<" "<<q<<" "<<xt<<" "<<yt<<" "<<bs<<" "<<mid<<" "<<cmid<<endl;
	int z=Mul(xt,mid); z=Mul(z,yt);
	if(z==3) return 1;
	return 0;
}

int main()
{
	pre();
	int t; cin>>t;
	loope(z,1,t)
	{
		Scan();
		printf("Case #%d: ",z);
		if(Out()) cout<<"YES\n";
		else cout<<"NO\n";
	}
	return 0;
}
