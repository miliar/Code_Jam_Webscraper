#include<bits/stdc++.h>

using namespace std;


#define ms(x,val) memset(x,val,sizeof(x))
#define scan(x) scanf("%d",&x)
#define scanL(x) scanf("%I64d",&x)
#define print(x) printf("%d\n",x)
#define debug(x) printf("DEBUG: %d\n",x)
#define printL(x) printf("%I64d\n",x)
#define ull unsigned long long
#define iii long long
#define pi acos(-1)
#define pb push_back
#define PII pair<int,int>
#define vi vector<int>
#define printv(vec) for(int i=0;i<vec.size();i++)cout<<vec[i]<<' ';cout<<endl;
#define itr_all(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MAPL map<long long, int > 
#define MAPI map<int,int> 
#define MAPP map< pair<int,int> , int>
#define MP make_pair
#define eps 1e-9
#define inf 999999999
#define MAXN 1000009
#define MOD 1000000007 // 10^9 + 7

template <class T> inline T bigmod(T p,T e,T M)
{
    iii ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template < class T > T gcd(T a , T b ) { if(b==0) return a; else return gcd(b, a%b);}
template < class T > T lcm(T a , T b ) { return  a*b / gcd(a, b);}
template < class T > T absolute(T a ) { if(a>0) return a; else return -a;}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}
inline iii power(iii base,iii p) { iii ans=1; while(p>0) ans*=base,p-=1; return ans;}


map<int,bool> mp;
int cnt;

void calc(iii n){
	int dgt;
	while(n){
		dgt=n%10;
		if(mp.find(dgt)==mp.end()){
			mp[dgt]=true;
			cnt++;
		}
		n/=10;
	}
}






int main()
{
//	  ios::sync_with_stdio(false);
//	  freopen("a1.in","r",stdin);
//	  freopen("a1.txt","w",stdout);

	int t,cases=1;
	iii n,i;

	scan(t);
	while(t--){
		cin>>n;
		mp.clear();
		if(n==0){
			printf("Case #%d: INSOMNIA\n",cases++);
			continue;
		}
		cnt=0;
		i=0;
		while(cnt<10){
			calc(n*i);
			i++;
		}
		printf("Case #%d: %lld\n",cases++,n*(i-1));
	}

	


	return 0;
}

