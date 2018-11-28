// Include Header and Libraries
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <stdint.h>
#define FF(I,N) for(int I=0;I<N;I++)
#define FR(I,N) for(int I=N-1;I>=0;I--)
typedef long long LL;
using namespace std;
const LL INFN = -9223372036854775807; //const LL INFN = (int64_t)1<<63;
const LL INFP = 9223372036854775807; // const LL INFN = (int64_t)1<<62;

int main(int argc, char * argv[]){
		
	LL  FUN(LL n);
	
	string infile = argv[1];
	string outfile = infile + ".out";
	
	ofstream ofh (outfile, ios::out); if (!ofh.is_open()) { cout << "Can't open the output file " << outfile << "\n";return 1;}
	string line;ifstream ifh (infile);if (!ifh.is_open()) { cout << "Can't open input file" << infile << "\n";return 1;}
	
	
	// Input: Number of Test Cases
	int T;getline(ifh,line);stringstream(line) >> T;
	
	
	FF(t,T){
	
		int N,J;
		size_t nPP=0,oPP=0;
		
		// Input
		getline(ifh,line);		
		nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> N;oPP=nPP+1;
		nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> J;oPP=nPP+1;
		
				
		// Solution
		int sol=0;
		LL ans[J];
		LL div[J][9];
		
		LL num = pow(2,N-1)-1;
		
		while(sol<J & num<pow(2,N)-1){
		  
		  num=num+2;
		  //cout << num<<":";
		  int bin[N];
		  LL temp=num;
		  FF(n,N){
		    bin[n]=temp%2;
		    temp/=2;
		  }
		  
		  //FF(n,N){cout << bin[n];}
		  //cout << endl;
		
		  int base=2;
		  for(base=2;base<=10;base++){
		    LL baseSum=0;
		    FF(n,N)
		      baseSum+=bin[n]*pow(base,n);
		    LL res=FUN(baseSum);
		    if(res==1)
		      break;
		    else
		      div[sol][base-2]=res;
		  }
		  
		  if(base==11){
		    ans[sol]=num;
		    sol++;
		  }
		}
		    
		    
		// Output
		
		cout << "Case #"<< t+1 << ": "<< endl;
		FF(j,J){
		    LL temp=ans[j];
		    int bin[N];
		    FF(n,N){
		      bin[n] = temp%2;
		      temp/=2;
		    }
		    FF(n,N)
		      cout << bin[N-n-1];
		      
		    FF(i,9)
		      cout << " " << div[j][i];
		    cout << endl;
		}
		
		ofh << "Case #"<< t+1 << ": "<< endl;
		FF(j,J){
		    LL temp=ans[j];
		    int bin[N];
		    FF(n,N){
		      bin[n] = temp%2;
		      temp/=2;
		    }
		    FF(n,N)
		      ofh << bin[N-n-1];
		    FF(i,9)
		      ofh << " " << div[j][i];
		    ofh << endl;
		}
		    
		
	}
return 0;
}



      LL  FUN(LL n){
	   if (n == 2 || n == 3)
	     return 1;
	   if (n % 2 == 0)
	     return 2;
	   if (n % 3 == 0)
	     return 3;

	  int i = 5;
	  int w = 2;

	  while (i * i <= n){
	      if (n % i == 0)
		return i;
	      i += w;
	      w = 6 - w;
	  }

	  return 1;
      }
		