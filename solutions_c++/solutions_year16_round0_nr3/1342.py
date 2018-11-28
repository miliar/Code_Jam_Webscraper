#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	mp make_pair
#define	pb push_back
#define sz(a) int((a).size())
#define all(a)  a.begin(), a.end()
#define	debug(ccc)	cout << #ccc << " = " << ccc << endl;
#define present(c,x) ((c).find(x) != (c).end())
const double eps = 1e-8;
#define EQ(a,b) (fabs((a)-(b))<eps)
inline int max(int a,int b){return a<b?b:a;}
inline int min(int a,int b){return a>b?b:a;}
inline ll max(ll a,ll b){return a<b?b:a;}
inline ll min(ll a,ll b){return a>b?b:a;}
const int mod = 1e9+7;
const int N = 1e6+10;
const ll inf = 1e18;

ll power(ll a,ll n){
	if(n==0){
		return 1;
	}
	ll b = power(a,n/2);
	b = b*b%mod;
	if(n%2) b= b*a%mod;
	return b;
}

int add(int a,int b){ return (a+b)%mod;}
int mul(int a,int b){ return (ll)a*b%mod;}



map < ll , ll > M;
map < string , string > M1;

string ff(ll num){
	string r = "";
	while(num>0){
		if(num%10==1)	r.pb('1');
		else r.pb('0');
		num/=10;	
	}
	reverse(all(r));
	return r;
}

int main(){
 // 	freopen("nice.in","r",stdin);
 // freopen("nice.out","w",stdout);
	int cnt = 0;
	REPP(i,2,(1<<9)){
		REPP(j,i,(1<<16)){
			if(i%2==0 || j%2==0)	continue;
			if(i*j>=(1<<16))	break;
			if(i*j<(1<<15))	continue;
			ll n1 = 0 , p = 1 , c = i;
			while(c>0){
				if(c&1){
					n1 += p;
				}
				p*=10;c/=2;
			}
			ll n2 = 0 ;
			p = 1 , c = j;
			while(c>0){
				if(c&1){
					n2+= p;
				}
				p*=10, c/=2;
			}
			ll n = n1*n2;
			int f=0;
			while(n>0){
				if(n%10!=0 and n%10!=1){
					f=1;break;
				}
				n/=10;
			}
			if(f==0){
				cnt++;
				M[n1*n2]=n1;
				ll q = n1 , r = (ll)1e15;
				while(q<r)	q*=10;
				string a1 = ff(q) + ff(n1*n2);
				M1[a1] = ff(n1);
				// printf("%lld %lld %lld\n",n1*n2,n1,n2);
			}

		}
	}
	cnt = 0;
	printf("Case #1:\n");
	// foreach(M,it){
	// 	cnt++;
	// 	printf("%lld ",it->X);
	// 	REPP(i,2,11){
	// 		ll n = it->X , n1 = it->Y;
	// 		ll p = 1;
	// 		ll num1 = 0, num2 = 0;
	// 		int c=0;
	// 		while(n>0 || n1>0){
	// 			if(n%10)		num1+= p;	
	// 			if(n1%10)	   num2+=p;
	// 			n/=10;n1/=10,p*=i;c++;
	// 		}
	// 		printf("%lld ",num2);
	// 		assert(num1%num2==0 and num2!=num1 and num2!=1 and c==16);
	// 	}
	// 	printf("\n");
	// 	if(cnt==500)	break;
	// }

	assert(M1.size()>=500);
	foreach(M1,it){
		cnt++;
		cout<<it->X<<" ";
		REPP(i,2,11){
			string a = it->X , a1 = it->Y;
			
			reverse(all(a));reverse(all(a1));

			assert((int)a.size()==32 and a1.size()<=16);
			// printf("%d\n",(int)a.size());
			ll p = 1 , num2 = 0;
			REP(j,a1.size()){
				if(a1[j]=='1'){
					num2+=p;
				}
				p*=i;
			}
			p=1;
			ll num1 = 0;
			REP(j,16){
				if(a[j]=='1')	num1+=p;
				p*=i;
			}
			// cout<<
			// printf("%d\n",i);
			assert(num1%num2==0);
			num1 = 0; p = 1;
			// printf("%d\n",i);
			printf("%lld ",num2);
			REPP(j,16,32){
				if(a[j]=='1')	num1+=p;
				p*=i;
			}
			assert(num1%num2==0);
		}
		printf("\n");
		if(cnt==500)	break;
	}

	return 0;
}


