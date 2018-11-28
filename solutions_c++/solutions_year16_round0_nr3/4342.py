#include <iostream>
using namespace std;
const int MAX = 50;
const int N_MAX = 32;
const int BASE_MIN = 2;
const int BASE_MAX = 10;
const int BASE_CNT = BASE_MAX - BASE_MIN + 1;

// index 0 is least position
struct StrInt
{
	int maxPos;
	char data[MAX];

	void CopyFrom(const StrInt& src)
	{
		maxPos = src.maxPos;
		for (int i = 0; i < MAX; ++i)
		{
			data[i] = src.data[i];
		}
	}

	void CopyTo(StrInt& dst)
	{
		dst.maxPos = maxPos;
		for (int i = 0; i < MAX; ++i)
		{
			dst.data[i] = data[i];
		}
	}

	void Plus(const StrInt& op1, const StrInt& op2)
	{
		int pos = op1.maxPos > op2.maxPos ? op1.maxPos : op2.maxPos;
		int cur;
		int carry = 0;
		for (int i = 0; i <= pos + 1; ++i)
		{
			cur = (op1.data[i] - '0') + (op2.data[i] - '0');
			cur += carry;
			carry = cur / 10;
			data[i] = cur % 10 + '0';
			if (i == MAX - 1 && carry > 0)
			{
				return;
			}
		}

		if (data[pos + 1] == '1')
		{
			maxPos = pos + 1;
		}
		maxPos = pos;
	}

	// n must be only small value
	bool Multiply(int n)
	{
		StrInt backup(*this);
		int cur = 0;
		int carry = 0;
		for (int i = 0; i < MAX; ++i)
		{
			cur = data[i] - '0';
			cur *= n;
			cur += carry;
			carry = cur / 10;
			data[i] = (cur % 10) + '0';
			if (i == MAX - 1 && carry > 0)
			{
				CopyFrom(backup);
				return false;
			}
			if (carry == 0 && i >= maxPos)
			{
				break;
			}
		}

		for (int i = MAX - 1; i >= 0; --i)
		{
			if (data[i] != '0')
			{
				maxPos = i;
				break;
			}
		}

		return true;
	}

	// n must be only small value
	bool Divide(int n)
	{
		StrInt backup(*this);
		int cur = 0;
		for (int i = maxPos; i >= 0; --i)
		{
			cur += data[i] - '0';
			data[i] = (cur / n) + '0';
			cur %= n;
			if (i == 0 && cur != 0)
			{
				CopyFrom(backup);
				return false;
			}
			cur *= 10;
		}

		for (int i = maxPos; i >= 0; --i)
		{
			if (data[i] != '0')
			{
				maxPos = i;
				break;
			}
		}

		return true;
	}

	void Print()
	{
		for (int i = maxPos; i >= 0; --i)
		{
			cout << data[i];
		}
		cout << endl;
	}

	StrInt()
	{
		for (int i = 0; i < MAX; ++i)
		{
			data[i] = '0';
		}
		maxPos = -1;
	}
	StrInt(char* pStr, int len)
	{
		for (int i = len; i < MAX; ++i)
		{
			data[i] = '0';
		}
		maxPos = -1;

		for (int i = 0; i < len; ++i)
		{
			data[i] = pStr[len - 1 - i];
			if (pStr[len - 1 - i] != '0')
			{
				maxPos = i;
			}
		}
	}
	StrInt(const StrInt& src)
	{
		maxPos = src.maxPos;
		for (int i = 0; i < MAX; ++i)
		{
			data[i] = src.data[i];
		}
	}
};


StrInt gBase[BASE_CNT][N_MAX];



int main(void)
{
	// make each base
	for (int i = 0; i < BASE_CNT; ++i)
	{
		StrInt src("1", 1);
		for (int k = 0; k < N_MAX; ++k)
		{
			gBase[i][k].CopyFrom(src);
			src.Multiply(i + BASE_MIN);
			//gBase[i][k].Print(); // for debugging
		}
	}

	int t;
	int n, j;

	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> n >> j;
		cout << "Case #" << i << ":" << endl;
		StrInt base[BASE_CNT];
		for (int k = 0; k < BASE_CNT; ++k)
		{
			base[k].Plus(gBase[k][0], gBase[k][n - 1]);
			//base[k].Print(); // for debugging
		}
		StrInt cur[BASE_CNT];
		int cnt = 0;
		int k = 0;

		// fix as  bs         ae  be  fix
		// 0   1   2  ... n-4 n-3 n-2 n-1
		// fix as  bs cs ds    ae  be  ce  de  fix
		// 0   1   2  3  4 ... n-5 n-4 n-3 n-2 n-1
		int a = 1;
		int b = 2;
		int c = 3;
		int d = 4;
		bool fourMode = false;
		int divider[BASE_CNT];
		const int dCnt = 20;
		int div[dCnt] = {
			2, 3, 5, 7, 11, 
			13, 17, 19, 23, 29, 
			31, 37, 41, 43, 47, 
			53, 59, 61, 67, 71 };
		// 2 added loop
		while (true)
		{
			if (fourMode == false)
			{
				StrInt temp;
				temp.Plus(base[k], gBase[k][a]);
				cur[k].Plus(temp, gBase[k][b]);
			}
			else
			{
				StrInt temp;
				temp.Plus(gBase[k][a], gBase[k][b]);
				StrInt temp2;
				temp2.Plus(gBase[k][c], gBase[k][d]);
				StrInt temp3;
				temp3.Plus(temp, temp2);

				cur[k].Plus(base[k], temp3);

			}


			int di;
			for (di = 0; di < dCnt; ++di)
			{
				if (cur[k].Divide(div[di]))
				{
					//cout << "cur[" << k << "]: ";
					//cur[k].Print();
					//cout << "div[di]:   " << div[di] << endl;
					divider[k] = div[di];
					break;
				}
			}

			if (di >= dCnt)
			{
				k = 0;
				// skip and next
				if (fourMode == false)
				{
					//cout << "Fail : a" << a << "b" << b << endl; // for debugging
					// fix as  bs         ae  be  fix
					// 0   1   2  ... n-4 n-3 n-2 n-1
					if (b <= n - 3)
					{
						b++; // up to index n-2
						continue;
					}

					if (a <= n - 4)
					{
						a++; // up to index n-3
						b = a + 1; // new set
						continue;
					}

					a = 1;
					b = 2;
					fourMode = true;
				}
				else
				{
					//cout << "Fail : a" << a << "b" << b << endl; // for debugging
					// fix as  bs cs ds    ae  be  ce  de  fix
					// 0   1   2  3  4 ... n-5 n-4 n-3 n-2 n-1
					if (d <= n - 3)
					{
						d++; // up to index n-2
						continue;
					}

					if (c <= n - 4)
					{
						c++; // up to index n-3
						d = c + 1; // new set
						continue;
					}

					if (b <= n - 5)
					{
						b++; // up to index n-4
						c = b + 1; // new set
						d = b + 2; // new set
						continue;
					}

					if (a <= n - 6)
					{
						a++; // up to index n-5
						b = a + 1; // new set
						c = a + 2; // new set
						d = a + 3; // new set
						continue;
					}
					
					break;
				}
			}

			k++;
			if (k == BASE_CNT)
			{
				k = 0;
				cout << '1'; // pi == 0
				for (int pi = 1; pi <= n - 2; ++pi)
				{
					if (fourMode == false)
					{
						if ((pi == n - 1 - a) || (pi == n - 1 - b))
						{
							cout << '1';
						}
						else
						{
							cout << '0';
						}
					}
					else
					{
						if ((pi == n - 1 - a) || (pi == n - 1 - b) || (pi == n - 1 - c) || (pi == n - 1 - d))
						{
							cout << '1';
						}
						else
						{
							cout << '0';
						}
					}
				}
				cout << '1'; // pi == n - 1
				for (int pd = 0; pd < BASE_CNT; ++pd)
				{
					cout << ' ' << divider[pd];
				}
				cout << endl;

				cnt++;

				if (cnt == j)
				{
					break;
				}

				// counting and next
				if (fourMode == false)
				{
					if (b <= n - 3)
					{
						b++; // up to index n-2
						continue;
					}

					if (a <= n - 4)
					{
						a++; // up to index n-3
						b = a + 1; // new set
						continue;
					}

					a = 1;
					b = 2;
					fourMode = true;
				}
				else
				{
					if (d <= n - 3)
					{
						d++; // up to index n-2
						continue;
					}

					if (c <= n - 4)
					{
						c++; // up to index n-3
						d = c + 1; // new set
						continue;
					}

					if (b <= n - 5)
					{
						b++; // up to index n-4
						c = b + 1; // new set
						d = b + 2; // new set
						continue;
					}

					if (a <= n - 6)
					{
						a++; // up to index n-5
						b = a + 1; // new set
						c = a + 2; // new set
						d = a + 3; // new set
						continue;
					}

					break;
				}

			}

		}


		if (cnt != j)
		{
			cout << "Not Found Any More!! " << cnt << " Found!! " << endl;
		}
	}

	//char sample[33] = "10000000000000000000000000000000";
	//StrInt a(sample, 32);
	//a.Divide(200000001);
	//a.Print();
	

	return 0;
}