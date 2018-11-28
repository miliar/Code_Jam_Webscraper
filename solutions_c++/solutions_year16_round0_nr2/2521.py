#include<bits/stdc++.h>
 
using namespace std;
 
#define dbg(x) cerr << (#x) << " --> " << (x) << endl
#define lli long long int
#define pii pair<int,int>
#define mod 1000000007
#define N (int)(1e5+10)
#define mp make_pair
#define pb push_back
#define nd second
#define st first
#define endl '\n'
#define inf mod
#define sag (sol|1)
#define sol (root<<1)
#define ort ((bas+son)>>1)

int i,j,k,n,m,x,y,z,ans,t;
string str;

int main(){
	cin >> t;

	for(i=1 ; i<=t ; i++){
		ans=0;
		cin >> str;

		printf("Case #%d: ",i);
			
		int p=str.size()-1;

		while(p>=0 and str[p] == '+')
			p--;
		str = str.substr(0,p+1);

		while(str.size()){
			int p=0,w=0;
			while(p<str.size() and str[p] == '+'){
				str[p]='-';
				w=1;
				p++;
			}
			if(p == str.size())
				break;
			p=str.size()-1;
			ans += w;
			reverse(str.begin(),str.end());

			while(p>=0 and str[p] == '-')
				p--;

			str = str.substr(0,p+1);

			for(j=0 ; j<str.size() ; j++){
				if(str[j] == '+')
					str[j] = '-';
				else
					str[j] = '+';
			}
			ans++;
		}

		cout << ans << endl;
	}
}
