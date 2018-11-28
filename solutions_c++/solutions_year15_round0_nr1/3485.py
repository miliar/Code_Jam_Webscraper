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
int main(){
   // freopen("input.txt", "r", stdin);
    geti(T);
    int c=1;
    while(T--){
    	geti(S);
    	string s;
    	cin >> s;
    	int cnt=0;
    	int avail=0;
    	rep(i,s.size()){
    		if((avail >= i) && (s[i]-'0'>0)){
    			avail+=s[i]-'0';
    			

    		}
    		else if(s[i]-'0' ==0){

    		}
    		else{


    			cnt+=(i-avail);
    			avail+=(s[i]-'0')+(i-avail);
    		}

    	}
    	cout << "Case #" << c++ <<": " << cnt << endl;

    }

	return 0;

}