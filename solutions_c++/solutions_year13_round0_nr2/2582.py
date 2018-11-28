#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <string>


using namespace std;

#define _CRT_SECURE_NO_WARNINGS
#ifdef TC_OFFLINE
	#define PAUSE system("pause");
#else
	#define PAUSE
#endif

class RedIsGood{

public:
	
	static double getProfit(int R, int B){

		return 0;
	};
};

int ipt[1000][1000];
int max1[1000],max2[1000];

int main(){
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++){
		int N,M;
		cin>>N>>M;
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++)
			cin>>ipt[i][j];
		}
		fill(max1,max1+N,-1);
		fill(max2,max2+M,-1);
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++){
				max1[i]=max(max1[i],ipt[i][j]);
				max2[j]=max(max2[j],ipt[i][j]);
			}
		int ok=true;
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				if(ipt[i][j]!= max1[i] && ipt[i][j]!=max2[j]){
					ok=false;
					goto fin;
				}
fin:
		cout<<"Case #"<<tt<<": "<<(ok?"YES":"NO")<<endl;
	}
	PAUSE;
	return 0;
};

