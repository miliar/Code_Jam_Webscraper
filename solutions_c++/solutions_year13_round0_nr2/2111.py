#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;


int main(){
	int t;
	scanf("%d",&t);
	for(int tst=1;tst<=t;tst++){
		int n,m;
		scanf("%d%d",&n,&m);
			
		vector<vector<int> > v;

		for(int i=0;i<n;i++){
			vector<int> temp;
			for(int j=0;j<m;j++){
				int x;
				scanf("%d",&x);
				temp.push_back(x);
			}
			v.push_back(temp);
		}

		vector<int> mr;
		for(int i=0;i<v.size();i++){
			int max=0;
			for(int j=0;j<v[i].size();j++){
				if(v[i][j]>max)
					max=v[i][j];
			}
			mr.push_back(max);
		}

		vector<int> mc;

		for(int j=0;j<m;j++){
			int max=0;
			for(int i=0;i<n;i++){
				if(v[i][j]>max)
					max=v[i][j];
			}
			mc.push_back(max);
		}

		vector<vector<int> > v2;

		for(int i=0;i<n;i++){
			vector<int> temp;
			for(int j=0;j<m;j++){
				temp.push_back(100);
			}
			v2.push_back(temp);
		}

		for(int i=0;i<mr.size();i++){
			for(int j=0;j<v2[i].size();j++){
				v2[i][j]=mr[i];
			}
		}

		for(int j=0;j<mc.size();j++){
			for(int i=0;i<n;i++){
				if(v2[i][j]>=mc[j])
					v2[i][j]=mc[j];
			}
		}

		int count=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(v[i][j] == v2[i][j])
					count++;
			}
		}


		/*for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cout<<v2[i][j]<<" ";
			}
			cout<<endl;
		}*/

		if(count == (n*m))
			cout<<"Case #"<<tst<<": YES"<<endl;
		else
			cout<<"Case #"<<tst<<": NO"<<endl;
	}
	return 0;
}