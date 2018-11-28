#include <iostream>
#include<cmath>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<sstream>
#include<iterator>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<map>
#include<ctime>
#include<utility>
#include<cstdio>
#include<set>

using namespace std;

#define FOR(i,a,b) for(int i=a;i!=b;i++)

int main ()
{	
	int T,M,N;
	char result[50];
	bool st;
	FILE* fi;
	FILE* fo;
	fi = fopen("B-large.in","r");
	fo = fopen("B-large.out","w");
	fscanf(fi,"%d",&T);
	int V[100][100];
	FOR(i,1,T+1){
		st = true;
		fscanf(fi,"%d %d",&N,&M);
		cout << N << " " << M<<endl;
		vector<int> Vr(N,0);
		vector<int> Vc(M,0);
		FOR(j,0,N){
			FOR(k,0,M){
				fscanf(fi," %d ",&V[j][k]);
				Vr[j] = Vr[j]>V[j][k]?Vr[j]:V[j][k];
				Vc[k] = Vc[k]>V[j][k]?Vc[k]:V[j][k];
			}
		}
		FOR(j,0,N){
			FOR(k,0,M){
				if(V[j][k]!=Vr[j] && V[j][k]!=Vc[k]){
					sprintf(result,"Case #%d: NO",i);
					st = false;
					break;
				}
			}
			if(!st)break;
		}
		if(st) sprintf(result,"Case #%d: YES",i);
		
		fprintf(fo,"%s\n",result);
	}

	return 0;
}
