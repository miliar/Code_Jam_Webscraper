#include <iostream>
#include <stack>
#include <queue>

//#include <string>
using namespace std;





int main(){
  int t,movs,cont,cas=1;
  string in;
  stack<char> cakes;
  
  cin>>t;

  while(t--){
    movs=0;
    while(!cakes.empty()) cakes.pop();

    cin>>in;
    for(int i=in.size()-1;i>=0;i--){
      cakes.push(in[i]);
    }
    
    while(!cakes.empty()){

      if(cakes.top()=='-'){
	cont=0;
	while(!cakes.empty() && cakes.top()=='-'){
	  cakes.pop();
	  cont++;
	}

	for(int k=0;k<cont;k++)
	  cakes.push('+');

	movs++;
      }else{
	while(!cakes.empty() && cakes.top()=='+')
	  cakes.pop();
    
	if(!cakes.empty())
	  movs++;	
      }
      
    }
    cout<<"Case #"<<cas<<": "<<movs<<endl;
    cas++;
  }

return 0;
}
