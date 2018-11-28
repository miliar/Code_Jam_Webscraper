#include <iostream>
#include <algorithm>

using namespace std;

int printIntersection(int arr1[], int arr2[], int m, int n)
{
	int i = 0, j = 0, flag = 0;
    while(i < m && j < n)
    {
      if(arr1[i] < arr2[j])
        i++;
      else if(arr2[j] < arr1[i])
        j++;
      else
      {
      	if(flag == 0){
      		flag = arr2[j++];
      	}else{
      		flag = -1;
      		break;
      	}
      }
    }
    
    if(flag == 0){
    	return 0;
    }else if(flag == -1){
    	return -1;
    }else{
    	return flag;
    }
}

int main()
{
	int t, r1, r2, i, j, flag, k;
	int mat1[4][4], mat2[4][4];
	int a1[4], a2[4];
	
	cin >> t;
	k = 1;
	while(t--)
	{
		flag = 0;
		cin >> r1;
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++){
				cin >> mat1[i][j];
			}
		}
		for(i = 0; i < 4; i++){
			a1[i] = mat1[r1-1][i];
		}
		
		cin >> r2;
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++){
				cin >> mat2[i][j];
			}
		}
		for(i = 0; i < 4; i++){
			a2[i] = mat2[r2-1][i];
		}
		
		sort(a1, a1+4);
		sort(a2, a2+4);
		flag = printIntersection(a1, a2, 4, 4);
		
		if(flag == 0){
			cout << "Case #" << k << ": " << "Volunteer cheated!" << endl;
		}else if(flag == -1){
			cout << "Case #" << k << ": " << "Bad magician!" << endl;
		}else{
			cout << "Case #" << k << ": " << flag << endl;
		}
		k++;
	}
	
	return 0;
}
