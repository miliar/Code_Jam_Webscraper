// codejam.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cstring>
#include <string>
#include <set>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int T,N,M;
int lawn[200][200];
bool possible[200][200];

int main()
{
	cin>>T;
	for(int i=0; i<T; i++){
		cin>>N>>M;
		for(int j=0; j<N; j++){
			for(int k=0; k<M; k++){
				cin>>lawn[j][k];
				possible[j][k] = false;
			}
		}
		for(int j=0; j<N; j++){
			for(int k=0; k<M; k++){
				int c = 0;
				for(int l=0; l<M; l++){
					if(lawn[j][l]<=lawn[j][k])
						c++;
				}
				if(c==M){
					possible[j][k] = true;
					continue;
				}
				c = 0;
				for(int l=0; l<N; l++){
					if(lawn[l][k]<=lawn[j][k])
						c++;
				}
				if(c==N){
					possible[j][k] = true;
				}
			}
		}
		bool done = false;
		for(int j=0; j<N && !done; j++){
			for(int k=0; k<M && !done; k++){
				if(!possible[j][k]){
					done = true;
					printf("Case #%d: NO\n",i+1);
				}
			}
		}

		if(!done)
			printf("Case #%d: YES\n",i+1);
	}

	return 0;
}

