#include <iostream>
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <set>
#include <list>
#include <string>
#include <algorithm>
#include <map>
#include <cmath>
#include <stack>
#include <functional>
#include <math.h>
#include <queue>
#include <vector>
#include <bitset>
#include <cstdio>
#pragma comment(linker, "/STACK:2048000000000000")
typedef long long ll;
#define eps 1e-10
#define MP make_pair
 
using namespace std;

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int t,a[7][7],r;
	vector<int> vec1,vec2;
	set<int> ans;
	cin>>t;
	for(int ii=1;ii<=t;ii++){
		cin>>r;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin>>a[i][j];
				if (i==r)
					vec1.push_back(a[i][j]);
			}
		}
		sort(vec1.begin(),vec1.end());
		cin>>r;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin>>a[i][j];
				if (i==r)
					vec2.push_back(a[i][j]);
			}
		}
		sort(vec2.begin(),vec2.end());
		for(int i=0;i<vec1.size();i++){
			for(int j=0;j<vec2.size();j++){
				if (vec1[i]==vec2[j]){
					ans.insert(vec1[i]);
				}
			}
		}
		cout<<"Case #"<<ii<<": ";
		if (ans.size()==0){
			puts("Volunteer cheated!");
		}
		if (ans.size()==1){
			cout<<*ans.begin()<<endl;
		}
		if (ans.size()>1){
			puts("Bad magician!");
		}
		vec1.clear();
		vec2.clear();
		ans.clear();
	}
}