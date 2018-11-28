#include<bits/stdc++.h>
using namespace std;
#define ll long long 

int hash[26]={0};
	
int check(){
	for(int i=0;i<26;i++)
		if(hash[i]!=0)
			return 1;
			
	return 0;
}

int main(){
ll int t,m=1;
cin>>t;
while(t--){
	string s;
	cin>>s;
	int cnt[10]={0};
	for(int i=0;i<s.length();i++){
		hash[s[i]-'A']++;
		//cout<<s[i]<<hash[s[i]-'A']<<endl;
	}
	
	
			while(hash['Z'-'A']!=0){
				hash['Z'-'A']--;
				hash['E'-'A']--;
				hash['R'-'A']--;
				hash['O'-'A']--;
				cnt[0]++;
			}
			while(hash['W'-'A']!=0){
				hash['T'-'A']--;
				hash['W'-'A']--;
				hash['O'-'A']--;
				cnt[2]++;
			}
			while(hash['R'-'A']!=0 && hash['U'-'A']!=0 && hash['O'-'A']!=0 && hash['F'-'A']!=0){
				hash['F'-'A']--;
				hash['O'-'A']--;
				hash['U'-'A']--;
				hash['R'-'A']--;
				cnt[4]++;
			}
			while( hash['E'-'A']!=0&& hash['V'-'A']!=0&& hash['I'-'A']!=0&& hash['F'-'A']!=0){
				hash['F'-'A']--;
				hash['I'-'A']--;
				hash['V'-'A']--;
				hash['E'-'A']--;
				cnt[5]++;
			}
			while(hash['S'-'A']!=0&& hash['I'-'A']!=0&& hash['X'-'A']!=0){
				hash['S'-'A']--;
				hash['I'-'A']--;
				hash['X'-'A']--;
				cnt[6]++;
			}
			while(hash['S'-'A']!=0&& hash['E'-'A']-1!=0&& hash['V'-'A']!=0&& hash['E'-'A']!=0&& hash['N'-'A']!=0){
				hash['S'-'A']--;
				hash['E'-'A']--;
				hash['V'-'A']--;
				hash['E'-'A']--;
				hash['N'-'A']--;
				cnt[7]++;
			}
			while(hash['E'-'A']!=0&& hash['I'-'A']!=0&& hash['G'-'A']!=0&& hash['H'-'A']!=0&& hash['T'-'A']!=0){
				hash['E'-'A']--;
				hash['I'-'A']--;
				hash['G'-'A']--;
				hash['H'-'A']--;
				hash['T'-'A']--;
				cnt[8]++;
			}
			while(hash['N'-'A']!=0 && hash['I'-'A']!=0 && hash['N'-'A']-1!=0&& hash['E'-'A']!=0){
				hash['N'-'A']--;
				hash['I'-'A']--;
				hash['N'-'A']--;
				hash['E'-'A']--;
				cnt[9]++;
			}
			while(hash['O'-'A']!=0 && hash['N'-'A']!=0 && hash['E'-'A']!=0){
				hash['O'-'A']--;
				hash['N'-'A']--;
				hash['E'-'A']--;
				cnt[1]++;
			}
			while(hash['E'-'A']!=0 &&hash['E'-'A']-1!=0 &&hash['R'-'A']!=0 &&hash['H'-'A']!=0 && hash['T'-'A']!=0 ){
				hash['T'-'A']--;
				hash['H'-'A']--;
				hash['R'-'A']--;
				hash['E'-'A']--;
				hash['E'-'A']--;
				cnt[3]++;
			}
		cout<<"Case #"<<m++<<": ";	
		for(int i=0;i<10;i++){
			for(int j=0;j<cnt[i];j++)
				cout<<i;
		}
		cout<<endl;
}
return 0;
}