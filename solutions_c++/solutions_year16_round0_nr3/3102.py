#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

typedef long long ll;

using namespace std;

const int MAXP = 10000;

class Solution
{
private:
	vector<int> primes;
	bool flag[MAXP];
public:
	Solution()
	{
		memset(flag, 0, sizeof(flag));
		for (int i = 2; i < MAXP; ++i)
		{
			if (isPrime(i))
				primes.push_back(i);
		}
	}

	bool isPrime(int nr)
	{
		for (int d = 2; (d * d) < (nr + 1); ++d){
			if (!(nr % d)){
				return false;
			}
		}
		return true;
	}

	void getSolution(int i,int n,int j)
	{
		cout << "Case #" << i + 1 << ":" << endl;
		int start = (1 << (n - 1)) | 1, end = (1 << n) - 1;
		for (int k = start, base; k <= end; k += 2)
		{
			//cout << k << endl;
			vector<int> tmp;
			for (base = 2; base <= 10; ++base)
			{
				ll num = getNum(k, base);
				int prime = check(num);
				if (!prime) break;
				tmp.push_back(prime);
			}
			if (base > 10)
			{
				for (int i = n - 1; i >= 0; --i)
				{
					cout << ((k & (1 << i)) >> i);
				}
				for (auto prime : tmp)
					cout << " " << prime;
				cout << endl;
				if (--j == 0) break;
			}
		}
	}

	int check(ll num)
	{
		for (int p : primes) 
		{
			if (p >= num) break;
			if (num % p == 0 && num != p) return p;
		}
		return 0;
	}

	ll getNum(int x, int b)
	{
		ll ret = 0, top = 1;
		for (int i = 0; i <= 15; ++i) 
		{
			ret = top * (x & 1) + ret;
			top *= b;
			x >>= 1;
		}
		return ret;
	}

};

int main()
{
	//freopen("C:/Users/ywy/Desktop/large.in", "r", stdin);
	//freopen("C:/Users/ywy/Desktop/large-out.txt", "w", stdout);
	//freopen("C:/Users/ywy/Desktop/in.in", "r", stdin);
	//freopen("C:/Users/ywy/Desktop/out.txt", "w", stdout);
	int cases;
	cin >> cases;
	Solution ss;
	for (int i = 0; i < cases; ++i)
	{
		int n,j;
		cin >> n >> j;
		ss.getSolution(i,n,j);
	}
	return 0;
}


