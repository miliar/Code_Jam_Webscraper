#include<bits/stdc++.h>
#define f(i,x,y) for (int i = x; i < y; i++)
#define fd(i,x,y) for(int i = x; i>= y; i--)
#define all(v) (v).begin(), (v).end()
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define cua(x) (x)*(x)
#define eps (1e-9)
#define oo (1<<30)
using namespace std;
string s;
int main(){
	int T,Smax,res,ans;
	cin >> T;
	f(ii,0,T){
		res=0;
		ans=0;
		cin >> Smax;
		cin >> s;
		f(i,0,s.length()){
			if(i>res&&s[i]!='0') { ans+=(i-res); res+=(i-res); }
			res+=(s[i]-'0');
		}
		cout << "Case #"<<ii+1<<": ";
		cout << ans << endl;
	}	
}