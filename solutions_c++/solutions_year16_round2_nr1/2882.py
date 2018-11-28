#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include <cassert>
#include<map>
#include<queue>
#include<stack>
#include<time.h>
#include<math.h>
#include<set>
#include<complex>
using namespace std;
#define INF 0x3f3f3f3f
#define DINF 1e30
#define EPS 1e-9
#define PII acos(-1)
#define LL long long
#define Pii pair<int,int>
#define For(i,n) for(int i=0;i<n;i++)
#define ileer(n) scanf("%d",&n)
#define i2leer(n,m) scanf("%d %d",&n,&m)
#define fleer(n) scanf("%lf",&n)
#define f2leer(n,m) scanf("%Lf %Lf",&n,&m)
#define MK make_pair
#define PB push_back
#define llenar(arr,val) memset(arr,val,sizeof(arr))
#define VLL vector< LL >
#define matrix vector<VI >
#define F first
#define S second
#define MAXN 36000
#define MAXM 201
int letras[30];

char verga[10][5]={{'Z','E','R','O'},{'O','N','E'},{'T','W','O'},{'T','H','R','E','E'},{'F','O','U','R'},{'F','I','V','E'},{'S','I','X'},{'S','E','V','E','N'},{'E','I','G','H','T'},{'N','I','N','E'}};
int can[10];
int veces[10];
int mapa[300];

int main(){
	int n;
	ileer(n);
	for(int c=0;c<n;c++){
		string g;
		cin>>g;
		
		llenar(letras,0);
		llenar(veces,0);
		can[0]=4;
		can[1]=3;
		can[2]=3;
		can[3]=5;
		can[4]=4;
		can[5]=4;
		can[6]=3;
		can[7]=5;
		can[8]=5;
		can[9]=4;
		for(int i=0;i<300;i++) mapa[i]=-1;
		mapa['Z']=0;
		mapa['W']=2;
		mapa['U']=4;
		mapa['X']=6;
		mapa['G']=8;
		mapa['O']=1;
		mapa['T']=3;
		mapa['F']=5;
		mapa['V']=7;
		mapa['I']=9;
		for(int i=0;i<g.size();i++){
			letras[g[i]-'A']++;
		}
		
		for(int i=0;i<30;i++){
			if(letras[i]>0){
				//cout<<(char)(i+'A')<<endl;
				if(mapa[i+'A']>=0 &&mapa[i+'A']%2==0){
					//cout<<"entro"<<endl;
					veces[mapa[i+'A']]+=letras[i];
					int aux=letras[i];
					for(int j=0;j<can[mapa[i+'A']];j++){
						letras[verga[mapa[i+'A']][j]-'A']-=aux;
					}
					
				}
			}
		}
		
		for(int i=0;i<30;i++){
			if(letras[i]>0){
				
			//	cout<<(char)(i+'A')<<" "<<letras[i]<<endl;
				if(mapa[i+'A']>=0 &&mapa[i+'A']%2==1 && mapa[i+'A']!=9){
					veces[mapa[i+'A']]+=letras[i];
				//	cout<<"entro"<<endl;
					int aux=letras[i];
					for(int j=0;j<can[mapa[i+'A']];j++){
						letras[verga[mapa[i+'A']][j]-'A']-=aux;
					}
					
					
				}
			}
		}
		
		for(int i=0;i<30;i++){
			if(letras[i]>0){
				//cout<<(char)(i+'A')<<endl;
				if(mapa[i+'A']>=0 &&mapa[i+'A']==9){
				//	cout<<"entro"<<endl;
					veces[mapa[i+'A']]+=letras[i];
					int aux=letras[i];
					for(int j=0;j<can[mapa[i+'A']];j++){
						letras[verga[mapa[i+'A']][j]-'A']-=aux;
					}
					
				}
			}
		}
		
		printf("Case #%d: ",c+1);
		for(int i=0;i<10;i++){
			for(int j=0;j<veces[i];j++) printf("%d",i);
		}
		printf("\n");
	}
	
	
	
	
	
}