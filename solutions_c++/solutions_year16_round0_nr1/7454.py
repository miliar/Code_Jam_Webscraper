#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int kontrol[10];
int dizi[101];

int main(){
  int i,j,m,n,m2,k,sayac1=0,sayac2=0,sayac3=0;
  ifstream oku ("girdi1.txt");
  ofstream yaz ("cikti1.txt");
  oku >> n ;
  for(i=1;i<=n;i++){
    oku >> dizi[i];
  }
  for(i=1;i<=n;i++){
    m=dizi[i];
    for(k=m;k<=111000000;k+=m){
      m2=k;
      if(k==0){
        yaz <<"Case #"<<i<<": INSOMNIA"<<endl;
        sayac3++;
        break;
      }
      for(j=7;j>=1;j++){
        if(m2%10!=0){
            sayac1=1;
        }
        if(sayac1==1 && kontrol[m2%10]==0){
            kontrol[m2%10]=1;
            sayac2++;
        }
        m2/=10;
        if(m2==0)
          break;
      }
      if(sayac2==10){
        kontrol[0]=0;kontrol[1]=0;kontrol[2]=0;kontrol[3]=0;kontrol[4]=0;
        kontrol[5]=0;kontrol[6]=0;kontrol[7]=0;kontrol[8]=0;kontrol[9]=0;
        sayac2=0;
        sayac1=0;
        yaz << "Case #"<<i<<": "<<k<<endl;
        sayac3++;
        break;
      }
    }
  }
}
