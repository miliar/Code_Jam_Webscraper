#include <iostream>
#include <stack>

using namespace std;

stack <char> serve;

int main(){
  int t; string in;
  int cases = 1;
  cin >> t;

  while(t--){
    
    
    cin >> in;

    for(int i = in.size()-1 ; i >= 0; --i){
      //cout << in[i] << endl;
      serve.push(in[i]);
    }

    // while(!serve.empty()){
    //   char out =  serve.top();
    //   cout << out << endl;
    //   serve.pop();
    // }

    int contmas = 0;
    int cont = 0;
    int moves = 0;
    
    while(!serve.empty()){
      //cout << "hola" << endl;
      contmas = cont = 0;
      
      if(!serve.empty()){
	while(serve.top() == '-'){
	  //cout << "jiji" << endl;
	  serve.pop();
	  contmas++;
	  if(serve.empty()) break;	   
	}

       
	  if(contmas){
	    //cout << "yuju1" << endl;
	    moves++;
	  }
	
	
      }

      if(!serve.empty()){
	for(int i = 0; i < contmas; ++i)
	  serve.push('+');
      }
       
      //cout << "jijiFASDFA" << endl;
      

      if(!serve.empty()){
	while(serve.top() == '+'){
	  // cout << "jaja" << endl;
	  serve.pop();
	  cont++;
	  if(serve.empty()) break;
	}
	
	if(!serve.empty()){
	  if(cont){
	    //cout << "yuju2" << endl;
	    moves++ ;
	  }
	}
	
      }
      
      
    }
    
    cout << "Case #" << cases  << ": " <<moves << endl;
    cases++;
    
  }
  
  return 0;
}
