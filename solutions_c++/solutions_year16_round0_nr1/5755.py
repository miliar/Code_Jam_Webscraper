#define _CRT_SECURE_NO_WARNINGS
#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <hash_map>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>

#define PI 3.14159265359
#define all(v) v.begin(),v.end()
#define sortva(v) sort(all(v))
#define sortvd(v) sort(v.rbegin(),v.rend())
#define sortaa(a,n) sort(a,a+n)
#define sortad(a,n) sort(a,a+n),reverse(a,a+n)
#define sfi1(v) scanf("%d",&v)
#define sfi2(v1,v2) scanf("%d %d",&v1,&v2)
#define sfi3(v1,v2,v3) scanf("%d %d %d",&v1,&v2,&v3)
#define sfll1(v) scanf("%I64d",&v);
#define sfll2(v1,v2) scanf("%I64d %I64d",&v1,&v2)
#define sfll3(v1,v2,v3) scanf("%I64d %I64d %I64d",&v1,&v2,&v3)
#define pfi1(v) printf("%d ",v)
#define pfi2(v1,v2) printf("%d %d ",v1,v2)
#define pfi3(v1,v2,v3) printf("%d %d %d ",v1,v2,v3)
#define pfll1(v) printf("%I64d ",v)
#define pfll2(v1,v2) printf("%I64d %I64d ",v1,v2)
#define pfll3(v1,v2,v3) printf("%I64d %I64d %I64d ",v1,v2,v3)
#define ndl puts("")
typedef long long ll;
using namespace std;
void openfile() {
	cout << fixed << setprecision(15);
	#ifndef ONLINE_JUDGE 
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
}


int main() {
	openfile();

	int t, n;
	sfi1(t);
	for (int T = 1; T <= t; T++) {
		sfi1(n);
		printf("Case #%d: ", T);
		if (!n)
			printf("INSOMNIA\n");
		else {
			set<int> st;
			stringstream ss;
			ss << n;
			string s;
			ss >> s;
			for (int i = 0; i < s.size(); i++)
				st.insert(s[i] - '0');
			int num;
			for (int i = 2; i < 1000 && st.size() != 10; i++) {
				num = i * n;
				stringstream ss;
				ss << num;
				string s;
				ss >> s;
				for (int i = 0; i < s.size(); i++)
					st.insert(s[i] - '0');
			}
			printf("%d\n", num);
		}
	}
	
	
	
	return 0;
}