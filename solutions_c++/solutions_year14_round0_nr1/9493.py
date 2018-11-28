#include<iostream>
#include<cstdio>
using namespace std;

int main()
{

 int i,j,n,l,ans1,ans2,ctr,which;
 int arr1[4][4], arr2[4][4];
 cin >> n;
for(l=1;l<=n;l++){
 cin >> ans1;
 for(i=0;i<4;i++)
  for(j=0;j<4;j++)
   cin >> arr1[i][j];
 cin >> ans2;
 for(i=0;i<4;i++)
  for(j=0;j<4;j++)
   cin >> arr2[i][j];

 ctr = 0;
 for(i=0;i<4;i++)
 {
  for(j=0;j<4;j++)
  {
   if(arr1[ans1-1][i] == arr2[ans2-1][j])
   {
    ctr++;
    which = arr1[ans1-1][i];
   }
  }
 }


 cout << "Case #" << l << ": ";
 if(ctr == 0)
 {
  cout << "Volunteer cheated!" << endl;
 }
 if(ctr == 1)
  cout << which << endl;
 if(ctr > 1)
  cout << "Bad magician!" << endl;



}

 




 return 0;
}

