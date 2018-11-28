#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <iomanip>
#define unsigned int uint
#define ff first
#define ss second
using namespace std;


int main() {
        cin.sync_with_stdio(0);
	int t,x,ans,row,count;
	bool first;
	cin >> t;
	for (int f=0; f<t; f++) {
		bool arr[16]={false};
		ans=0; first=false; count=0; 
		cin >> row;
		for (int i=0; i<4; i++) for (int j=0; j<4; j++) {
			cin >> x;
			if (i+1==row) arr[x-1]=true;}
		cin >> row;
		for (int i=0; i<4; i++) for (int j=0; j<4; j++) {
			cin >> x;
			if (i+1==row && arr[x-1]) {if (!first) {first=true; ans=x;} count++;}}

		if (count==1)  cout << "Case #" << f+1 << ": " << ans << endl;
		else if (count>1)  cout << "Case #" << f+1 << ": Bad magician!" << endl;
		else cout << "Case #" << f+1 << ": Volunteer cheated!" << endl;}	
        return 0;}  
