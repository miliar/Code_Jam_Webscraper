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

vector<int> v;
int main(){
	int T,D,ss;
	cin >> T;
	f(ii,0,T){
		v.clear();
		cin >> D;
		f(i,0,D){ 
			int aux; 
			cin >> aux; 
			v.pb(aux); 
		}
		int block=2;
		sort(all(v));
		int ans=v.back();
		while(block<ans){
			ss=0;
			f(i,0,v.size())ss+=((v[i]-1)/block);
			ans=min(ans,ss+block);
			block++;
		}
		cout << "Case #"<<ii+1<<": "; 
		cout << ans << endl;

	}
}