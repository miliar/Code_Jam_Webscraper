#include <iostream>
#include <map>
using namespace std;
#define N 4
int main() {
	int test=0;
	int test_case=1;
	cin>>test;
	
	while(test--){
		int row=0,new_row=0; 
		int found_count=0;
		int result=0;
		map<int,int> mymap;
		map<int,int>:: iterator it;
		int first[N][N]={0};
		int second[N][N]={0};
		
		cin>>row;
		
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				cin>>first[i][j];
			}
		}
		for(int i=0;i<N;i++){
			mymap.insert(pair<int,int>(first[row-1][i],1));
		}
		
		cin>>new_row;
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				cin>>second[i][j];
			}
		}
		for(int i=0;i<N;i++){
			it=mymap.find(second[new_row-1][i]);
			if(it!=mymap.end()){
				found_count++;
				if(1==found_count){
				result=it->first;
				}
			}
		}
		switch(found_count){
			case 0:{
				cout<<"Case #"<<test_case<<": "<<"Volunteer cheated!"<<endl;
				break;
			}
			case 1:{
				cout<<"Case #"<<test_case<<": "<<result<<endl;
				break;
			}
			default:{
				cout<<"Case #"<<test_case<<": "<<"Bad magician!"<<endl;
				break;
			}
		}
		test_case++;
	}
	return 0;
}