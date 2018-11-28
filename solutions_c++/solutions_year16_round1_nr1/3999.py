#include <iostream>

using namespace std;

int main(){
  int t,cont=1;
  string s,salida;
  
  cin>>t;

  while(t--){

    cin>>s;
    salida=s.at(0);
    
    for(int i=1;i<s.size();i++){
      if(s.at(i)>=salida.at(0))
	salida=s.at(i)+salida;
      else
	salida+=s.at(i);
    }

    cout<<"Case #"<<cont<<": "<<salida<<endl;
    cont++;

  }

    return 0;
}
