//HUHUHAHA

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long l;
typedef double dbl;
typedef pair<int , int> pll;

#define endl '\n'


ll i , j;


int main(){
	
	freopen("A-large.in" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);
	
	ios::sync_with_stdio(0);
	int t;cin>>t;
	for(int T =1 ; T<=t ;T++){
		
		l n;
		cin>>n;
		string c = "          " , fin = "1111111111";
		
		if(!n)cout<<"Case #"<<T<<": "<<"INSOMNIA"<<endl;
		else{
			j = 1;ll tmp , ans;
			while(c != fin){
				tmp = j*n;ans = tmp;
				while(tmp){
					int tm = tmp%10;
					c[tm] = '1';
					tmp/=10;
				}
				j++;
			}
			cout<<"Case #"<<T<<": "<<ans<<endl;
		}
	}
	
	return 0;
}
