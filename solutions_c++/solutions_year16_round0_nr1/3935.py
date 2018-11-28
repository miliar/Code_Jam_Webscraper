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
		
	string infile = argv[1];
	string outfile = infile + ".out";
	
	ofstream ofh (outfile, ios::out); if (!ofh.is_open()) { cout << "Can't open the output file " << outfile << "\n";return 1;}
	string line;ifstream ifh (infile);if (!ifh.is_open()) { cout << "Can't open input file" << infile << "\n";return 1;}
	
	
	// Input: Number of Test Cases
	int T;getline(ifh,line);stringstream(line) >> T;
	
	
	FF(t,T){
	
		int N;getline(ifh,line);stringstream(line) >> N;
		
		int dig[10];
		FF(i,10) dig[i]=0;
		
		int ans=-1;
		
		for(int mul=1;mul<=10;mul++){		
		    int a=mul*N;
		    dig[a%10]=1;
		    a/=10;
		    while(a!=0){
		      dig[a%10]=1;
		      a/=10;
		    }
		    
		    int sumDig=0;
		    FF(i,10)
		      sumDig+=dig[i];
			
		    if(sumDig==10){
		      ans=mul*N;break;}		      
		}
		
		
		    int sumEven=0;
		    int sumOdd=0;
		    FF(i,5){
		      sumEven+=dig[i*2];
		      sumOdd+=dig[i*2+1];
		    }
		    
		    if(sumOdd==0 && sumEven>0)
		      ans=0;
		    		    
		    if(sumOdd==1 & sumEven==1 & dig[0]==1 & dig[5]==1)
		      ans=0;
		    
		    if(ans==-1){		      
		      int mul=11;
		      while(1){		
			 int a=mul*N;
			  dig[a%10]=1;
			  a/=10;
			  while(a!=0){
			    dig[a%10]=1;
			    a/=10;
			  }
		    
			  int sumDig=0;
			  FF(i,10)
			    sumDig+=dig[i];
			  if(sumDig==10){
			    ans=mul*N;
			    break;//mul=10000;
			  }
			  mul++;
		      }
			  
		    }
		    
		// Output
		if(ans==0){
		  ofh << "Case #"<< t+1 << ": "  << "INSOMNIA" << endl;
		  cout << "Case #"<< t+1 << ": " << "INSOMNIA" << endl;
		}
		else{
		  ofh << "Case #"<< t+1 << ": " << ans << endl;
		  cout << "Case #"<< t+1 << ": " << ans << endl;
		}
	}
return 0;
}



		