#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		string s;
		cin>>s;
		vector<int> v[s.length()+1];
		v[0].push_back(0);
		v[0].push_back(0);
		for (int j = 0; j < s.length(); j++) {
			j++;
			if(s[j-1]=='+') {
				v[j].push_back(v[j-1][0]);
				v[j].push_back(v[j-1][0] + 1);
			} else {
				v[j].push_back(v[j-1][1] + 1);
				v[j].push_back(v[j-1][1]);
			}
			j--;
		}
		cout<<"Case #"<<i+1<<": "<<v[s.length()][0]<<endl;
	}
	return 0;
}