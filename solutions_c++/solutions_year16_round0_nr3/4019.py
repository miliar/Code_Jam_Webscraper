#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
typedef long long BIGNUM;

bool check(BIGNUM number)
{
	string s = "";
	BIGNUM n = number;
	while( n > 0)
	{
		s = s + char(48 + n%2);
		n = n/2;
	}
	//cout <<"nhiphan:"<<s<<endl;
	vector<BIGNUM>uoc;
	for(int base = 2; base <= 10; base++)
	{
		BIGNUM vl = 0;
		for (int i = 0; i < s.length(); i++)
			vl += (BIGNUM)(pow(base,i)*(s[i]-48));
		//cout <<"base"<<base<<" checkPrimerNum:"<<vl<<endl;
		bool valid = false;
		for (BIGNUM i = 2; i <= sqrt(vl); i++)
			if (vl % i == 0)
			{
				valid = true;
				uoc.push_back(i);
				break;
				// cout <<"valid:"<<i<<" "<<(vl/i) <<endl;
			}
		if (valid == false)
		{
			return false;
		}
	}
	for (int i = s.length(); i >= 0; i--)
		cout <<s[i];
	for (int i = 0; i < uoc.size(); i++)
		cout <<" "<<uoc[i];
	cout <<endl;
	return true;
}
int main() {
	// your code goes here
	int testcase;
	cin >> testcase;
	for (int test = 1; test <= testcase; test++)
	{
		cout <<"Case #"<<test<<":"<<endl;
		int n,j;
		cin >> n >> j;
		int rsCount = 0;
		int minNum = 1 << n-1;
		int maxNum = 1 << n;
		for (int num = minNum; num < maxNum; num++)
		{
			//cout <<"xet:"<<num<<endl;
			if (num & 1 == 1)
			{
				bool isValid = check(num);
				if (isValid)
				{
					rsCount ++;
					if (rsCount == j)
						break;
				}
			}
		}
	}
	return 0;
}