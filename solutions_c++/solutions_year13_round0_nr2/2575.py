//*****Template*****//
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <utility>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <numeric>
#include <iterator>
#include <functional>

#define INF 987654321
#define ll long long
#define rep0N(i,n) for(int i = 0;i < n;i++)
#define repN0(i,n) for(int i = n-1;i >= 0;i--)
#define repij(i,j,n) for(int i = j;j < n;i++)
#define pb(a) push_back(a)
#define si(a) scanf("%d",&a)
#define pi(a) printf("%d",a)

using namespace std;

int main(){
	int test;
	int C = 0;
	cin>>test;
	while(test--){
		C++;
		int n,m;
		cin>>n>>m;
		vector<vector<int> >v(n,vector<int> (m));
		vector<int>row(n);
		vector<int>col(m);
		for(int i = 0;i < n;i++){
			int max = 0;
			for(int j = 0;j < m;j++){
				cin>>v[i][j];
				if(v[i][j] > max)
					max = v[i][j];
			}
			row[i] = max;
		}
		for(int j = 0;j < m;j++){
			int max = 0;
			for(int i = 0;i < n;i++){
				if(v[i][j] > max)
					max = v[i][j];
			}
			col[j] = max;
		}
		bool flag = 0;
		for(int i = 0;i < n;i++){
			for(int j = 0;j < m;j++){
				if(v[i][j] < row[i] && v[i][j] < col[j])
					flag = 1;
				if(flag == 1)
					break;
			}
			if(flag == 1)
				break;
		}
		if(flag == 0)
			cout<<"Case #"<<C<<": YES"<<endl;
		else
			cout<<"Case #"<<C<<": NO"<<endl;
	}
	return 0;
}