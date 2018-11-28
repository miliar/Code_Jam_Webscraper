#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
using namespace std;

typedef long long ll;

bool match( string s0, string s1){

	if (s0.length() != s1.length())return false;

	for (int i = 0; i < s0.length(); ++i){
		if (s0[i] == '?' || s0[i] == s1[i])
		{

		}
		else{
			return false;
		}
	}
	return true;
}

string addZero(int n, int len){

	stringstream ss;
	ss << n;
	string result = ss.str();
	//cout << result.length() << ";" << len << endl;
	int addNum = len-result.length();
	string add(addNum, '0');

	return add+result;
}

bool match2(string s, int n){
	int pos = 0;
	while (pos!=s.length()){
		if (s[s.length()-1-pos]=='?'||n==0&&s[s.length()-1-pos]=='0'||n!=0&&s[s.length() - 1 - pos] == (n % 10)+'0'){

		}
		else{
			return false;
		}
		++pos;
		n /= 10;
	}
	return true;
}

int main()
{
	ll T = 0;
	cin >> T;
	for (int _t = 1; _t <= T; ++_t){
		string s0, s1;
		cin >> s0;
		cin >> s1;
		int len = (int)s0.length()-1;
		int dig = 1;
		int bestDist = 100000000;
		for (int i = 0; i < len; ++i)dig *= 10;
		string code, jam;
		for (int i = 0; i < dig * 10; ++i){

			for (int j = 0; j < dig * 10; ++j){
			//	cout << i << ";" << j << endl;
				//string si = addZero(i, len + 1);
				//string sj =  addZero(j, len + 1);

				if (match2(s0, i) && match2(s1, j)){
					if (abs(i - j) < bestDist){
						bestDist = abs(i - j);
						code = addZero(i, len+1);
						jam = addZero(j,len+1);
					}
				}
			}
		}


		cout << "Case #" << _t << ": " << code << " "<<jam<<endl;
		cerr << "Case #" << _t << endl;// ": " << result << endl;
		
	}
}