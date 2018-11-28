#include<iostream>
#include<algorithm>
#include<math.h>
#include<stack>
#include<limits.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<utility>
#include<map>
#include<vector>
#include<set>
#include<queue>
#include<deque>
#include<iterator>
#include <sstream>
#include <fstream>
using namespace std;
#define sci(n) scanf("%d",&n)
#define scl(n) scanf("%ld",&n)
#define scll(n) scanf("%lld",&n)
#define scs(a) scanf("%s",a)
#define pri(n) printf("%d",n)
#define prl(n) printf("%ld",n)
#define prll(n) printf("%lld",n)
#define pnl printf("\n")
#define pr_ printf(" ")
#define ll long long int
#define l long int
#define mp make_pair
#define re(i,n) for(i=0;i<n;i++)
#define repin(i,a,b) for(i=a;i>=b;i--)
#define rep(i,a,b) for(i=a;i<b;i++)
#define init(arr) memset(arr,0, sizeof(arr)) 
#define pairs pair<int,int>
#define fi first
#define se second
#define mod 1000000007
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	ll t,turn=1,num=1;
	cin>>t;
	while(t--){
		map<char,int> mp;
		vector<int> ans;
		string s;
		cin>>s;
		//cout<<s<<endl;
		int i;
		for(i=0;i<26;i++){
			mp[i+'A']=0;
		}
		for(i=0;i<s.length();i++){
			mp[s[i]]++;
		}
		while(mp['Z']!=0){
			ans.push_back(0);
			mp['Z']--;
			mp['E']--;
			mp['R']--;
			mp['O']--;
		}
		while(mp['W']!=0){
			ans.push_back(2);
			mp['T']--;
			mp['W']--;
			mp['O']--;
		}
		while(mp['G']!=0){
			ans.push_back(8);
			mp['E']--;
			mp['I']--;
			mp['G']--;
			mp['H']--;
			mp['T']--;
		}
		while(mp['X']!=0){
			ans.push_back(6);
			mp['S']--;
			mp['I']--;
			mp['X']--;
		}
		while(mp['S']!=0){
			ans.push_back(7);
			mp['S']--;
			mp['E']--;
			mp['V']--;
			mp['E']--;
			mp['N']--;
		}
		while(mp['V']!=0){
			ans.push_back(5);
			mp['F']--;
			mp['I']--;
			mp['V']--;
			mp['E']--;
		}
		while(mp['F']!=0){
			ans.push_back(4);
			mp['F']--;
			mp['O']--;
			mp['U']--;
			mp['R']--;
		}
		while(mp['O']!=0){
			ans.push_back(1);
			mp['O']--;
			mp['N']--;
			mp['E']--;
		}
		while(mp['T']!=0){
			//cout<<mp['T'];
			ans.push_back(3);
			mp['T']--;
			mp['H']--;
			mp['R']--;
			mp['E']--;
			mp['E']--;
		}
		while(mp['N']!=0){
			ans.push_back(9);
			mp['N']--;
			mp['I']--;
			mp['N']--;
			mp['E']--;
		}
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<turn<<": "; 
		turn++;
		for(i=0;i<ans.size();i++){
			cout<<ans[i];
		}
		cout<<endl;
	}
}
