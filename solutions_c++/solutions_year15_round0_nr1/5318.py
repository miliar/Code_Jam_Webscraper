#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<unordered_map>
#include<queue>
#include<stack>
#include<iterator>
#include<cmath>
#include<string>
#include<sstream>
#include<cstring>
#include<ctype.h>
#include<iomanip>
#include<bitset>
#include<stdio.h>
#include<fstream>
#include<regex>
#include<stdlib.h>
#include<math.h>
#include<ctime>
using namespace std;

#define R_(s)         freopen(s, "r", stdin)
#define W_(s)        freopen(s, "w", stdout)
#define R_W R_("input.txt"),W_("output.txt")
#define PI 3.14159265358979323846
#define ll long long
#define DFS_GRAY  -1
#define DFS_WHITE  0
#define DFS_BLACK  1

using namespace std;
int main()
{
	R_W;
	int n; cin >> n;
	for (int i = 0; i < n; i++)
	{
		int sum = 0, invited = 0, Max; string s; cin >> Max >> s;
		sum += (int(s[0]) - 48);
		for (int j = 1; j < s.length(); j++)
		{
			if (sum < j/*&&s[j]!=0*/)
			{
				invited++; sum += (int(s[j]) - 48) + 1;
			}
			else
			if (sum >= j)
			{
				sum += (int(s[j]) - 48);
			}
			if (sum >= Max)break;
		}
		cout << "Case #"<<i+1<<": " << invited << endl;
	}
}
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