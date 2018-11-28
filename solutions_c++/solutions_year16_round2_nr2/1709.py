#include<bits/stdc++.h>
#define MAXN 100009
#define INF 1000000007
#define imx 2147483647
#define LLINF 1000000000000000007
#define mp(x,y) make_pair(x,y)
#define wr cout<<"Continue Debugging!!!"<<endl;
#define ff first
#define ss second
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
#define ppb() pop_back()
#define tr(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
using namespace std;
typedef long long ll;
typedef pair<int,int>PII;
template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}

int mn,a,b;
int arr[77],ten[7];
string s,t,as,bs,cs,ds;
void full(){
	int c=0;
	cs.resize(0);
	ds.resize(0);
	for(int i=0;i<s.size();i++){
		int h;
		if(s[i]!='?')
			cs+=s[i],as[i]=s[i];
		else
			cs+=char(48+arr[++c]),as[i]=char(48+arr[c]);
	}
	for(int i=0;i<t.size();i++){
		int h;
		if(t[i]!='?')
			ds+=t[i],bs[i]=t[i];
		else
			ds+=char(48+arr[++c]),bs[i]=char(48+arr[c]);
	}
}
void fun(int x,int y){
	if(x>y){
		int c=0;
		int _a=0,_b=0;	
		for(int i=0;i<s.size();i++){
			int h;
			if(s[i]!='?')
				h=s[i]-'0';
			else
				h=arr[++c];	
			_a+=h*ten[s.size()-i-1];	
		}
		for(int i=0;i<t.size();i++){
			int h;
			if(t[i]!='?')
				h=t[i]-'0';
			else
				h=arr[++c];	
			_b+=h*ten[t.size()-i-1];	
		}
		if(abs(_a-_b)<mn)
			a=_a,b=_b,mn=abs(_a-_b),full();
		else if(abs(_a-_b)==mn){
			if(_a<a)
				a=_a,b=_b,full();
			else if(_a==a and _b<b)
				b=_b,full();
		}
		return;
	}
	for(int i=0;i<10;i++)
		arr[x]=i,fun(x+1,y);
}
int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	ten[0]=1;
	for(int i=1;i<7;i++)
		ten[i]=ten[i-1]*10;
	int tt;
	scanf("%d",&tt);
	for(int test=1;test<=tt;test++){
		cin>>s>>t;
		mn=a=b=INF;
		int mark=0;
		for(int i=0;i<s.size();i++){
			if(s[i]=='?')
				mark++;
			if(t[i]=='?')
				mark++;	
		}
		fun(1,mark);
		printf("Case #%d: ",test);
	//	cout<<a<<" "<<b<<endl;
	//	assert(as==cs and bs==ds);
	//	cout<<as<<" "<<bs<<endl;
		cout<<cs<<" "<<ds<<endl;
	}
	return 0;
}
//LooK aT mY COde ONlinE +_+

