#include <bits/stdc++.h>
#include<vector>
#include<fstream>
using namespace std;
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.in","w",stdout); 
	int test,n,x;
	vector<int>row,copy,square;
	cin>>test;
	for(int i=0;i<test;i++){
		cin>>n;
			for(int j=0;j<16;j++){
				cin>>x;
				square.push_back(x);			
			}
		for(int o=0;o<4;o++){
			row.push_back(square[(4*(n-1) + o)]);
		}
		square.clear();
		cin>>n;
			for(int j=0;j<16;j++){
				cin>>x;
				square.push_back(x);			
			}
		for(int o=0;o<4;o++){
			copy.push_back(square[(4*(n-1) + o)]);
		}
		square.clear();
		for(int c=0;c<4;c++){
			for(int r=0;r<4;r++){
				if(copy[c]==row[r]){
					square.push_back(copy[c]);
				}
			}
		}
		if(square.size()==1)cout<<"Case #"<<i+1<<": "<<square[0]<<endl;
		else if(square.size()>1)cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		else cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		square.clear();
		copy.clear();
		row.clear();
	}	
	return 0;
}
