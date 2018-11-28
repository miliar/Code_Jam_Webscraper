#include<bits/stdc++.h>

using namespace std;

int main() {
	int tCase;
	cin>>tCase;

	vector<char> orderCheck = {'Z','W','U','X','G','O','R','F','S','N'};
             vector<string> digits = {"ZERO","TWO","FOUR","SIX","EIGHT","ONE","THREE","FIVE","SEVEN","NINE"};

	for (int c=1; c<=tCase; ++c) {
		string s,ans = "";
		cin>>s;
		vector<int> count(26);
	
		for(int i=0,len = s.size(); i <len; ++i)	{
			++count[s[i]-'A'];
		}

		for(int j=0; j <10; ++j){				
			while( count[orderCheck[j] -'A'] > 0 ){
				for(int k=0; k<digits[j].size(); ++k) {
					--count[digits[j][k]-'A'];
				}
				j *= 2;
				if(j < 10)
					ans += to_string(j);
				else
					ans += to_string(j-9);
				j /= 2;
			}

		}	
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<c<<": "<<ans<<endl;		
	}
	return 0;
}