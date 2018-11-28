#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;
typedef long long LL;

void run(int Case)
{
	int count[17]={0};
	int r;
	vector<int> chosen;
	for(int k=0;k<2;k++){
		cin >> r;
		r--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				int v;
				cin >> v;
				if(i==r){
					count[v]++;
					if(count[v]==2){
						chosen.push_back(v);
					}
				}
			}
		}
	}
	cout << "Case #" << Case << ": ";
	if(chosen.size()==0){
		cout << "Volunteer cheated!";
	}
	else if(chosen.size()==1){
		cout << chosen[0];
	}
	else
	{
		cout << "Bad magician!";
	}
	cout << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		run(t);
	}
}
