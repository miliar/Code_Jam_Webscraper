#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

void reverse_and_replace(string &s){
	reverse(s.begin(), s.end());
	for(char& c : s) {
		c = (c == '+') ? '-' : '+';
	}
}

int calc(string s){

	if (s.find('+') == string::npos)
	{
		return 1;
	}
	else if (s.find('-') == string::npos)
	{
		return 0;
	}
	else
	{
		int out_maneuver_times = 0;
		string sub = "";

		for (int i = 0; i < s.size(); ++i)
		{
			if(s.find('-') == string::npos)
			{
				break;
			}
			else if(s.find('+') == string::npos)
			{
				reverse_and_replace(s);
				out_maneuver_times++;
				break;
			}
			else if(i == s.size() - 1)
			{
			}
			else if(s[i] == s[i+1])
			{
				continue;
			}
			else
			{
				sub = s.substr(0, i + 1);
				reverse_and_replace(sub);
				out_maneuver_times++;
				//cout << sub << endl;
				s = sub + s.substr(i + 1, s.size() - i + 1);
			}
		}

		return out_maneuver_times;
	}
}

int main(int argc, char const *argv[]){

	int t;
	vector<string> s;

	cin >> t;

	string ts;
	for (int i = 0; i < t; ++i)
	{
		cin >> ts;
		s.push_back(ts);
	}

	for (int i = 0; i < t; ++i)
	{	
		cout << "Case #" << (i + 1) << ": " << calc(s[i]) << endl;	
	}

	return 0;
}