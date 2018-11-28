#include <iostream>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int i=0;i<T;i++){
    int Smax;
    cin >> Smax;
    int A[Smax+1];
    int standing[Smax+1];
    int friends = 0;
    fscanf(stdin,"%1d",&(A[0]));
    // cout << "A[0]: " << A[0] << endl;
    standing[0] = A[0];
    for(int j=1;j<Smax+1;j++){
      fscanf(stdin,"%1d",&A[j]);
      // cout << "A[" << j << "]: " << A[j] << endl;
      if(A[j] == 0)
	{
	  standing[j] = standing[j-1];
	}
      else
	if (standing[j-1]<j){
	  friends += (j - standing[j-1]);
	  standing[j] = standing[j-1] + friends + A[j];
	}
	else{
	  standing[j] = standing[j-1] + A[j];
	}
      // cout << j << " , friends : " << friends << " , standing : " << standing[j] << endl;
    }
    cout << "Case #" << (i+1) << ": " << friends << endl;
  }
  return 0;
}
