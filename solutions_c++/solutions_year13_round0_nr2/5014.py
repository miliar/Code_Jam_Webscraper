
#include <iostream>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <list>

using namespace std;

int main(){
	int test;
	cin>>test;
	int C = 0;
	while(test--){
		C++;
		int n,m;
		cin>>n>>m;
		vector<vector<int> >v(n,vector<int> (m));
		vector<int>row(n);
		vector<int>col(m);
		for(int i = 0;i < n;i++){
			for(int j = 0;j < m;j++){
				cin>>v[i][j];
				if(v[i][j] == 2){
					row[i] = 2;
					col[j] = 2;
				}
			}
		}
		bool flag = 0;
		for(int i = 0;i < n;i++){
			for(int j = 0;j < m;j++){
				if(v[i][j] == 1){
					if(row[i] == 2 && col[j] == 2)
						flag = 1;
				}
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
