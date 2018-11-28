#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>


using namespace std;

bool iscons(char c){
   if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')return false;
   else return true;		
}

//Does A contain a consonant sequence of length l?
bool contseq(string A, int l){
	
	int length = A.size();
	if(l>length) return false;
	for(int i=0;i<length+1-l;++i){
		bool novow=true;
		for(int j=i; j<i+l;++j){
			if(!iscons(A[j])) novow=false;			
		}	
		if(novow==true) {return true;}
		
	}
	return false;
}


int main(){

  //cout << "max_size: " << str.max_size() << "\n";  

  ifstream input("input.in",ios::in);
  ofstream output("output.out", ios::out);
  
  int T=0;
  string S;
  int L;  
  int n;
  
  int ans;  

  input>>T;


  for(unsigned int t=0; t<T; ++t){
    
    
    input>>S;
    input>>n;
    
    ans = 0;

    L=S.size(); 
	cout<<L<<endl;
    for(int i=0;i<L;++i){
	for(int j=i;j<L;++j){
		if(contseq(S.substr(i,j-i+1), n)){
			ans++;
			//cout<<S.substr(i,j-i+1)<<endl;
		}	
	}
    }
    


    output<<"Case #"<<t+1<<": "<<ans<<"\n";
    cout<<endl;
  } 
  


}
