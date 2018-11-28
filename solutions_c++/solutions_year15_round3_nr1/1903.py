// Include Header and Libraries
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <stdint.h>
#define FF(I,N) for(int I=0;I<N;I++) {
#define FF1(I,A,N) for(int I=A;I<=N;I++) {
#define FR(I,N) for(int I=N-1;I>=0;I--) {
#define FR1(I,N,A) for(int I=N;I>=A;I--) {
typedef long long LL;
using namespace std;
const LL INFN = -9223372036854775807; //const LL INFN = (int64_t)1<<63;
const LL INFP = 9223372036854775807; // const LL INFN = (int64_t)1<<62;

#define VMAX 1000 
int R,C,W;
size_t nPP=0,oPP=0;
int dp[21][21];

int main(){
	int fun(int,int);
	
	ofstream ofh ("A.out", ios::out); if (!ofh.is_open()) { cout << "Can't open the output file";return 1;}
	//string line;ifstream ifh ("T.i");if (!ifh.is_open()) {cout << "Can't open input file";return 1;}	
	string line;ifstream ifh ("A-small-attempt0.in");if (!ifh.is_open()) {cout << "Can't open input file";return 1;}
	//string line;ifstream ifh ("A-large.in");if (!ifh.is_open()) {cout << "Can't open input file";return 1;}
	
	
	int T;getline(ifh,line);stringstream(line) >> T;
	FF(t,T)
		//getline(ifh,line);stringstream(line) >> N;

		getline(ifh,line);nPP=oPP=0;
		nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> R;oPP=nPP+1;
		nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> C;oPP=nPP+1;
		nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> W;oPP=nPP+1;
		
		//getline(ifh,line);nPP=oPP=0; FF1(i,1,) nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> V[i];oPP=nPP+1;}
		///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		
		FF1(i,0,C) FF1(j,0,C) dp[i][j]=-1;}}
		int ans=fun(1,C);
		cout << ans << endl;
		ans=(R-1)*(ans)+ans+W-1;

		/*FF1(i,1,C)
			FF1(j,1,C)
				cout << dp[i][j] << " ";
			}
			cout << endl;
		}*/

		
		///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		ofh << "Case #"<< t+1 << ": " << ans << endl;
		cout << "Case #"<< t+1 << ": " << ans << endl;
	}
return 0;
}



		int fun(int s,int e){
			
			//cout << "se:" << s << e << endl;
			
			if(s<1 || e>C || s> C || e< 1 || e<s)
				return 0;
			

			//if(dp[e-s+1]!=-1) {//cout <<dp[e-s+1]<<endl;
			if(dp[s][e]!=-1){
				//return dp[e-s+1];}
				return dp[s][e];}
			
			if(e-s+1 < W){
				//dp[e-s+1]=0;
				dp[s][e]=0;
				//cout << "00" << endl;
				return 0;
			}
			
	
			if(e-s+1 == W){
				//dp[e-s+1]=0;
				dp[s][e]=1;
				//cout << "00" << endl;
				return 1;
			}
				
			if(e-s+1<2*W) {
				//dp[e-s+1]=1;
				dp[s][e]=2;
				//cout << 11 <<endl;
				return 2;
			}
			else{
				int mi=10000000;
				FF1(i,s,e)
					//if(e-i>=W)				
					mi=std::min(mi,1+fun(i+1,e)+fun(s,i-1));
					//cout << i <<" " << fun(i+1,e) << " " << fun(s,i-1) << endl;
				}

				//dp[e-s+1]=mi;
				dp[s][e]=mi;
				//cout << mi << endl;
				return mi;
			}								
						
		}

			



