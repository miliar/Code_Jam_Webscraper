#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;
const int N = 35;
int Bit[N];
void to(long long n, int len)
{
	memset(Bit, 0 ,sizeof(Bit));
	for (int  i = len - 1;i >= 0;i --)
	{
		Bit[i] = n & 1;
		n >>= 1;
	}
}	
long long convert(int bit[N], int len, int base)
{
	long long ret = 0;
	long long c = 1;
	for (int i = len - 1;i >= 0;i --)
	{
		ret += c * bit[i];
		c *= base;
	}	
	return ret;
}
long long check(long long n)
{
	for (long long i = 2;i * i <= n;i ++)
	{
		if (n % i == 0)
		{
			return i;
		}
	}
	return -1;
}
int main(){
	int T;
	cin >> T;
	for (int cas = 1;cas <= T;cas ++)
	{
		int len, total;
		cin >> len >> total;
		cout << "Case #" << cas << ":" << endl;
		for (long long i = 1;i < (1LL << (len - 1));i += 2)
		{
			to(i + (1LL << (len - 1)), len);
			bool flag = true;
			vector<long long> tmp;
			for (int base = 2;base <= 10;base ++)
			{
				long long number = convert(Bit, len, base);
				long long ret = check(number);
	//			cout << (i + (1LL << (len - 1))) << " " << number << " " << ret << endl;
				if (ret == -1)
				{
					flag = false;
					break;
				}else{
					tmp.push_back(ret);
				}
			}
			if (flag && total > 0)
			{
				total --;
				for (int j = 0;j < len;j ++)
				{
					cout << Bit[j];
				}
				for (int j = 0;j < tmp.size();j ++)
				{
					cout << " " << tmp[j];
				}
				cout << endl;

			}
			if (total == 0)
			{
				break;
			}
					
		}
	}
	return 0;
}
