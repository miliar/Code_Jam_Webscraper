#include <iomanip>
#include <algorithm>
#include <iterator>     // std::insert_iterator
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>

using namespace std;
ifstream in("A.in");
ofstream out("result.txt");
#define INF 1e16
string num2str(long long i) { stringstream ss; ss << i; return ss.str(); }
long long str2num(string s) { long long num; stringstream ss(s); ss >> num; return num; }

long long reverse(long long num){
	string t = num2str(num);
	reverse(t.begin(), t.end());
	long long ret = str2num(t);
	return ret;
}

//map<long long, long long> cache;

struct Node{
	long long step, num;
	bool operator<(const Node& a) const{ return a.step < step; }
	Node(long long s, long long n) : step(s), num(n){}
};

void Solve(){
	long long N;
	in >> N;

	priority_queue< Node, vector< Node >, less< Node > > pq;
	pq.push(Node(1, 1));
	set<long long> visited;
	while (!pq.empty()){
		Node cur = pq.top(); pq.pop();
		if (cur.num == N){
			out << cur.step << endl;
			cout << cur.step << endl;
			return;
		}
		//		cache[cur.num] = cur.step;
		if (visited.find(cur.num + 1) == visited.end()){
			Node nxt = cur;
			nxt.step = cur.step + 1; nxt.num = cur.num + 1;
			pq.push(nxt);
			visited.insert(nxt.num);
		}
		long long r = reverse(cur.num);
		if (visited.find(r) == visited.end()){
			Node nxt = cur;
			nxt.step = cur.step + 1; nxt.num = r; 
			pq.push(nxt);
			visited.insert(nxt.num);
		}
	}
	out << -1 << endl;
	cout << -1 << endl;
	return;
}

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	in >> T;
	for (int test = 0; test < T; test++){
		cout << "Case #" << test + 1 << ": ";
		out << "Case #" << test + 1 << ": ";
		Solve();
	}
	return 0;
}
