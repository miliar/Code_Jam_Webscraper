#include<bits/stdc++.h>
#define mod 1000000007
#include<bits/stdc++.h>
#define mod 1000000007
#define pp pair<ll,ll>
#define mp make_pair
#define ll long long
#define ff first
#define ss second
#define big 100000000000000000
using namespace std;

ll tc,hsh[200],cnt;
string str,ans;

bool recur(ll cnt){
	if(cnt == 0)
		return 1;
//	cout<<"a"<<" "<<cnt<<"\n";
	bool temp;

	if(hsh['O'] && hsh['N'] && hsh['E']){
		hsh['O']--;
		hsh['N']--;
		hsh['E']--;
		temp = recur(cnt-3);
		if(temp){
			ans = '1'+ans;
//			cout<<'1'<<"\n";
			return 1;
		}
		hsh['O']++;
		hsh['N']++;
		hsh['E']++;
	}
	if(hsh['T'] && hsh['W'] && hsh['O']){
		hsh['T']--;
		hsh['W']--;
		hsh['O']--;
		temp = recur(cnt-3);
		if(temp){
//			cout<<'2'<<"\n";
			ans = '2'+ans;
			return 1;
		}
		hsh['T']++;
		hsh['W']++;
		hsh['O']++;
	}
	if(hsh['T'] && hsh['H'] && hsh['R'] && hsh['E'] >= 2){
		hsh['T']--;
		hsh['H']--;
		hsh['R']--;
		hsh['E'] -= 2;
		temp = recur(cnt-5);
		if(temp){
			ans = '3'+ans;
//			cout<<'3'<<"\n";
			return 1;
		}
		hsh['T']++;
		hsh['H']++;
		hsh['R']++;
		hsh['E'] += 2;
	}
	if(hsh['F'] && hsh['O'] && hsh['U'] && hsh['R']){
		hsh['O']--;
		hsh['F']--;
		hsh['U']--;
		hsh['R']--;
		temp = recur(cnt-4);
		if(temp){
//			cout<<'4'<<"\n";
			ans = '4'+ans;
			return 1;
		}
		hsh['O']++;
		hsh['F']++;
		hsh['U']++;
		hsh['R']++;
	}
	if(hsh['F'] && hsh['I'] && hsh['V'] && hsh['E']){
		hsh['F']--;
		hsh['I']--;
		hsh['V']--;
		hsh['E']--;
		temp = recur(cnt-4);
		if(temp){
			ans = '5'+ans;
//			cout<<'5'<<"\n";
			return 1;
		}
		hsh['F']++;
		hsh['I']++;
		hsh['V']++;
		hsh['E']++;
	}
	if(hsh['S'] && hsh['I'] && hsh['X']){
		hsh['S']--;
		hsh['I']--;
		hsh['X']--;
		temp = recur(cnt-3);
		if(temp){
			ans = '6'+ans;
//			cout<<'6'<<"\n";
			return 1;
		}
		hsh['S']++;
		hsh['I']++;
		hsh['X']++;
	}
	if(hsh['S'] && hsh['E'] >= 2 && hsh['V'] && hsh['N']){
		hsh['S']--;
		hsh['V']--;
		hsh['N']--;
		hsh['E'] -= 2;
		temp = recur(cnt-5);
		if(temp){
			ans = '7'+ans;
//			cout<<'7'<<"\n";
			return 1;
		}
		hsh['S']++;
		hsh['V']++;
		hsh['N']++;
		hsh['E'] += 2;
	}
	if(hsh['E'] && hsh['I'] && hsh['G'] && hsh['H'] && hsh['T']){
		hsh['E']--;
		hsh['I']--;
		hsh['G']--;
		hsh['H']--;
		hsh['T']--;
		temp = recur(cnt-5);
		if(temp){
			ans = '8'+ans;
//			cout<<'8'<<"\n";
			return 1;
		}
		hsh['E']++;
		hsh['I']++;
		hsh['G']++;
		hsh['H']++;
		hsh['T']++;
	}
	if(hsh['N'] >= 2 && hsh['I'] && hsh['E']){
		hsh['N']--;
		hsh['I']--;
		hsh['N']--;
		hsh['E']--;
		temp = recur(cnt-4);
		if(temp){
			ans = '9'+ans;
	//		cout<<'9'<<"\n";
			return 1;
		}
		hsh['N']++;
		hsh['I']++;
		hsh['N']++;
		hsh['E']++;
	}
	if(hsh['Z'] && hsh['E'] && hsh['R'] && hsh['O']){
		hsh['Z']--;
		hsh['E']--;
		hsh['R']--;
		hsh['O']--;
		temp = recur(cnt-4);
		if(temp){
			ans = '0'+ans;
	//		cout<<'0'<<"\n";
			return 1;
		}
		hsh['Z']++;
		hsh['E']++;
		hsh['R']++;
		hsh['O']++;
	}
	return 0;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(ll t=1;t<=tc;t++){
		cin>>str;
		
		ll n = str.length();
		memset(hsh,0,sizeof(hsh));
		for(ll i=0;i<n;i++){
			hsh[str[i]]++;
		}
		ans = "";
		recur(n);
		for(ll i=0;i<=ans.length();i++)
			hsh[ans[i]]++;
		ans="";
		for(ll i='0';i<='9';i++){
			while(hsh[i]){
				ans = ans+char(i);
				hsh[i]--;
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<"\n";
	}
	return 0;
}

