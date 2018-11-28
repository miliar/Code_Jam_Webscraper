
#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

#define loop(_i, _n) for( _i = 0; _i < _n; _i++)
#define loopi(_i, _n, _s) for( _i = _s; _i < _n; _i++)
void solve();

int main(int argc, char* argv[]) {
	freopen("C:\\Users\\Beauty\\Downloads\\A-large.in", "r", stdin);
	freopen("out0.txt", "w", stdout);

	int num_case, t;
	cin >> num_case; num_case++;

	loopi(t, num_case, 1) {
		cout << "Case #" << t << ": ";
		solve();
	}

	return 1;
}

struct point
{
	long idx, val;
	bool operator<(const point& v)
	{
		//if (v.val != val)
		return v.val < val;
		//return v.idx > idx;
	}
};
static point part[26];


void solve()
{
	int i, j, n;
	long v, mx = -1;
	unsigned long long cnt = 0;
	string s;

	cin >> n;
	loop(i, n)
	{
		cin >> v;
		part[i] = { i, v };
		cnt += v;
		if (v > mx)
			mx = v;
	}

	s = "";
	int p = 0;
	sort(part, part + n);
	mx = part[0].val;
	int l = -1, lmx = -1;

	while (cnt > 0)
	{
		int o = 0;
		int b = 0;
		
		loop(i, n)
		{
			if (part[i].val == mx)
			{
				o = 0;
				loop(j, n)
					if (part[j].val)
						o++;
				p++;
				s += part[i].idx + 'A';
				cnt--;
				part[i].val--;
	
				sort(part, part + n);
				mx = part[0].val;


				if (o == 3 && cnt <= o && mx == 1)
				{
					//s += p > 1 ? " " : "";
					p = 2;
				}

				
				break;
			}
		}

		if (p > 1)
		{
			s += " ";
			p = 0;
		}
	}

	cout << s;
	cout << endl;
}