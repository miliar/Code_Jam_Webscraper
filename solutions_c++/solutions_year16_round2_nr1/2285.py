
#include<iostream>
#include<cstdio>
#include<set>
#include<cstdlib>
#include<vector>
#include<algorithm>

using namespace std;

#define FOR(x,N) for(int x = 0 ; x < (N) ; x++ )
#define FOR1(x,N) for(int x = 1 ; x <= (N) ; x++ )


int main()
{
	long long T;
	char buf[1000000];
		freopen("in2.in", "rt", stdin);
		freopen("out2.out", "wt", stdout);
	//	freopen("in.txt", "rt", stdin);
	//	freopen("out.txt", "wt", stdout);
		cin >> T;

		char a;
		int k;
		int e=0, f=0, g=0, h=0, i=0, n=0, o=0, t=0, u=0, r=0, w=0, z=0, v=0, s=0, x = 0;
		string ret;
		int num[10];
		FOR(m, T){
			cin >> buf;
			a = buf[0];
			k = 0;
			e = 0, f = 0, g = 0, h = 0, i = 0, n = 0, o = 0, t = 0, u = 0, r = 0, w = 0, z = 0, v = 0, s = 0, x = 0;
			ret.clear();
				while (a != '\0')
				{
					if (a == 'E')
						e++;
					if (a == 'F')
						f++;
					if (a == 'G')
						g++;
					if (a == 'H')
						h++;
					if (a == 'I')
						i++;
					if (a == 'N')
						n++;
					if (a == 'O')
						o++;
					if (a == 'T')
						t++;
					if (a == 'U')
						u++;
					if (a == 'R')
						r++;
					if (a == 'W')
						w++;
					if (a == 'Z')
						z++;
					if (a == 'V')
						v++;
					if (a == 'S')
						s++;
					if (a == 'X')
						x++;

					k++;
					a = buf[k];					
				}

				num[0] = z;
				e -= z;
				r -= z;
				o -= z;

				num[2] = w;
				t -= w;
				o -= w;

				num[4] = u;
				f -= u;
				o -= u;
				r -= u;

				num[5] = f;
				i -= f;
				v -= f;
				e -= f;

				num[6] = x;
				s -= x;
				i -= x;

				num[7] = v;
				e -= (2 * v);
				s -= v;
				n -= v;

				num[8] = g;
				e -= g;
				i -= g;
				h -= g;
				t -= g;

				num[9] = i;
				n -= 2 * i;
				e -= i;

				num[3] = t;
				h -= t;
				r -= t;
				e -= 2 * t;

				num[1] = o;
				n -= o;
				e -= o;

				FOR(it, num[0])
				{
					ret = ret + "0";
				}
				FOR(it, num[1])
				{
					ret = ret + "1";
				}
				FOR(it, num[2])
				{
					ret = ret + "2";
				}
				FOR(it, num[3])
				{
					ret = ret + "3";
				}
				FOR(it, num[4])
				{
					ret = ret + "4";
				}
				FOR(it, num[5])
				{
					ret = ret + "5";
				}
				FOR(it, num[6])
				{
					ret = ret + "6";
				}
				FOR(it, num[7])
				{
					ret = ret + "7";
				}
				FOR(it, num[8])
				{
					ret = ret + "8";
				}				
				FOR(it, num[9])
				{
					ret = ret + "9";
				}
				cout << "Case #" << m + 1 << ": " << ret.c_str() << endl;
		}




	return 0;
}

