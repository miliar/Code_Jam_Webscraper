#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	int T;
	int arr_1[4][4],arr_2[4][4];
	int A1,A2;
	vector<int> vec;
	cin>>T;
	for(int i=0;i<T;i++){
		cin>>A1;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>arr_1[j][k];
		cin>>A2;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>arr_2[j][k];
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(arr_1[A1-1][j]==arr_2[A2-1][k])
					vec.push_back(arr_2[A2-1][k]);
			}
		}
		if(vec.size()==0)cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
		else if(vec.size()>1)cout<<"Case #"<<i+1<<": Bad magician!\n";
		else cout<<"Case #"<<i+1<<": "<<vec[0]<<"\n";
		vec.clear();
	}
}