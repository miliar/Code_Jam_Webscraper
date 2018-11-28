#define _CRT_SECURE_NO_WARNINGS
#include<algorithm>
#include<stdlib.h>
#include<iterator>
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstring>
#include<ctype.h>
#include<iomanip>
#include<stdio.h>
#include<fstream>
#include<vector>
#include<bitset>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<cmath>
#include<set>
#include<map>

using namespace std;

#define all(v)             v.begin(),v.end()
#define sz(v)            ((int)((v).size()))
#define psh(x)                  push_back(x)
#define sc(x)                 scanf("%d",&x)
#define sc2(x,y)         scanf("%d%d",&x,&y)
#define lop(i,n)        for(int i=0;i<n;i++)
#define loop(i,f,l)     for(int i=f;i<l;i++)
#define R_(s)         freopen(s, "r", stdin)
#define W_(s)        freopen(s, "w", stdout)
#define R_W R_("input.txt"),W_("output.txt")
#define INF                       1000000000
#define PI                 3.141592653589793
#define DFS_GRAY  -1
#define DFS_WHITE  0
#define DFS_BLACK  1

typedef string            ss;
typedef long long         ll;
typedef pair <int, int>   ii;
typedef pair<ss, int>     si;
typedef pair<int, ss>     is;
typedef pair<char, int>  chi;
typedef pair<ss, ss>     pss;
typedef vector<ii>       vii;
typedef vector<int>       vi;
typedef vector<vi>       vvi;
typedef vector<ss>        vs;
typedef vector<ll>       vll;
typedef vector<vll>     vvll;

ll pw(ll b, ll p){ if (!p) return 1; ll sq = pw(b, p / 2); sq *= sq; if (p % 2) sq *= b; return sq; }
ll sq(ll x){ lop(i, x)if ((ll)i*i > x) return (i - 1); return 1; }
ll gcd(ll a, ll b)  { return (b == 0 ? a : gcd(b, a % b)); }
ll sd(ll x)  { return x<10 ? x : x % 10 + sd(x / 10); }
ll lcm(ll a, ll b){ return ((a*b) / gcd(a, b)); }


int T, D, v, mx, cnt = 0;
vi  plates(10);

int solve(int i, vi vec)
{
	if (i == 1)return 1;
	int m = INF;
	for (int k = 1; k<i; k++)
	{
		vec[k] += vec[i];
		vec[i - k] += vec[i];
		for (int j = i - 1; j > 0; j--)
		{
			if (vec[j] > 0)
			{
				m = min(m, solve(j, vec));
				break;
			}
		}
		vec[k] -= vec[i];
		vec[i - k] -= vec[i];
	}
	int ret = min(m + vec[i], i);
	for (int j = 0; j < i; j++)
	{
		vec[j] = vec[j + 1];
	}
	for (int j = i - 1; j > 0; j--)
	{
		if (vec[j] > 0)
		{
			ret = min(ret, 1 + solve(j, vec));
			break;
		}
	}
	return ret;
}

int main()
{
	R_W;

	cin >> T;
	lop(i, T)
	{
		lop(i, 10)plates[i] = 0;
		mx = -1;
		cin >> D;
		lop(i, D)
		{
			cin >> v;
			++plates[v];
			mx = max(v, mx);
		}
		cout << "Case #" << ++cnt << ": " << solve(mx, plates) << endl;
	}
}




//#define _CRT_SECURE_NO_WARNINGS
//#include<iostream>
//#include<algorithm>
//#include<vector>
//#include<set>
//#include<map>
//#include<unordered_map>
//#include<queue>
//#include<stack>
//#include<iterator>
//#include<cmath>
//#include<string>
//#include<sstream>
//#include<cstring>
//#include<ctype.h>
//#include<iomanip>
//#include<bitset>
//#include<stdio.h>
//#include<fstream>
//#include<regex>
//#include<stdlib.h>
//#include<math.h>
//#include<ctime>
//using namespace std;
//#define R_(s)         freopen(s, "r", stdin)
//#define W_(s)        freopen(s, "w", stdout)
//#define R_W R_("input.txt"),W_("output.txt")
//#define PI 3.14159265358979323846
//#define ll long long
//#define DFS_GRAY  -1
//#define DFS_WHITE  0
//#define DFS_BLACK  1
//using namespace std;
//string a[4][4] = { "1", "i", "j", "k", "i", "-1", "k", "-j", "j", "-k", "-1", "i", "k", "j", "-i", "-1" };
//map<char, int>mp;
//string mul(string s1, char s2)
//{
//	string d;
//	d += s2;
//	if (s1 == "PP")return d;
//	string ans = a[mp[s1[s1.length() - 1]]][mp[s2]];
//	if (s1[0] != s2 && (s1[0] == '-'|| s2=='-'))
//	{
//		if (ans[0] != '-')ans = '-' + ans;
//		else ans.erase(0, 1);
//	}
//	return ans;
//}
//int main()
//{
//	R_W;
//	mp['1'] = 0; mp['i'] = 1; mp['j'] = 2; mp['k'] = 3;
//	int T; cin >> T;
//	for (int i = 0; i < T; i++)
//	{
//		int L, X; string s,S; cin >> L >> X >> s;
//		vector<int>I, J, K;
//		string ansI="PP", ansJ, ansK;
//		bool test = false; set<char>se;
//		for (int j = 0; j < L; j++)
//		{
//			se.insert(s[j]);
//		}
//		if (se.size() != 1)
//		{
//			for (int j = 0; j < X; j++)S += s;
//			for (int j = 0; j < S.length(); j++)
//			{
//				ansI = mul(ansI, S[j]); ansJ = "PP"; ansK = "PP";
//				if (ansI == "i")
//				{
//					for (int z = j + 1; z < S.length(); z++)
//					{
//						ansJ = mul(ansJ, S[z]);
//						if (ansJ == "j")
//						{
//							for (int u = z + 1; z < S.length(); u++)
//							{
//								ansK = mul(ansK, S[u]);
//								if (ansK == "k"){ test = true; break; }
//							}
//						}
//						if (test)break;
//					}
//				}
//				if (test)break;
//			}
//			if (test)cout << "Case #" << i + 1 << ": YES" << endl;
//			else cout << "Case #" << i + 1 << ": NO" << endl;
//		}
//		else
//			cout << "Case #" << i + 1 << ": NO" << endl;
//	}
//}
//void DFS(int visited[], vector<vector<int>>graph, int node)
//{
//	visited[node - 1] = 1;
//	cout << node << " ";
//	for (int i = 0; i < graph[node - 1].size(); i++)
//	{
//		int child = graph[node - 1][i];
//		if (!visited[child])DFS(visited, graph, child + 1);
//	}
//}
//int ConnectedComponenetsCnt(int visited[], vector<vector<int>>graph)
//{
//	int cnt = 0;
//	for (int i = 0; i < graph.size(); i++)
//	{
//		if (!visited[i])
//		{
//			cnt++;
//			DFS(visited, graph, i + 1);
//		}
//	}
//	return cnt;
//}



//atoll
/*stringstream ss;
ss << int name;
string string name = ss.str();*/

//bool comp(structname a, structname b)
//{
//  return a.struct1 < b.struct1; or > for desc. or struct2 to sort 3la 2
//}andeha fe al sort
//note//al rkm fe al string s[0]-48


//bitset<70> string name(int); by7wl int to string fe 70 mn alymen;

//int binaryToBase10(int n) {
//
//	int output = 0;
//
//	for (int i = 0; n > 0; i++) {
//
//		if (n % 10 == 1) {
//			output += pow(2, i);
//		}
//		n /= 10;
//	}
//
//	return output;
//}

//cout << fixed << setprecision(10) << almot8er; dh 3shan atl3 ad ah b3d al-3lama


/*void runEratosthenesSieve(int upperBound)
{
int upperBoundSquareRoot = (int)sqrt((double)upperBound);
bool *isComposite = new bool[upperBound + 1];
memset(isComposite, 0, sizeof(bool)* (upperBound + 1));
for (int m = 2; m <= upperBoundSquareRoot; m++)
{
if (!isComposite[m])
{
cout << m << " " << endl;
for (int k = m * m; k <= upperBound; k += m)
{
isComposite[k] = true;
}
}
}
for (int m = upperBoundSquareRoot; m <= upperBound; m++)
{
if (!isComposite[m])
{
cout << m << " " << endl;
}
}
delete[] isComposite;
}*/


//inline bool IsPrime(int number)
//{
//	if (((!(number & 1)) && number != 2) || (number < 2) || (number % 3 == 0 && number != 3))
//		return (false);
//
//	for (int k = 1; 36 * k*k - 12 * k < number; ++k)
//	if ((number % (6 * k + 1) == 0) || (number % (6 * k - 1) == 0))
//		return (false);
//	return true;
//}
/*stringstream ss;
ss << int name;
string string name = ss.str();*/


//bool comp(structname a, structname b)
//{
//  return a.struct1 < b.struct1; or > for desc. or struct2 to sort 3la 2
//}andeha fe al sort


//note//al rkm fe al string s[0]-48


//bitset<70> string name(int); by7wl int to string fe 70 mn alymen;

//int binaryToBase10(int n) {
//
//	int output = 0;
//
//	for (int i = 0; n > 0; i++) {
//
//		if (n % 10 == 1) {
//			output += pow(2, i);
//		}
//		n /= 10;
//	}
//
//	return output;
//}

//cout << fixed << setprecision(10) << almot8er; dh 3shan atl3 ad ah b3d al-3lama


/*void runEratosthenesSieve(int upperBound)
{
int upperBoundSquareRoot = (int)sqrt((double)upperBound);
bool *isComposite = new bool[upperBound + 1];
memset(isComposite, 0, sizeof(bool)* (upperBound + 1));
for (int m = 2; m <= upperBoundSquareRoot; m++)
{
if (!isComposite[m])
{
cout << m << " " << endl;
for (int k = m * m; k <= upperBound; k += m)
{
isComposite[k] = true;
}
}
}
for (int m = upperBoundSquareRoot; m <= upperBound; m++)
{
if (!isComposite[m])
{
cout << m << " " << endl;
}
}
delete[] isComposite;
}*/


//inline bool IsPrime(int number)
//{
//	if (((!(number & 1)) && number != 2) || (number < 2) || (number % 3 == 0 && number != 3))
//		return (false);
//
//	for (int k = 1; 36 * k*k - 12 * k < number; ++k)
//	if ((number % (6 * k + 1) == 0) || (number % (6 * k - 1) == 0))
//		return (false);
//	return true;
//}



//int n; cin >> n; int sum_elements[1007] = { 0 }; vector<int>v;
//for (int i = 0; i < n; i++)
//{
//	int D, Max = 0, stop = 0; cin >> D;
//	for (int j = 0; j < D; j++)
//	{
//		int a; cin >> a; if (a>Max)Max = a; sum_elements[a]++;
//	}
//	while (1)
//	{
//		if (sum_elements[Max] + Max / 2 >= Max){ v.push_back(stop + Max); break; }
//		else
//		{
//			v.push_back(stop + Max);
//			stop += sum_elements[Max];
//			if (Max % 2 == 0)
//			{
//				sum_elements[Max / 2] = sum_elements[Max] * 2;
//				sum_elements[Max] = 0;
//			}
//			else
//			{
//				sum_elements[Max / 2] = sum_elements[Max];
//				sum_elements[Max / 2 + 1] = sum_elements[Max];
//				sum_elements[Max] = 0;
//			}
//		}
//		Max = 0;
//		for (int j = 0; j < 1007; j++)
//		{
//			if (sum_elements[j] != 0 && Max < j)Max = j;
//		}
//	}
//	memset(sum_elements, 0, 1007);
//	sort(v.begin(), v.end());
//	cout << "Case #" << i + 1 << ": " << v[0] << endl;
//	v.clear();
//}