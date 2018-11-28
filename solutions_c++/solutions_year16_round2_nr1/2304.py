#include<iostream>
#include<string>
#include<cstring>
#include<map>

using namespace std;

int main()
{
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		string s; cin >> s;
		int count[26];
		memset(count,0,26*sizeof(int));
		int digits[10];
		memset(digits,0,10*sizeof(int));
		int len = s.length();
		map<int,string> MM;
		MM[0] = "ZERO";
		MM[1] = "ONE";
		MM[2] = "TWO";
		MM[3] = "THREE";
		MM[4] = "FOUR";
		MM[5] = "FIVE";
		MM[6] = "SIX";
		MM[7] = "SEVEN";
		MM[8] = "EIGHT";
		MM[9] = "NINE";
		for (int j = 0; j < len; j++) {
			count[s[j]-'A']++;
		}
		int temp[] = {25,22,20,6,23,7,14,5,21,4};
		int t2[] = {0,2,4,8,6,3,1,5,7,9};
		for (int j = 0; j < 10; j++) 
		{
			digits[t2[j]] += count[temp[j]];
			string num = MM[t2[j]];
			for (int k = 0; k < num.length(); k++) {
				count[num[k]-'A'] -= digits[t2[j]];
			}
		}
		string ans = "";
		for (int j = 0; j < 10; j++) {
			char c = '0'+j;
			ans += string(digits[j],c);
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
}
