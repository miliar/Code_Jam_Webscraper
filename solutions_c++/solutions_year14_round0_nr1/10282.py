#include <bits/stdc++.h>

using namespace std;

int main()
{
	int ara1[4][4];
	int ara2[4][4];
	int testCase;
	cin>>testCase;
	int row1, row2;
	for(int i = 1; i <= testCase ; i++){
		int match = 0;
		int ans = 0;
		cin>>row1;
		
		for(int j = 0 ; j < 4 ; j++){
			for(int k =0 ; k < 4 ; k++){
				cin>>ara1[j][k];
				
			}
		}
		cin>>row2;
		for(int j = 0 ; j < 4 ; j++){
			for(int k =0 ; k < 4 ; k++){
				cin>>ara2[j][k];
				
			}
		}
		
		for(int j =0 ; j < 4 ; j++){
		
			int num1 = ara1[row1-1][j];
			
			for(int k = 0 ; k < 4 ; k++){
				int num2 = ara2[row2-1][k];
				if(num1==num2) {
					match++;
					ans = num2;
				} 
			}
			
			if(match>1) break;
			
		}
		
		
		if(match==1) cout << "Case #"<<i<<": "<<ans<<endl;
		else if(match==0) cout << "Case #"<<i<<": Volunteer cheated!"<<endl;
		else if(match>1) cout << "Case #"<<i<<": Bad magician!"<<endl;
		
		
		
	}
	

	return 0;
}
