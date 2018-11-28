#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t;
	int  k =1;
	scanf("%d",&t);
	while(t--){
		int r1 ;
		cin >> r1 ;
		int grid[5][5] ; 
		int arr1[20]={0},arr2[20]={0};
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin >> grid[i][j];
				if(i+1==r1)
				arr1[grid[i][j]]++;
			}
		}
		int r2;
		cin >> r2;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin >> grid[i][j];
				if(i+1==r2)
				arr2[grid[i][j]]++;
			}
		}
		/*
		for(int i=0;i<=16;i++)
		cout << arr1[i] << " " ;
		cout << endl;
		for(int i=0;i<=16;i++)
		cout << arr2[i] << " " ;
		cout << endl; 
		*/
		vector<int> ind;
		for(int i=0;i<=16;i++){
			if(arr1[i]==arr2[i]&& arr1[i]!=0){
				ind.push_back(i);
			}
    	}
    	if((int)ind.size()==0){
    		cout << "Case #" << k<< ": Volunteer cheated!" << endl;
    	}else if((int)ind.size()>1){
    		cout << "Case #"<< k << ": Bad magician!" << endl; 
    	}else{
    		cout << "Case #" << k << ": " << ind[0] << endl;
    	}
    	k++;
	}
	return 0;
	
}

