#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <queue>

#define SZ 1000000
#define pb push_back
using namespace std;


char Invert(char c)
{
	if(c=='+') return '-';
	return '+';
}

string Flip(string cur,int pos)
{
	int l = 0;
	int r = pos;
	while(l<=r) {
		swap(cur[l],cur[r]);
		cur[l] = Invert(cur[l]);
		if(l!=r)	cur[r] = Invert(cur[r]);
		l++;
		r--;
	}
	return cur;

}


int Bfs(string start)
{
	map<string,int> D;
	D[start] = 1;
	string end  = start;
	for(int i=0;i<end.size();i++) end[i] = '+';

	queue<string> Q;
	Q.push(start);
	while(!Q.empty()) {
		string cur = Q.front();
		Q.pop();
		if(cur==end) return D[cur]-1;
		for(int i=0;i<cur.size();i++) {
			string next = Flip(cur,i);
			//cout<<cur<<" "<<next<<endl;
			if(D[next] == 0) D[next] = D[cur] + 1 , Q.push(next);
		}

	}
	return -1;

}

int main()
{
	freopen("B.txt","rt",stdin);
	freopen("Bout.txt","wt",stdout);
	int tst,cas;
	scanf("%d",&tst);
	for(cas=1;cas<=tst;cas++) {
		string L;
		cin>>L;
		printf("Case #%d: %d\n",cas,Bfs(L));
	}

	return 0;
}