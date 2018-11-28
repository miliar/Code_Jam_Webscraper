#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;
int main(){
	int t;
	cin>>t;
	cin.ignore();
	for(int q=1;q<=t;q++){
		string s;
		cin>>s;
		int arr[26]={0};
		for(int i=0;i<s.length();i++)
			arr[s[i]-'A']++;
		int count=s.length();
		vector<int> result;
		for(int i=0;i<arr['Z'-'A'];){
			count-=4;
			arr['Z'-'A']--;
			arr['E'-'A']--;
			arr['R'-'A']--;
			arr['O'-'A']--;
			result.push_back(0);
		}
		for(int i=0;i<arr['W'-'A'];){
			count-=3;
			arr['T'-'A']--;
			arr['W'-'A']--;
			arr['O'-'A']--;
			result.push_back(2);
		}
		for(int i=0;i<arr['U'-'A'];){
			count-=4;
			arr['F'-'A']--;
			arr['O'-'A']--;
			arr['U'-'A']--;
			arr['R'-'A']--;
			result.push_back(4);
		}
		for(int i=0;i<arr['X'-'A'];){
			count-=3;
			arr['S'-'A']--;
			arr['I'-'A']--;
			arr['X'-'A']--;
			result.push_back(6);
		}
		for(int i=0;i<arr['G'-'A'];){
			count-=5;
			arr['E'-'A']--;
			arr['I'-'A']--;
			arr['G'-'A']--;
			arr['H'-'A']--;
			arr['T'-'A']--;
			result.push_back(8);
		}
		for(int i=0;i<arr['O'-'A'];){
			count-=3;
			arr['O'-'A']--;
			arr['N'-'A']--;
			arr['E'-'A']--;
			result.push_back(1);
		}
		for(int i=0;i<arr['R'-'A'];){
			count-=5;
			arr['T'-'A']--;
			arr['H'-'A']--;
			arr['R'-'A']--;
			arr['E'-'A']--;
			arr['E'-'A']--;
			result.push_back(3);
		}
		for(int i=0;i<arr['F'-'A'];){
			count-=4;
			arr['F'-'A']--;
			arr['I'-'A']--;
			arr['V'-'A']--;
			arr['E'-'A']--;
			result.push_back(5);
		}
		for(int i=0;i<arr['S'-'A'];){
			count-=5;
			arr['S'-'A']--;
			arr['E'-'A']--;
			arr['V'-'A']--;
			arr['E'-'A']--;
			arr['N'-'A']--;
			result.push_back(7);
		}
		while(count>0){
			count-=4;
			result.push_back(9);
		}
		sort(result.begin(),result.end());
		printf("Case #%d: ",q);
		for(int i=0;i<result.size();i++)
			cout<<result[i];
		cout<<endl;
	}
	return 0;
}
