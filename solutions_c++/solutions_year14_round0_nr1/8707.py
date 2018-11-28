#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
	int T,R1,R2;
	int i,j,k;
	
	vector<int> row1[4],row2[4],soln;
	
	
	cin >> T;
	for(k=0;k<T;k++){
		cout<< "Case #" << k+1 << ": ";
	
		cin >> R1;
		R1--;
		for(i=0;i<4;i++){
			row1[i].clear();
			for(j=0;j<4;j++){
				int tmp;
				cin>>tmp;
				row1[i].push_back(tmp);
			}
		}
		cin >> R2;
		for(i=0;i<4;i++){
			row2[i].clear();
			for(j=0;j<4;j++){
				int tmp;
				cin>>tmp;
				row2[i].push_back(tmp);
			}
		}
		R2--;
	
		sort(row1[R1].begin(), row1[R1].end());
		sort(row2[R2].begin(), row2[R2].end());
		
		soln.clear();
		set_intersection(row1[R1].begin(), row1[R1].end(), row2[R2].begin(), row2[R2].end(), back_inserter(soln));
		
		if(soln.size() == 0){
			cout<<"Volunteer cheated!\n";
		}
		else if(soln.size() == 1){
			cout<<soln[0] << "\n";
		}
		else{
			cout<<"Bad magician!\n";
		}
		
	
	}
}
	
		