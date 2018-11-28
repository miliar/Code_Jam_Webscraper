//============================================================================
// Name        : Lawnmower.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;
char winner='.';
bool empty=false;

int main() {
	int   T;
	int   N,M;
		scanf("%d",&T);

		int c=1;
		while(T--){

			scanf("%d %d",&N,&M);
			short** field=new short*[N];
			short* maxc=new short[M];
			short* maxr=new short[N];

			for (int j = 0; j < N; ++j) {

				field[j]=new short[M];
				short m=0;
				for (int i = 0; i < M; ++i) {
					scanf("%d",&(field[j][i]));
					m=max(m,field[j][i]);
				}
				maxr[j]=m;
			}

			for (int i = 0; i < M; ++i) {

				short  m=0;
				for (int j = 0; j < N; ++j) {
					m=max(m,field[j][i]);
				}
				maxc[i]=m;
			}
			char* works="YES";
			for (int j = 0; j < N; ++j) {


							for (int i = 0; i < M; ++i) {
								if(field[j][i]<maxc[i]&&field[j][i]<maxr[j]){
									works="NO";
									goto done;
								}
							}

						}
			done:
			printf("Case #%d: %s\n",c++,works);

		}

		return 0;
}
