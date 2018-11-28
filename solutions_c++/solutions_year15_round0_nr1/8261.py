#include<iostream>
#include<algorithm>
#include<string>



using std::cout;
using std::cin;

using std::endl;

int main(){

int T;
cin >> T;
if (T == 0)
  exit(0);
int S[T]={0};

for (int i=0;i<T;i++)
{
  int max;
  cin >> max;
  max +=1;
  int a[max];
  char b[max];
  cin >> b;
  int c=0,s=0;
  int j=0;
  for (j=0;j<max;j++){
     a[j]=(int)b[j]-'0';
  }
  int zp;
  for (j=0;j<max;j++){
    if(a[j] == 0){
      zp=j;
      continue;
    }
    if(s<j){     
      int ab= abs(s-j);
      c=c+ab;
      a[zp]=ab;
      s+=ab;    
    }
    s+=a[j]; 
  }   
 
  S[i]=c;
}

for(int i=1;i<=T;i++){

 cout << "Case #"<< i <<": " << S[i-1]<< endl;

}


return 0;
}
