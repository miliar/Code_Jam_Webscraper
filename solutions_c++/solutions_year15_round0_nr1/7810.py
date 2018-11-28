#include <iostream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define For(i,a,b) for (int i(a); i < b; i++)
#define Ford(i,a,b) for (int i(a); i > b; i--)
#define Foreq(i,a,b) for (int i(a); i <= b; i++)
#define Fordeq(i,a,b) for (int i(a); i >= b; i--)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()


int f(string s, int max){
	int extra = 0, people = s[0] - '0';
	Foreq(i,1,max){
		//printf("people:%d , i:%d\n",people,i );
		if(people < i){
			extra += i - people;
			people = i + s[i] - '0';
		}

		else{
			people += s[i] - '0';
		}
	}

	return extra;
}

int main(int argc, char **argv){
	int T, max;
	cin >> T;
	string s;
	For(i,0,T){
		cin >>  max;
		cin >> s;
		printf("Case #%d: %d\n",i+1,f(s,max) );
	}
}


