#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>
#include <exception>
#include <numeric>

using namespace std;

typedef long long lo;
typedef vector< vector<long long> > vvl;
typedef vector< long long> vl;
typedef pair<lo, lo> ll;
typedef vector< ll > vll;
typedef vector< vll > vvll;
typedef pair<long, pair<long, long>> lll;
typedef vector<lll> vlll;
typedef vector<vvl> vvvl;
typedef vector<set<long>> vs;

char buff[1100];

void solve(){
	deque<char> q;
	lo n=strlen(buff);
	q.push_back(buff[0]);
	for (lo i=1;i<n;i++)
		if (buff[i]>=q.front()) q.push_front(buff[i]);
		else q.push_back(buff[i]);
	
	while (!q.empty()){
		printf("%c", q.front());
		q.pop_front();
	}
	printf("\n");
}
int main() {
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	lo t, n;
	scanf("%I64d", &t);
	for (lo i=0;i<t;i++){
		scanf("%s", &buff);
		printf("Case #%I64d: ", i+1);
		solve();
	}
	return 0;
}