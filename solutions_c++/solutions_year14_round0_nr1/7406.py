#include <iostream>

using namespace std;

int main()
{
	int t;
	int hint1 = 0;
	int hint2 = 0;
	int cnt = 0;
	int cnt_case = 0;
	cin>>t;

	while(t--){		
		cnt_case++;
		int arr1[4][4] = {0};
		int arr2[4][4] = {0};
		int tmp;
		cnt = 0;
		
		cin>>hint1;
		for(int i = 0 ; i < 4 ; i++){
			for(int j = 0 ; j < 4 ; j++){
				cin>>arr1[i][j];
			}	
		}

		cin>>hint2;
		for(int i = 0 ; i < 4 ; i++){
			for(int j = 0 ; j < 4 ; j++){
				cin>>arr2[i][j];
			}	
		}

		for(int i = 0 ; i < 4 ; i++){
			for(int j = 0 ; j < 4 ; j++){
				if(arr1[hint1-1][i] == arr2[hint2-1][j]){
					tmp = arr1[hint1-1][i];
					cnt++;
				}
			}
		}
		if(cnt == 1){
			printf("Case #%d: %d\n",cnt_case,tmp);
		}else if(cnt==0){
			printf("Case #%d: Volunteer cheated!\n",cnt_case);
		}else{
			printf("Case #%d: Bad magician!\n",cnt_case);
		}
	}
	return 0;
}
