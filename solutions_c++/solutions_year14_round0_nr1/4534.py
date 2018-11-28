#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <set>
#include <cstring>
#include <cassert>

#define F(i, a,b) for(int i=int(a);i<int(b);i++)
#define foreach(it, l) for (typeof(l.begin()) it = l.begin(); it != l.end(); it++)
#define DBG(a) cout<<__LINE__<<": "<<#a<<"= "<<a<<endl;

#define L long long
using namespace std;

int t, caseNumber;
void resolve() {
	int n, m, aux;
	scanf("%d", &n);
	vector<int> v(4,0);
	vector<int> vv(4,0);
	F(i,0,4) {
		if(n - 1 == i)  scanf("%d%d%d%d", &v[0], &v[1], &v[2], &v[3]);
		else scanf("%d%d%d%d", &aux, &aux, &aux, &aux);
	}
	scanf("%d", &m);
	F(i,0,4) {
		if(m - 1 == i)  scanf("%d%d%d%d", &vv[0], &vv[1], &vv[2], &vv[3]);
		else scanf("%d%d%d%d", &aux, &aux, &aux, &aux);
	}
	int found = 0, res = 0;
	F(i,0,4)
	F(j,0,4)
	if(v[i] == vv[j]){ found++; res = v[i]; }

 	if(found == 1)  printf("Case #%d: %d\n",caseNumber++, res);
 	if(found > 1) printf("Case #%d: Bad magician!\n", caseNumber++);
 	if(found == 0) printf("Case #%d: Volunteer cheated!\n", caseNumber++);
}

int main() {
	scanf("%d", &t);
	caseNumber = 1;
	F(i,0,t) {
		resolve();
	}
}