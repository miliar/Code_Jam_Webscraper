#include <bits/stdc++.h>
using namespace std;
#define all(c) (c).begin(), (c).end()
#define cnt(c, x) ((c).find(x) != (c).end())
#define pb push_back
#define FOR(i, a, n) for(int i = (a); i < (n); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int) (x).size())
#define mp(x,y) make_pair((x), (y))
#define mp3(x,y,z) make_pair((x), make_pair( (y), (z)))
#define foreach(C, i) for(auto i = (C).begin(); i != (C).end(); i++)
#define xx first
#define yy second
#define clr clear()
#define var(x) cout<< #x << " = "<<x<<"\n";
#define print(x) for_each((x).begin(), (x).end(), [](auto n) { cout<<x<<" " })
typedef int32_t i3;
typedef int64_t i6;
typedef vector<i3> vi;
typedef pair<i3,i3> ii;
typedef vector<pair<i3,i3> > vii;

vector<string> numbers;
vector<vector<i6> > factors;
int main()
{
	numbers.pb("1000000000000001");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 7, });
	numbers.pb("1000000000000101");
	factors.pb({13, 11, 3, 4751, 173, 3, 53, 109, 3, });
	numbers.pb("1000000000000111");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 11, });
	numbers.pb("1000000000001001");
	factors.pb({73, 5, 3, 19, 19, 3, 5, 19, 3, });
	numbers.pb("1000000000001101");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 11, });
	numbers.pb("1000000000010011");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 7, });
	numbers.pb("1000000000011001");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 11, });
	numbers.pb("1000000000011011");
	factors.pb({5, 1567, 15559, 6197, 5, 5, 1031, 7, 83, });
	numbers.pb("1000000000011111");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000000100101");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 7, });
	numbers.pb("1000000000101011");
	factors.pb({3, 7, 13, 3, 5, 43, 3, 73, 7, });
	numbers.pb("1000000000101111");
	factors.pb({5, 2, 3, 2, 37, 2, 5, 2, 3, });
	numbers.pb("1000000000110001");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 11, });
	numbers.pb("1000000000110101");
	factors.pb({23, 17, 11, 23, 5, 299699, 43, 239, 59, });
	numbers.pb("1000000000110111");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000000111011");
	factors.pb({17, 2, 3, 2, 73, 2, 17, 2, 3, });
	numbers.pb("1000000000111101");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000001000011");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 11, });
	numbers.pb("1000000001001001");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 7, });
	numbers.pb("1000000001001111");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000001010101");
	factors.pb({3, 7, 13, 3, 5, 17, 3, 53, 7, });
	numbers.pb("1000000001010111");
	factors.pb({5, 2, 3, 2, 37, 2, 5, 2, 3, });
	numbers.pb("1000000001011001");
	factors.pb({11, 5, 281, 101, 5, 67, 5, 13, 19, });
	numbers.pb("1000000001011011");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000001011101");
	factors.pb({17, 2, 3, 2, 1297, 2, 11, 2, 3, });
	numbers.pb("1000000001011111");
	factors.pb({59, 113, 7, 157, 19, 1399, 7, 43, 107, });
	numbers.pb("1000000001100001");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 11, });
	numbers.pb("1000000001100011");
	factors.pb({23, 19, 11, 105491, 5, 47, 11117, 1787, 127, });
	numbers.pb("1000000001100111");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000001101011");
	factors.pb({5, 2, 3, 2, 37, 2, 5, 2, 3, });
	numbers.pb("1000000001101101");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000001110011");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000001110101");
	factors.pb({5, 2, 3, 2, 37, 2, 5, 2, 3, });
	numbers.pb("1000000001111001");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000001111011");
	factors.pb({31, 557, 7, 19, 23, 1129, 7, 5441, 241, });
	numbers.pb("1000000001111101");
	factors.pb({7, 19, 43, 17, 55987, 23, 7, 7, 31, });
	numbers.pb("1000000001111111");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 7, });
	numbers.pb("1000000010000011");
	factors.pb({167, 2, 11, 2, 58427, 2, 23, 2, 839, });
	numbers.pb("1000000010000101");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 11, });
	numbers.pb("1000000010001001");
	factors.pb({5, 2, 7, 2, 1933, 2, 29, 2, 157, });
	numbers.pb("1000000010010001");
	factors.pb({3, 2, 5, 2, 7, 2, 3, 2, 7, });
	numbers.pb("1000000010010111");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000010011001");
	factors.pb({7, 1667, 179, 13, 5, 11, 23, 7, 311, });
	numbers.pb("1000000010011011");
	factors.pb({11, 2, 3, 2, 13, 2, 47, 2, 3, });
	numbers.pb("1000000010011101");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	numbers.pb("1000000010100011");
	factors.pb({3, 1259, 421, 3, 5, 8893, 3, 67, 17, });
	numbers.pb("1000000010100111");
	factors.pb({5, 2, 3, 2, 37, 2, 5, 2, 3, });
	numbers.pb("1000000010101001");
	factors.pb({3, 5, 13, 3, 5, 43, 3, 73, 7, });
	numbers.pb("1000000010110011");
	factors.pb({47, 2, 3, 2, 11, 2, 204311, 2, 3, });
	numbers.pb("1000000010110101");
	factors.pb({3, 2, 3, 2, 7, 2, 3, 2, 3, });
	int n,k;
	cin>>n>>k;
	cout<<"Case #1: \n";
	for(int i = 0; i < SZ(numbers); i++)
	{
		cout<<numbers[i]<<" ";
		for(int j = 0; j < SZ(factors[i]); j++)
			cout<<factors[i][j]<<" ";
		cout<<"\n";
	}
	return (0);
}
