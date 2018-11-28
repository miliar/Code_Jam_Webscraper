#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <functional>
#include <fstream>
#include <math.h>
using namespace std;
int main(){
	freopen("in.txt", "r", stdin);
	ofstream myfile;
	myfile.open("pancakes.txt");
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		int d;
		int mini = 2e19;
		scanf("%d", &d);
		int checks[4] = { 2, 3, 5, 7 };
		vector< priority_queue<int, vector<int>, less<int> > > q;
		priority_queue<int, vector<int>, less<int> > tmp;
		q.push_back(tmp);
		while (d--){
			int n;
			scanf("%d", &n);
			q[0].push(n);
		}
		mini = q[0].top();
		int removes = 0;
		while (!q.empty()){
			vector< priority_queue<int, vector<int>, less<int> > > qtmp;
			while (!q.empty()){
				priority_queue<int, vector<int>, less<int> > cur = q.back();
				q.pop_back();
				for (int x = 0; x < 4; x++){
					priority_queue<int, vector<int>, less<int> > pp(cur);
					int n = pp.top();
					mini = min(mini, n + removes);
					if (cur.top() >= checks[x]*2){
						int other = n / checks[x];
						n -= other;
						pp.pop();
						pp.push(n);
						pp.push(other);
						qtmp.push_back(pp);
					}
				}
			}
			q = qtmp;
			removes++;
		}
		cout << mini;
		myfile << "Case #" << i << ": " << mini << "\n";
	}
	myfile.close();
	return 0;
}
