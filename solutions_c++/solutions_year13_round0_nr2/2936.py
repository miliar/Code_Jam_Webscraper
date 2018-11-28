#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
  int T;
  long N,M;
  long temp,i,j,k;
  int flag;
  int A[100][100];
  int row[100];
  int column[100];
  cin >> T;
  for(i=0;i<T;i++){
	cin >> N;
	cin >> M;
	flag =0;
	for(j=0;j<100;j++){
		 for(k=0;k<100;k++){
			A[j][k]=0;
		}
		row[j]=0;
		column[j]=0;
	}
	for(j=0;j<N;j++){
		 for(k=0;k<M;k++){
			cin >> temp;
			A[j][k]=temp;
		}
	}
	for(j=0;j<N;j++){
		 for(k=0;k<M;k++){
			if(A[j][k] > row[j]){
				row[j] = A[j][k];
			}
			if(A[j][k] > column[k]){
				column[k] = A[j][k];
			}
		}
	}
	for(j=0;j<N;j++){
		 for(k=0;k<M;k++){
			if(A[j][k] < row[j] && A[j][k] < column[k]){
				flag=1;
			}
		}
	}	
	if(flag ==1){
	    cout << "Case #" << i+1 << ": NO" << endl;
	}
	if(flag ==0){
	    cout << "Case #" << i+1 << ": YES" << endl;
	}
  }
  return 0;
}
