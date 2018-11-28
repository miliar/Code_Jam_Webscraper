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

string S;

int main(int argc, char * argv[]){
		
	string infile = argv[1];
	string outfile = infile + ".out";
	
	ofstream ofh (outfile, ios::out); if (!ofh.is_open()) { cout << "Can't open the output file " << outfile << "\n";return 1;}
	string line;ifstream ifh (infile);if (!ifh.is_open()) { cout << "Can't open input file" << infile << "\n";return 1;}
	
	
	// Input: Number of Test Cases
	int T;getline(ifh,line);stringstream(line) >> T;
	
	
	FF(t,T){
	
		getline(ifh,line);stringstream(line) >> S;
		
		int dig[10];
		int chCount[26];
		
		FF(i,26)
		  chCount[i]=0;
		  
		FF(i,10)
		  dig[i]=0;
		  
		FF(i,S.size())
		  chCount[S[i]-'A']++;
		  
		if(chCount['Z'-'A']>0)
		{
		  dig[0]=chCount['Z'-'A'];
		  chCount['Z'-'A']-=dig[0];
		  chCount['E'-'A']-=dig[0];
		  chCount['R'-'A']-=dig[0];
		  chCount['O'-'A']-=dig[0];
		}
		
		if(chCount['W'-'A']>0)
		{
		  dig[2]=chCount['W'-'A'];
		  chCount['T'-'A']-=dig[2];
		  chCount['W'-'A']-=dig[2];
		  chCount['O'-'A']-=dig[2];
		} 
		
		if(chCount['X'-'A']>0)
		{
		  dig[6]=chCount['X'-'A'];
		  chCount['S'-'A']-=dig[6];
		  chCount['I'-'A']-=dig[6];
		  chCount['X'-'A']-=dig[6];
		}
		
		if(chCount['G'-'A']>0)
		{
		  dig[8]=chCount['G'-'A'];
		  chCount['E'-'A']-=dig[8];
		  chCount['I'-'A']-=dig[8];
		  chCount['G'-'A']-=dig[8];
		  chCount['H'-'A']-=dig[8];
		  chCount['T'-'A']-=dig[8];
		}
		
		if(chCount['H'-'A']>0)
		{
		  dig[3]=chCount['H'-'A'];
		  chCount['T'-'A']-=dig[3];
		  chCount['H'-'A']-=dig[3];
		  chCount['R'-'A']-=dig[3];
		  chCount['E'-'A']-=dig[3];
		  chCount['E'-'A']-=dig[3];
		}
		
		if(chCount['R'-'A']>0)
		{
		  dig[4]=chCount['R'-'A'];
		  chCount['F'-'A']-=dig[4];
		  chCount['O'-'A']-=dig[4];
		  chCount['U'-'A']-=dig[4];
		  chCount['R'-'A']-=dig[4];
		}
		
		if(chCount['F'-'A']>0)
		{
		  dig[5]=chCount['F'-'A'];
		  chCount['F'-'A']-=dig[5];
		  chCount['I'-'A']-=dig[5];
		  chCount['V'-'A']-=dig[5];
		  chCount['E'-'A']-=dig[5];
		}
		
		if(chCount['O'-'A']>0)
		{
		  dig[1]=chCount['O'-'A'];
		  chCount['O'-'A']-=dig[1];
		  chCount['N'-'A']-=dig[1];
		  chCount['E'-'A']-=dig[1];
		  
		}
		
		if(chCount['S'-'A']>0)
		{
		  dig[7]=chCount['S'-'A'];
		  chCount['S'-'A']-=dig[7];
		  chCount['E'-'A']-=dig[7];
		  chCount['V'-'A']-=dig[7];
		  chCount['E'-'A']-=dig[7];
		  chCount['N'-'A']-=dig[7];	  
		}
		
		dig[9]=chCount['N'-'A']/2;
				  	
		    
		// Output
		ofh << "Case #"<< t+1 << ": "; FF(i,10) FF(j,dig[i]) ofh << i; ofh << endl;
		cout << "Case #"<< t+1 << ": "; FF(i,10) FF(j,dig[i]) cout << i;cout << endl;
	}
return 0;
}


		  

		