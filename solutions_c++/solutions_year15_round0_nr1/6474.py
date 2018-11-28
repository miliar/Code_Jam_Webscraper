#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>
#include <climits>
#include <bitset>

using namespace std;

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;

#define INF 1e9
#define EPS 1e-9
#define PI acos(-1.0)
#define MOD 1234567

int T, S, arr[1010], sum[1010], caseNo = 1;
string str;

int main() {		
	// open files
	//freopen("homework.txt","r",stdin);
    //freopen("output.txt","w",stdout);	

	ofstream fout ("A_out.txt");
    ifstream fin ("A-large.in");
	
	fin >> T;
	while(T--) {
		fin >> S;
		++S;
		fin >> str;
		for(int i = 0; i < S; i++) {
			arr[i] = (str[i] - '0');
			sum[i] = (!i) ? arr[i] : (sum[i - 1] + arr[i]);
		}
		int cnt = 0;
		for(int i = 1; i < S; i++)
			if(sum[i - 1] + cnt < i) cnt += (i - sum[i - 1] - cnt);
		fout << "Case #" << (caseNo++) << ": " << cnt << endl;
	}

	
	//system ("pause");
	return 0;	
}