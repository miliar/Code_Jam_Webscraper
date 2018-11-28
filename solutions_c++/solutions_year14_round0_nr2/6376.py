#include <iostream>
#include <cstdio>
using namespace std;


int main(){
  int cases;
  double C,F,X;
  double a[3],b[3],c[3];
  cin >> cases;
  for (int cc=0; cc<cases; cc++){
    
    cin >> C; cin>>F; cin>>X;
    cout << "Case #" << cc+1 << ": ";
    if (C/2+X/(2+F)>X/2) {
      printf("%.7f\n",X/2);
      continue;
    }
 
    a[1]=C/2; a[2]=a[1]+C/(2+F);
    for (int i=1; i<500000; i++) {
      a[0]=a[1];a[1]=a[2];a[2]+=C/(2+(i+1)*F);
      for (int j=0; j<3; j++) {
      b[j]=X/(2+(i+j)*F);
      c[j]=a[j]+b[j];
      }
      if ((c[0]>c[1]) && (c[1]<c[2])) {
      printf("%.7f\n",c[1]);
      break;
      } else if ((c[0]<c[1]) && (c[1]<c[2])) {
      printf("%.7f\n",c[0]);
      break;
      } 
      
    }
 }// for cases
 return 0;
}//main
