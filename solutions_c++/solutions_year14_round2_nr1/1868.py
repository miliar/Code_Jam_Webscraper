#include <bits/stdc++.h>
using namespace std;

#define lli long long int

int main()
{
	int T, t;
	cin >> T;
	for(t = 1; t <= T; ++t)
	{
		int n, i, j;
		string str[3];
		cin >> n;		
		for(i = 0; i < n; ++i){
			cin >> str[i];
		}
		printf("Case #%d: ", t); 
		
		int stp = 0;
		if(str[0][0] == str[1][0]){
			for(i = 1, j = 1; i < str[0].size() || j < str[1].size();)
			{
				if(i == str[0].size()){
					if(str[1][j] != str[1][j - 1]) break;
					++stp;
					++j;
				}
				else if(j == str[1].size()){
					if(str[0][i] != str[0][i - 1]) break;
					++stp;
					++i;
				}
				else if(str[0][i] == str[1][j]){
					++i;
					++j;
				}
				else if(str[0][i] == str[0][i - 1]){
					++stp;
					++i;
				}
				else if(str[1][j] == str[1][j - 1]){
					++stp;
					++j;
				}
				else{
					break;
				}
			}
			if(i == str[0].size() && j == str[1].size()){
				cout << stp << endl;
			}
			else{
				cout << "Fegla Won\n";
			}
		}
		else{
			cout << "Fegla Won\n";
		}
		
	}
	return 0;
}
