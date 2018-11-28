/* vi: set sw=4 ts=4: */
//
////  main.cpp
////  Codejam2013
////
////  Created by hams on 13. 4. 13..
////  Copyright (c) 2013년 hams. All rights reserved.
////
//
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <math.h>

#define MAX_BOUND (100)
#define MIN(a,b) (a > b ? b:a)
#define MAX(a,b) (a > b ? a:b)

void init(int lawn[100][100]){
	int ni,nj;
	for(ni=0; ni < MAX_BOUND;++ni){
		for(nj=0; nj < MAX_BOUND; ++nj){
			lawn[ni][nj] = -1;

		}
	}	
}

void drawl(int lawn[100][100],int N,int M){
	for(int ni=0; ni < N; ++ni){
		for(int nj=0; nj < M; ++nj){
				printf("%d ",lawn[ni][nj]);
		}
		printf("\n");
	}
}

bool cut(int lawn[100][100],int count[100],int N,int M,int H){
	int ncount =0;
	for(int ni=0; ni < N; ++ni){
		bool bcut = true;
		for(int nj=0; nj < M;++nj){
			if( lawn[ni][nj] >  H ){
				bcut = false;
				break;
			}
		}
		if(bcut){
			for(int nj=0; nj < M;++nj){
				if( lawn[ni][nj] != -1){
					ncount++;	
					lawn[ni][nj] = -1;
				}
			}
		}
	}	
	for(int nj=0; nj < M;++nj){
		bool bcut = true;
		for(int ni=0; ni < N;++ni){
			if( lawn[ni][nj] >  H ){
				bcut = false;
				break;
			}
		}
		if(bcut){
			for(int ni=0; ni < N;++ni){
				if( lawn[ni][nj] != -1){
					ncount++;	
					lawn[ni][nj] = -1;
				}
			}
		}
	}	
	//printf("[cut]%03d ncount:%d,count:%d\n",H,ncount,count[H-1]);
	
	return ncount == count[H-1] ? true:false;

}


int main(){
	int lawn[100][100] = {0,};
	int count[100] = {0,};
	int T=0; 
	scanf("%d",&T);
	for(int nloop=0; nloop < T; ++nloop){
		init(lawn);
		memset(count,0,100);
		int N,M;
		scanf("%d",&N);
		scanf("%d",&M);
		int min=100,max=0;
		for(int ni=0; ni < N;++ni){
			for(int nj=0; nj < M;++nj){
				scanf("%d",&lawn[ni][nj]);
				min = MIN(min,lawn[ni][nj]);
				max = MAX(max,lawn[ni][nj]);
				count[lawn[ni][nj]-1]++;
			}
		}
		/*
		drawl(lawn,N,M);
		printf("min:%d,max:%d\n",min,max);
		printf("count:");
		for(int ni=0; ni < max; ni++)
			printf("%d ",count[ni]);
		printf("\n");
		*/

		bool bcut = true;
		for(int ni=min; ni<max; ++ni){
			bcut = cut(lawn,count,N,M,ni);
			//printf("cut %d:%d\n",ni,bcut);
			//drawl(lawn,N,M);
			if(!bcut)break;
		}
		printf("Case #%d: %s\n",nloop+1,bcut ? "YES":"NO");
	}
}
