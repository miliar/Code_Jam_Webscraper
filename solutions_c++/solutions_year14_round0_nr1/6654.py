#include <iostream>

using namespace std;

int main() {
  int T, a1, a2, arr1[4][4], arr2[4][4], count, num, m;

  cin>>T;

  m = 1;
  while(T--) {
    count = 0;
    cin>>a1;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
	cin>>arr1[i][j];
    
    cin>>a2;

    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
	cin>>arr2[i][j];

    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++){
	if(arr1[a1 - 1][i] == arr2[a2 - 1][j]){
	  num = arr1[a1 - 1][i];
	  count++;
	}
      }
    if(count == 0)
      cout<<"Case #"<<m<<": "<<"Volunteer cheated!\n";
    else if(count == 1)
      cout<<"Case #"<<m<<": "<<num<<"\n";
    else
      cout<<"Case #"<<m<<": "<<"Bad magician!\n";
    m = m + 1;
  }
  return 0;
}
      
