#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#define FOR(i,j,k) for(int i=j;i<=k;i++)
using namespace std;
deque<char> q;
int main (int argc, char *argv[])
{
	std::ios::sync_with_stdio(false);
	int noc;cin>>noc;
	FOR(cs,1,noc){
		string k;cin>>k;
		int n=k.size();
		q.push_back(k[0]);
		FOR(i,1,n-1){
			if (k[i]>=q.front())	q.push_front(k[i]);
			else q.push_back(k[i]);
		}
		cout<<"Case #"<<cs<<": ";
		FOR(i,1,n){
			cout<<q.front();q.pop_front();
		}cout<<endl;
	}
	return 0;
}
