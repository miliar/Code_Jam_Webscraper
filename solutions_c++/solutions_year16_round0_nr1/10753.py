#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;
int R[10];
int  N;
int t,T=0;
int main(){
  cin >> t;
  for(int j=1;j<=t;j++){
    cin>>N;
   
    unsigned long long int n=N;
    string numero;
    int cont=0;

    while(cont<10){
      if(N==0)break;
      stringstream num;
      num << N;
      numero = num.str();
      sort(numero.begin(),numero.end());
      for(int i =0;i<10;i++){
	if(!R[i]){
	  int s = i+48;
	  if(binary_search(numero.begin(),numero.end(),s)){
	    R[i]=1;
	    cont++;
	 
	  }
	}
      }
      N = n+N;
      numero.clear();
   
    }
    if(N-n==0){
      cout<<"Case #"<<j<<": INSOMNIA"<<endl;
    }else{
      cout<<"Case #"<<j<<": "<<N-n<<endl ;
    }
    for(int i =0;i<10;i++)R[i]=0;
   

  }
  return 0;
}
