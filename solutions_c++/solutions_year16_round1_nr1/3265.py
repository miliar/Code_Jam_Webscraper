#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

string getAnswer(string s)
{
	char gr = s[0];
	//vector<int> arr(s.size(),0);
	string ans1(s.begin(), s.begin()+1), ans2;
	for(int i = 1; i < s.size(); ++i){
		if(s[i] >= gr){
			gr = s[i];
			ans1 += gr;
		}
		else
			ans2 += s[i];
	}
	reverse(ans1.begin(), ans1.end());
	ans1 += ans2;
	return ans1;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i){
		string s;
		cin >> s;
		cout << "Case #" << i << ": " << getAnswer(s) << endl;
	}
	return 0;
}