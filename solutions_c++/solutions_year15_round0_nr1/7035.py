#include <iostream>
#include <string>


using namespace std;

int main(){

  int t,teste=1;
  cin>>t;
  while(t--){
    int n;
    string s;
    cin>>n;
    cin>>s;
    int up=0,invite=0;
    for(int i=0; i<s.size(); i++){
      if(up>=i){
	up+=(s[i]-'0');
      }
      else{
	invite+=i-up;
	up++;
	up+=(s[i]-'0');
      }
    }
    
    cout<<"Case #"<<teste<<": "<<invite<<endl;
    teste++;
  }
}
