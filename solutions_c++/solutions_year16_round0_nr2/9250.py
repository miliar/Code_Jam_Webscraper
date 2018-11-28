#include <bits/stdc++.h>

using namespace std;
 
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int,int> pii;
typedef vector< pii > vii;
typedef long long ll;
 
#define tcase int __t;cin >> __t; while( __t--)
#define fr(i,a,b) for(int i=a;i<b;i++)
#define rp(i,b) fr(i,0,b)
#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define inf 1 << 32

int main(){
	int t,j,ans=0;
	string s;
	char ch;
	cin >> t;
	for(int i=0;i<t;i++){
		cin >>s;
		j=0;
		ans=0;
		if(s[j] == '-'){
			ans++;
		}
		while(s[j]=='-' && j<s.size()){
			j++;
		}
		while(j<s.size()){
			if(s[j]=='+'){
				j++;
				continue;
			}
			else{
				ans=ans+2;
				j++;
				while(s[j]=='-' && j<s.size()){
					j++;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}