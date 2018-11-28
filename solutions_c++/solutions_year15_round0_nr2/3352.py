#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
	int csmax;
	cin >> csmax;
	for (int csnum = 1; csnum <= csmax; csnum++){
		int ndiners;
		cin >> ndiners;
		std::priority_queue<int> diner;
		{
			int cdiners = 0;
			while (cdiners != ndiners){
				int n;
				cin >> n;
				diner.push(n);
				cdiners += 1;
			}
		}
		//algo//
		int tpenelty = 0;
		int mintime = diner.top();
		while (tpenelty <= diner.top()){ //unoptimized halt condition
			int top = diner.top();
			diner.pop();
			diner.push(top / 2);
			diner.push(top - (top / 2));
			tpenelty++;
			mintime = std::min(mintime, tpenelty + diner.top());
		}

	output:
		cout << "Case #" << csnum << ": " << mintime << endl;
	}
	getchar(); getchar();
	return 0;
}
