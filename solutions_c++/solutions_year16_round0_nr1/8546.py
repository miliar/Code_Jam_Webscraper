#include <bits/stdc++.h>
#define ll long long
using namespace std;
int a[1000006][11];
ll ans[1000006];
void g(int num,ll i){
	ll x = i;
	while(x){
		a[num][x%10]=1;
		x/=10;
	}
}
int f(int i){
	for(int j = 0;j < 10; j++){
		if(!a[i][j])return 0;
	}
	return 1;
}
void solve()
{
	ll maxv = -1;
	for(int j = 1;j < 1000005; j++){
		for(int k = 0;k < 1000005; k++){
			ll c = k*j;
			maxv= max(maxv,c);
			g(j,c);
			if(f(j)){
				ans[j] = c;
				break;
			}
			if(k == 1000004){
				cout<<j<<" "<<"INSOMINIA \n";
			}
		}
	}
	//cout<<"MAX "<<maxv<<endl;
}
int main(){
	freopen("inp.txt","r",stdin);
	//freopen("this.txt","w",stdout);
 	solve();
 	int t;
 	cin>>t;
 	int y =1;
 	while(y<=t){
 		int x;
 		cin>>x;
 		printf("Case #%d: ",y);
 		if(x == 0){
 			cout<<"INSOMNIA";
 		}
 		else cout<<ans[x];
 		y++;
 		printf("\n");
 	}
}
