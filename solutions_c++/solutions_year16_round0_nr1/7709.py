#include <iostream>

using namespace std;

int main(){
  int t,n,r,on,i=1,a,cont;
  bool dig[10],nterm;
  long long num;

  cin>>t;

  while(i<=t){

    for(int j=0;j<10;j++) dig[j]=false;
    nterm=true;
    a=1;

    cin>>n;

    while(n*a && nterm){
      on=n*a;
      num=on;
      while(on!=0){
	
	r=on%10;
	dig[r]=true;
	
	on=on/10;
      }

      cont=0;
      for(int k=0;k<10;k++)
	if(dig[k])cont++;
      

      if(cont==10) nterm=false;

      a++;
    }
    cout<<"Case #"<<i<<": ";

    if(!nterm)
      cout << num <<endl;
    else
      cout<< "INSOMNIA"<<endl;

    i++;
  }
  return 0;
}
