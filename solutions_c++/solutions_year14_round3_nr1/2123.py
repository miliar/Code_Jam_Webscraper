#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  ofstream outputFile;
  ifstream inputFile;
  int T,pos,ans,count;
  long long A ,B,temp;
  string in , inA,inB;
  outputFile.open ("C:\\mix\\workspaces\\codejam_c++\\codejam\\output.txt");
  inputFile.open ("C:\\mix\\workspaces\\codejam_c++\\codejam\\A-small-attempt1.in");
  inputFile >>T;
  for(int i=1;i<=T;i++ ) {
	  ans=0;
	  count=0;
	  inA="";
	  inB="";

	  inputFile >>in;
	  pos = in.find("/");        
	  inA = in.substr (0,pos);  
	  inB = in.substr (pos+1); 

	  std::string str3 = in.substr (pos); 
	  A = stol (inA,nullptr,10);
	  B = stol (inB,nullptr,10);
	  temp=B;
	  while(temp%2==0) {
		temp=temp >>1;
		count++;
	  }
	  if(temp == 1 ) {
		  while(A<B){
			A=A <<1;
			ans++;
		  }
		
	  }
	  /*if(B%2!=0 || ceil(log(B) {
		if((B/A)%2 == 0 ) {
			ans= log (B/A)/0.693147;
		} else {
			ans=ceil(log (double(B)/A)/0.693147);
		}
	  }

	  */
	  if(ans>=40 || ans==0) {
		
		outputFile <<"Case #"<<i<<": impossible\n";
	  } else {
		outputFile <<"Case #"<<i<<": "<<ans<<"\n";
	  }
	}
  
  
  outputFile.close();
  inputFile.close();
  return 0;
}