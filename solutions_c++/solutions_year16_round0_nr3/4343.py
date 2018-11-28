#include <iostream>
#include <string>
#include <cmath>
#include <stack>
#include <deque>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <iomanip>

using namespace std;

int N = 0;
int J = 0;
int num = 0;

int jj = 0;
vector <long long> v;
vector <int> w;



vector<int> sumVectors(vector<int> n, vector<int> m)
{
	int nSize = n.size();
	int mSize = m.size();
//	cout << nSize << " and " << mSize << endl;
	vector <int> ans;


	int rest = 0;

	if(nSize > mSize)
	{
		for(int i = 0; i < mSize; i++)
		{
			ans.push_back( (n[i] + m[i] + rest) % 10 );
			rest = (n[i] + m[i] + rest) / 10;
		}
		for(int i = mSize; i < nSize; i++ )
		{
			ans.push_back( (n[i] + rest) % 10 );
			rest = (n[i] + rest) / 10;
		}
	}
	else if(nSize < mSize)
	{
		for(int i = 0; i < nSize; i++)
		{
			ans.push_back( (n[i] + m[i] + rest) % 10 );
			rest = (n[i] + m[i] + rest) / 10;
		}
		for(int i = nSize; i < mSize; i++ )
		{
			ans.push_back( (m[i] + rest) % 10 );
			rest = (m[i] + rest) / 10;
		}
	}
	else
	{
		for(int i = 0; i < nSize; i++)
		{
			ans.push_back( (n[i] + m[i] + rest) % 10 );
			rest = (n[i] + m[i] + rest) / 10;
		}
	}

	if(rest > 0) ans.push_back(rest);


	return ans;
}

vector<int> multiplyVectors(vector<int> n, int k)
{
	vector <int> ans;
	int rest = 0;
	for(int i = 0; i < n.size(); i ++)
	{
		ans.push_back( (n[i] * k + rest) % 10 );
		rest = (n[i] * k + rest) / 10;
	}
	if(rest > 0) ans.push_back(rest);

	return ans;
}

vector<int> convert( int b)
{
//	cout << "vector w: ";
//	for(auto ssss: w)
//	{
//		cout << ssss;
//	}
//	cout << endl;
//	cout << "vector size: " << w.size() << " and base: " << b << endl;


	vector<int> ans;
	for(int i = N - 1; i >= 0; i--)
	{
		vector<int> n;
		if(w[i] != 0)
		{
			if(N - 1 - i > 17)
			{
				long long temp = pow(b, 17);
				while(temp > 0)
				{
					n.push_back(temp % 10);
					temp = temp / 10;
				}
				for (int z = 0; z < N - 1 - i - 17; z++)
				{
					n = multiplyVectors(n, b);
				}
			}
			else
			{
				long long temp = pow(b, N - 1 - i);
				while(temp > 0)
				{
					n.push_back(temp % 10);
					temp = temp / 10;
				}
			}

//			cout << "elments of n: ";
//			for(auto ssss: n)
//			{
//				cout << ssss;
//			}
//			cout << endl;

			ans = sumVectors(ans, n);

//			cout << "elments of ans: ";
//			for(auto ssss: ans)
//			{
//				cout << ssss;
//			}
//			cout << endl;
		}

	}

	return ans;
}

long long findDivisor(vector <int> n, int b)  // n is a number from right to left
{
	if((n[0] % 2 == 0 && n.size() > 1) || (n[0] % 2 == 0 && n[0] == 1 && n[0] > 2)) return 2;


	long long sq = pow(b, (N / 2 + 1));
//	cout << "sq: " << sq << endl;

	for(long long i = 2; i < sq ; i++ )
	{
		long long div = 0;
		long long x = 0;
		for(int a = n.size() - 1; a >= 0; a--)
		{
			x = x * 10 + n[a];
			if(x >= i)
			{
				div = div * 10 + x / i;
				x = x % i;
			}
			else
			{
				div = div * 10;
			}
		}
		if(x == 0) return i;   // OJO
	}

	return 0;
}



void vectorConbinations( int ii)
{
	if(J == num)
	{
		//system("PAUSE");
		return;
	}
	if(ii < N - 2)
	{
		//ii++;
		vectorConbinations(ii + 1);
		w[ii + 1] = 1;
		for(int h = ii + 2; h < N - 1; h++)
		{
			w[h] = 0;
		}
		vectorConbinations(ii + 1);
	}
	else
	{
//		////////////////
//		for(int h = 0; h < N; h++)
//		{
//			cout << w[h];
//		}
//		cout << endl;


			for(int b = 2; b < 11; b++)
			{
//				///////////////////////
//				w[0] = 1;
//				w[1] = 0;
//				w[2] = 0;
//				w[3] = 1;
//
//
//
//				///////////////////////
				long long ret = findDivisor( convert( b), b );
//				cout << "ret: " << ret << endl;


				if(ret != 0)
				{
					v[b] = ret;
					if(b == 10)
					{
						jj++;
						num++;
						for(int f = 0; f < N; f++)
						{
							cout << w[f];
						}
						for(int f = 2; f < 11; f++)
						{
							cout << " " << v[f];
						}
						cout << endl;

						v.resize(11, 0);
					}
				}
				else break;
			}
	}
}


int main()
{
	int T = 0;
	cin >> T;

	for (long long i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ":" << endl;
		cin >> N >> J;

		v.resize(11, 0);
		w.resize(N, 0);
		w[0] = 1;
		w[N - 1] = 1;

		int ii = 1;
		vectorConbinations(ii);
		w.clear();
		w.resize(N, 0);
		w[0] = 1;
		w[N - 1] = 1;
		w[ii] = 1;
		vectorConbinations(ii);
	}

	return 0;
}


