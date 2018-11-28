
#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <math.h>
#include <set>
#include <sstream>
#include <algorithm>

#include <memory.h>

#ifdef _WIN32
#include <time.h>
#endif

using namespace std;

#ifdef _WIN32
typedef __int64 n64;
typedef unsigned __int64 u64;
#else
typedef long long n64;
typedef unsigned long long u64;
#endif

#if !defined( _WIN32 )
#define _itoa itoa

char * itoa( int _Val, char * _DstBuf, int _Radix)
{
	sprintf( _DstBuf, "%d", _Val );
	return _DstBuf;
}

#endif
string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

#define INF 0x3FFFFFFF




int garden[100][100];

int main(){
		
	ifstream fin("b.in");
	ofstream fout("b.out");


	int n;
	fin >> n;

	int M,N;
	for(int i=1;i<=n;i++){
		fin >> N>> M;

		bool possible = true;
		for(int j=0;j<N;j++){
			for(int k=0;k<M;k++){
				fin >> garden[j][k];
			}
		}
		if(N==1 || M==1){
			fout << "Case #" << i <<": YES" << endl;
		}
		else{
			for(int j=0;(j<N && possible);j++){
				for(int k=0;(k<M && possible);k++){
					bool min = true;
					bool min1 = true;

					
					for(int a=0;a<N;a++){
						if(garden[a][k] > garden[j][k]){
							min = false;
						}
					}
					for(int a=0;(a<M);a++){
						if(garden[j][a] > garden[j][k]){
							min1 = false;
						}
					}


					// if(i==9){
					// 	cout << min1 << "" << min <<" " ;


					// 	if(min==false && min1==false){
					// 		for(int a=0;a<N;a++){
					// 			cout << garden[a][k] ;
					// 		}
					// 		cout << endl;
					// 		for(int a=0;(a<N);a++){
					// 			cout << garden[j][a] ;
								
					// 		}
					// 		cout << endl;
					// 	}
					// }

					if(!(min1 || min)){
						fout << "Case #" << i <<": NO" << endl;
						
						possible = false;
						break;
					}
					// if(garden[j][k] < garden[0][k] && garden[j][k]  <garden[N-1][k] )
					// 	if(garden[j][k] < garden[j][0] && garden[j][k] < garden[j][M-1]){
					// 		fout << "Case #" << i <<": NO" << endl;
					// 		possible = false;
					// 		break;
					// 	}
				}
			// 	if(i==9){
			// 	cout << endl;
			// }
			}


			if(possible){
				fout << "Case #" << i <<": YES" << endl;
			}


		}
	}
	


}