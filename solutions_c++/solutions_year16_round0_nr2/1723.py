#include <iostream>
#include <vector>
using namespace std;

int main(){
	int T;
	string S;

	cin >> T;
	int I = T;

	while(T--){
		cin >> S;

		cout << "Case #" << I-T << ": ";

		char c = S[0];

		vector<char> v;

		v.push_back(c);

		for(int i=1;i<S.length();i++)
			if(S[i]!=c){
				v.push_back(S[i]);
				c = S[i];
			}

		int l = v.size();
		int ans;
		if(v[0]=='+')
		{
			if(l%2)
				ans = l-1;
			else
				ans = l;
		}
		else
		{
			if(l%2)
				ans = l;
			else
				ans = l-1;
		}

		cout << ans << endl;
	}

	return 0;
}