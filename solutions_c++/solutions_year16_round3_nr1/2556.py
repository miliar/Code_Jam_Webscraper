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

int N;
int main(int argc, char * argv[]){
		
	LL  FUN(LL n);
	LL Prime(LL n);
	LL ModEx(LL a,LL b, LL n);

	
	string infile = argv[1];
	string outfile = infile + ".out";
	
	ofstream ofh (outfile, ios::out); if (!ofh.is_open()) { cout << "Can't open the output file " << outfile << "\n";return 1;}
	string line;ifstream ifh (infile);if (!ifh.is_open()) { cout << "Can't open input file" << infile << "\n";return 1;}
	
	
	// Input: Number of Test Cases
	int T;getline(ifh,line);stringstream(line) >> T;
	
	
	FF(t,T){
	
		// Input
		int N;getline(ifh,line);stringstream(line) >> N;		
		size_t nPP=0,oPP=0;
		int P[N];
		getline(ifh,line);
		FF(n,N){
		    nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> P[n];oPP=nPP+1;
		    //nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> B[n];oPP=nPP+1;
		}
		
		
		
		// Solution
		int sum=0;
		FF(n,N)
		  sum+=P[n];
		
		//int idx[N]; FF(n,N) idx[n]=n; 
		cout << "Case #"<< t+1 << ": ";
		ofh << "Case #"<< t+1 << ": ";
		
		
		while(sum>0)
		{
		  
		  int max1=0,max2=0,max3=0;
		  int pos1=0,pos2=0,pos3=0;
		  FF(n,N){
		    if(P[n]>max1){
		      max1=P[n];
		      pos1=n;
		    }
		  }
		
		  P[pos1]=0;
		  FF(n,N){
		    if(P[n]>max2){
		      max2=P[n];
		      pos2=n;
		    }
		  }
		  
		  P[pos2]=0;
		  FF(n,N){
		    if(P[n]>max3){
		      max3=P[n];
		      pos3=n;
		    }
		  }
		  
		  P[pos1]=max1;
		  P[pos2]=max2;
		  
		if((max2-max1)>=2 || ((max1-max2)==1 && max2<=(sum-2)/2)){
		    int out=min(P[pos1],2);
		    sum-=out;
		    P[pos1]-=out;
		      cout << " ";
		      ofh << " ";
		    FF(i,out){
		      cout  << char('A'+pos1);
		      ofh  << char('A'+pos1);
		    }
		  }
		  else{
		    if((max1-max2)==0 && max3<=(sum-2)/2){
		      sum-=2;
		      P[pos1]-=1;
		      P[pos2]-=1;
		      cout << " " << char('A'+pos1) << char('A'+pos2);
		      ofh << " " << char('A'+pos1) << char('A'+pos2);
		    } 
		      
		    else{
		      sum-=1;
		      P[pos1]-=1;
		      cout << " ";
		      cout << char('A'+pos1);
		      ofh << " ";
		      ofh << char('A'+pos1);
		    }
		  }
		}
		cout << endl;
		ofh << endl;
		// Output
		//ofh << "Case #"<< t+1 << ": "<< endl;
		//cout << "Case #"<< t+1 << ": "<< endl;
	}
return 0;
}
	  

	