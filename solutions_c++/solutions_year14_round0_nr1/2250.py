#include <iostream>
#include <vector>
#include <algorithm>    // std::sort

using namespace std;

int main(){
  int T;
  cin>>T;
  for (int i=1;i<=T;i++){
    int aa,bb;
    cin>>aa;
    int a[4][4], b[4][4];

    int j,k;
    for (j=0;j<4;j++)
    for (k=0;k<4;k++) {cin>>a[j][k];}
    cin >>bb;
    for (j=0;j<4;j++)
    for (k=0;k<4;k++) {cin>>b[j][k];}

    int c=0, val=-1;

       for (j=0;j<4;j++)
	  for (k=0;k<4;k++) {
	  if (a[aa-1][j]==b[bb-1][k]) {c++; val=a[aa-1][j];}
	  }
  cout << "Case #"<<i<<": ";
  if (c==1)
  cout << val<<endl;
  else if (c==0)
    cout << "Volunteer cheated!"<<endl;
  else if (c>1)
    cout << "Bad magician!" <<endl;

  }
  return 0;
}
