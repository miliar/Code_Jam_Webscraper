#include <bits/stdc++.h>

using namespace std;

int main(){
	int t,n,z=1;
	string s;
	cin>>t;
	while(t--){
		cin>>s;
		int l = s.length(),k;
		int a[26]={0};
		vector<int>ans;
		for(int i=0;i<l;++i){
			a[s.at(i)-65]++;
		}
		while(a['Z'-65]--){
			a['E'-65]--;
			a['O'-65]--;
			a['R'-65]--;
			ans.push_back(0);
		}
		while(a['W'-65]--){
			a['T'-65]--;
			a['O'-65]--;
			ans.push_back(2);
		}
		while(a['U'-65]--){
			a['F'-65]--;
			a['O'-65]--;
			a['R'-65]--;
			ans.push_back(4);
		}
		while(a['X'-65]--){
			a['S'-65]--;
			a['I'-65]--;
			ans.push_back(6);
		}
		while(a['G'-65]--){
			a['E'-65]--;
			a['I'-65]--;
			a['H'-65]--;
			a['T'-65]--;	
			ans.push_back(8);
		}
		while(a['R'-65]--){
			a['T'-65]--;
			a['H'-65]--;
			a['E'-65]-=2;
			ans.push_back(3);
		}
		while(a['S'-65]--){
			a['E'-65]-=2;
			a['V'-65]--;
			a['N'-65]--;
			ans.push_back(7);
		}
		while(a['O'-65]--){
			a['N'-65]--;
			a['E'-65]--;
			ans.push_back(1);
		}	
		while(a['V'-65]--){
			a['F'-65]--;
			a['I'-65]--;
			a['E'-65]--;
			ans.push_back(5);
		}
		while(a['I'-65]--){
			a['N'-65]-=2;
			a['E'-65]--;
			ans.push_back(9);
		}
		
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<z++<<": ";
		for(int i=0;i<ans.size();++i)
			cout<<ans[i];
		/*for(int i=0;i<26;++i)
		{
			if(a[i])
				cout<<i<<endl;
		}*/
		cout<<endl;
	}
	return 0;
}