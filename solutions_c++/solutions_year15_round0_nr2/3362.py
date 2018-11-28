#include <bits/stdc++.h>
using namespace std;
//cout << fixed << setprecision(4);
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef stringstream ss;
#define geti(n) int n;scanf("%d",&n)
#define getl(n) long long n;scanf("%lld",&n)
#define getc(c) char c;cin >> c
#define rep(i,n) for(int i=0;i<n;i++)
#define puti(n) printf("%d\n",n)
#define putl(n) printf("%lld\n",n)
#define ll long long
#define pb push_back
#define mem(p,q) memset(p,q,sizeof(p))
#define fu(i,a,n) for(int i=a;i<n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define mp make_pair
int a[1010];
bool f[10];
int main(){
    //freopen("input.txt", "r", stdin);
    geti(T);
    int test=1;
    while(T--){
    	int ans=0;
    	mem(f,1);
    	int _max=0;
    	geti(N);
    	rep(i,N){
    		geti(p);
    		a[i]=p;
    		_max=max(_max,a[i]);


    	}
    int res=_max;
    fu(i,1,_max){
    	int tmp=i;
    	ans=0;
    	rep(j,N){
    		if(a[j]<=i){


    		}
    		else{
    		if(a[j]%i ==0){
    			ans+=a[j]/i-1;
    		}
    		else{
    			//tmp=max(tmp,i+(a[j]%i));
    			tmp=i;
    			ans+=a[j]/i;

    			


    		}
    	}

    	}
    	res=min(res,ans+tmp);
    	
    }
    cout << "Case #"<< test++ << ": " << res << endl;
   }

	return 0;

}