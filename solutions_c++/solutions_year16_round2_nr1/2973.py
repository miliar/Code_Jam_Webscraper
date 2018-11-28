#include<bits/stdc++.h>
using namespace std;
string s;
bool checks(string s1){
	int i=0, flag;
	map<int, int> pos;
	for(i=0;i<s1.length();i++){
		flag=1;
		for (int j = 0; j < s.length(); ++j)
		{

			if(s[j]==s1[i]){
				if(pos[j]==0){
					flag=0;
					pos[j]=1;break;
				}
				//pos.push_back(j);
			}
		}
		if(flag)return false;
	}
	map<int, int>::iterator it;
		for (it = pos.begin(); it!=pos.end(); it++)
		{
			s[it->first]='1';
		}
	return true;
}

int main(int argc, char const *argv[])
{
	freopen("input1large.in", "r", stdin);
	freopen("output1large.in", "w", stdout);
	int t, n,  j , k;
	string s1;
	k=1;
	cin>>t;
	j=1;
	getchar();
	string ans;
	while(t--){
		cin>>s;
		/*ans.clear();
		s1="ZERO";
		while(checks(s1)){
			ans.push_back('0');
		}
		s1="ONE";
		while(checks(s1)){
			ans.push_back('1');
		}
		s1="TWO";
		while(checks(s1)){
			ans.push_back('2');
		}
		s1="THREE";
		while(checks(s1)){
			ans.push_back('3');
		}
		s1="FOUR";
		while(checks(s1)){
			ans.push_back('4');
		}
		s1="FIVE";
		while(checks(s1)){
			ans.push_back('5');
		}
		s1="SIX";
		while(checks(s1)){
			ans.push_back('6');
		}
		s1="SEVEN";
		while(checks(s1)){
			ans.push_back('7');
		}
		s1="EIGHT";
		while(checks(s1)){
			ans.push_back('8');
		}
		s1="NINE";
		while(checks(s1)){
			ans.push_back('9');
		}*/
			ans.clear();

		int arr[26];
		memset(arr, 0, sizeof(arr));
		for(int i=0;i<s.length();i++){
			arr[s[i]-'A']++;
		}
		//cout<<endl;
		j=arr['Z'-'A'];
		arr['Z'-'A']-=j;
		arr['E'-'A']-=j;
		arr['R'-'A']-=j;
		arr['O'-'A']-=j;
		for (int i = 0; i < j; ++i)
		{
			ans.push_back('0');
		}
		
		j=arr['W'-'A'];
		//j=min(arr['T'-'A'], min(arr['W'-'A'], arr['O'-'A']));
		arr['T'-'A']-=j;
		arr['W'-'A']-=j;
		arr['O'-'A']-=j;
		for (int i = 0; i < j; ++i)
		{
			ans.push_back('2');
		}
		//j=min(arr['F'-'A'], min(arr['O'-'A'], min(arr['U'-'A'], arr['R'-'A'])));
		j=arr['U'-'A'];
		arr['F'-'A']-=j;
		arr['O'-'A']-=j;
		arr['U'-'A']-=j;
		arr['R'-'A']-=j;
		for (int i = 0; i < j; ++i)
		{
			ans.push_back('4');
		}
		j=arr['F'-'A'];
		//j=min(arr['F'-'A'], min(arr['I'-'A'], min(arr['V'-'A'], arr['E'-'A'])));
		arr['F'-'A']-=j;
		arr['I'-'A']-=j;
		arr['V'-'A']-=j;
		arr['E'-'A']-=j;
		for (int i = 0; i < j; ++i)
		{
			ans.push_back('5');
		}
		j=arr['X'-'A'];
		//j=min(arr['S'-'A'], min(arr['I'-'A'], arr['X'-'A']));
		arr['S'-'A']-=j;
		arr['I'-'A']-=j;
		arr['X'-'A']-=j;
		//arr['R'-'A']-=j;
		for (int i = 0; i < j; ++i)
		{
			ans.push_back('6');
		}
		j=arr['V'-'A'];
		//j=min(arr['S'-'A'], min(arr['E'-'A']/2, min(arr['V'-'A'], arr['N'-'A'])));
		arr['S'-'A']-=j;
		arr['E'-'A']-=2*j;
		arr['V'-'A']-=j;
		arr['N'-'A']-=j;
		for (int i = 0; i < j; ++i)
		{
			ans.push_back('7');
		}
		j=arr['G'-'A'];
		//j=min(arr['E'-'A'], min(arr['I'-'A'], min(arr['G'-'A'], min(arr['H'-'A'], arr['T'-'A']))));
		arr['E'-'A']-=j;
		arr['I'-'A']-=j;
		arr['G'-'A']-=j;
		arr['H'-'A']-=j;
		arr['T'-'A']-=j;
		for (int i = 0; i < j; ++i)
		{
			ans.push_back('8');
		}
		j=arr['O'-'A'];
		//j=min(arr['O'-'A'], min(arr['N'-'A'], arr['E'-'A']));
		arr['E'-'A']-=j;
		arr['N'-'A']-=j;
		arr['O'-'A']-=j;
		for (int i = 0; i < j; ++i)
		{
			ans.push_back('1');
		}
		j=arr['T'-'A'];
		//j=min(arr['T'-'A'], min(arr['H'-'A'], min(arr['R'-'A'], arr['E'-'A']/2)));
		arr['T'-'A']-=j;
		arr['H'-'A']-=j;
		arr['R'-'A']-=j;
		arr['E'-'A']-=2*j;
		for (int i = 0; i < j; ++i)
		{
			ans.push_back('3');
		}
		j=arr['I'-'A'];
		//j=min(arr['N'-'A']/2, min(arr['I'-'A'], arr['E'-'A']));
		arr['N'-'A']-=j*2;
		arr['I'-'A']-=j;
		//arr['N'-'A']-=j;
		arr['E'-'A']-=j;
		for (int i = 0; i < j; ++i)
		{
			ans.push_back('9');
		}
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<k<<": "<<ans<<endl;
		k++;
	}



	return 0;
}