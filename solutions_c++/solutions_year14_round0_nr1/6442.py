#include <iostream>
#include <string>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <list>
using namespace std;

#define ll long long
#define ull unsigned long long
#define INF 1e9

int main(){
	ios_base::sync_with_stdio(0);

	int t, a1,a2,m[4][4],r1[4],r2[4];
	cin>>t;
	for(int k=1;k<=t;k++){
		memset(m, 0, sizeof(m));
		memset(r1, 0, sizeof(r1));
		memset(r2, 0, sizeof(r2));
		cin>>a1;
		a1=a1-1;
		for(int i=0; i < 4; i++){
			for(int j=0; j<4;j++){
				cin>>m[i][j];
			}
		}
		for(int j=0; j<4;j++){
			r1[j]= m[a1][j];
		}
		cin>>a2;
		a2=a2-1;
		for(int i=0; i < 4; i++){
			for(int j=0; j<4;j++){
				cin>>m[i][j];
			}
		}
		for(int j=0; j<4;j++){
			r2[j]= m[a2][j];
		}
		vector<int> ans;
		for(int i=0; i < 4; i++){
			for(int j=0; j<4;j++){
				if(r1[i] == r2[j]){
					ans.push_back(r1[i]);
				}
			}
		}
		if(ans.size()==0){
			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		}else if(ans.size()==1){
			cout<<"Case #"<<k<<": "<<ans[0]<<endl;
		}else{
			cout<<"Case #"<<k<<": Bad magician!"<<endl;			
		}
	}

	return 0;
}
