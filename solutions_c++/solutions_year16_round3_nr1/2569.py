#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void f2(int *P, int len,int *l1,int *l2){
	int i;//,v1,v2;

	//v1=0;v2=0;
	//*l1=len;*l2=len;
	for(i=0;;i++){
		if(P[i]!=0) break;
	}
	*l1 = i;

	for(i=0;i<len;i++){
		if(!P[i]) continue;

		if(P[i] > P[*l1]) {
			*l1 = i;
			//v1 = P[i];
		}
		/*
		else if((P[i]==v1)&&(P[i]>v2)){
			*l2 = i;
			v2 = P[i];
		}
		else if(P[i]>v2){
			*l2 = i;
			v2 = P[i];
		}
		*/
	}
	for(i=0;;i++){
		if((P[i]!=0)&&(i!=*l1)) break;
	}
	*l2 = i;
	for(i=*l2+1;i<len;i++){
		if(!P[i]) continue;
		if(i==*l1) continue;
		if(P[i] > P[*l2]) *l2 = i;
	}
}

void rm2(int *P,int len){
	int i;
	int l1,l2;

	for(i=0;i<len;i++){
		if(P[i]!=0){
			l1 = i;
			break;
		}
	}
	for(i=l1+1;i<len;i++){
		if(P[i]!=0){
			l2 = i;
			break;
		}
	}
	//printf("%d %d\n",l1,l2);
	for(i=0;i<P[l1];i++){
		//cout <<" "<<'A'+l1<<'A'+l2;
		printf(" %c%c",'A'+l1,'A'+l2);
	}
	cout<<endl;
}

void rm(int *P,int len,int num){
	
}

int main(int argc, char* argv[]){
	int T,nocase;
	int N;

	int i,j,k,t,num;
	int P[32];
	string S1,S2;

	int l1,l2;

	cin >> T;  // read t. cin knows that t is an int, so it reads it as such.
	//T = 4;
	for (nocase = 1; nocase <= T; ++nocase) {
		
		cin >> N;
		//printf("%d\n",N);
		num=0;j=0;
		for(i=0;i<N;i++){
			cin >> P[i];
			num += P[i];
			if(P[i]==1) j++;

			//printf("%d ",P[i]);
		}
		//printf("\n");
		//printf("j: %d\n",j);
		cout << "Case #" << nocase << ":";

		if(j==N){
			if((N%2)==0){
				for(i=0;i<N/2;i++)
					printf(" %c%c",'A'+2*i,'A'+2*i+1);
				printf("\n");
			}
			else {
				printf(" A");
				for(i=0;i<(N-1)/2;i++)
					printf(" %c%c",'B'+2*i,'B'+2*i+1);
				printf("\n");
			}
		}
		else{
			//printf("j:%d\n",j);
			t=N-j;
			while(t){
				f2(P,N,&l1,&l2);
				//printf("l1: %d l2: %d\n",l1,l2);
				if(P[l1]>P[l2]){
					printf(" %c",'A'+l1);
					P[l1]--;
					num--;
					if(P[l1]==1)t--;
				}
				else {
					printf(" %c%c",'A'+l1,'A'+l2);
					P[l1]--;P[l2]--;
					num-=2;
					if(P[l1]==1)t--;
					if(P[l2]==1)t--;
				}
				//break;
			}
			if((N%2)==0){
				for(i=0;i<N/2;i++)
					printf(" %c%c",'A'+2*i,'A'+2*i+1);
				printf("\n");
			}
			else {
				printf(" A");
				for(i=0;i<(N-1)/2;i++)
					printf(" %c%c",'B'+2*i,'B'+2*i+1);
				printf("\n");
			}
			/*
			t=N;
			while(t){
				j=0;
				for(i=1;i<N;i++){
					if(!P[i]) continue;
					if(P[i] > P[j]) j = i;
				}
				//cout <<" "<<'A'+j;
				printf(" %c",'A'+j);
				P[j]--; num--;
				if(P[j]==0) t--;
				
				f2(P, N,&l1,&l2);
				printf("\n%d %d\n",l2,l2);
				if( (l2*t) <= (num-1)){
					//cout <<'A'+l1<<endl;
					printf("%c",'A'+l1);
					P[l1]--; num--;
					if(P[l1]==0) t--;
				}
				//getchar();
			}
			printf("\n");
			*/
		}

	}

	return 0;
}