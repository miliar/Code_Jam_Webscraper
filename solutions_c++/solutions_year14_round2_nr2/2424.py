#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <algorithm>
#include <stack>
typedef long long LL;
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int ti = 1;ti<=t;ti++){
		int a,b,k;
		cin>>a>>b>>k;
		int count =0;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				if((i&j) < k) count++;
			}
		}
		cout<<"Case #"<<ti<<": "<<count<<endl;
	}
	return 0;
}