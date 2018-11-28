#include <iostream>
#include <algorithm>
using namespace std;

int a[5][5];
int b[5];
int c[5];

int main(){
  int t,z,i,j,r,count,num;
  cin >> t;
  for(z=1;z<=t;z++){
    cin >> r;
    count=0;
    for(i=1;i<=4;i++)
      for(j=1;j<=4;j++)
        cin >> a[i][j];
    for(i=1;i<=4;i++)
      b[i]=a[r][i];
    sort(b+1,b+5);
    cin >> r;
    for(i=1;i<=4;i++)
      for(j=1;j<=4;j++)
        cin >> a[i][j];
    for(i=1;i<=4;i++)
      c[i]=a[r][i];
    sort(c+1,c+5);
    i=1;j=1;
    while(i<=4 && j<=4){
      if(b[i]==c[j]){
        count++;
        num=b[i];
      }
      if(b[i]>c[j])
        j++;
      else
        i++;
    }
    if(count==1)
      cout << "Case #" << z << ": " << num << endl;
    if(count==0)
      cout << "Case #" << z << ": " << "Volunteer cheated!" << endl;
    if(count>1)
      cout << "Case #" << z << ": " << "Bad magician!" << endl;
  }
  return 0;
}