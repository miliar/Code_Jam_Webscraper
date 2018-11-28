
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;
class Solution{

	bool isPali(string & s){
		int n = s.size();
		for (int i = 0; i < n/2; ++i)
		{
			if (s[i] != s[n - i - 1])
			{
				return false;
			}
		}
		return true;
	}
	void check(string & num){
		long long root = atol(num.c_str());
		long long square = root * root;
		string res = ltoa(square);
		if (square >= a && square <= b && isPali(res))
		{
			++count;
		}
	}
	void buildPali(const string & low, const string & high, int left, int right, string & cur){
		if (left > right)
		{
			check(cur);
			return;
		}
		char start = '0';
		char end = '9';
		if (left == 0)
		{
			start = '1';
		}
		if (cur.size() == low.size())
		{
			start = low[left];
		}
		if (cur.size() == high.size())
		{
			end = high[left];
		}
		for (char i = start; i <= end ; ++i)
		{
			cur[left] = cur[right] = i;
			buildPali(low, high, left+1, right - 1, cur);
		}
	}
	string ltoa(long long num){
		string res;
		stringstream ss;
		ss<<num;
		ss>>res;
		return res;
	}
public:
	void solve(){
		count = 0;
		string a_str;
		string b_str;
		long long root_a = sqrt(a);
		long long root_b = sqrt(b);
		a_str = ltoa(root_a);
		b_str = ltoa(root_b);
		for(int i = a_str.size(); i <= b_str.size(); ++i){
			string cur(i, '0');
			buildPali(a_str, b_str, 0, i -1, cur);
		}
		printf("Case #%d: %d\n", c, count);
	}
	int count;
	long long a;
	long long b;
	int c;
};

int main()
{
    int t;
    ifstream ios("C-small-attempt0.in");
	ios>>t;
	long long a,b;
	Solution s;
	for (int p = 1; p <= t; ++p){
		ios>>a>>b;
		s.a = a;
		s.b = b;
		s.c = p;
		s.solve();
	}
    ios.close();
    return 0;
}