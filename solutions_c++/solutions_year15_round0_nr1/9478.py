#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;


int casos;
int caso=1;
int S;
char arr[1100]; 

int main(){

  cin >> casos;
  
  while(caso<=casos){
  
    cin >> S >> arr;
  
    int acum=0;
    int res=0;
    for(int i=0; i<=S;i++){

      if(acum<i){
      
        res += i-acum;
        acum=i;      
      }
    
      acum+=arr[i]-48;
       
    }
    
    cout << "Case #"<<caso++<< ": "<<res<<endl;
  
  }


}
