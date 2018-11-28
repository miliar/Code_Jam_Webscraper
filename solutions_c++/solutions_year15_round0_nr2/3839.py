#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

map<string,int> g_map;

string make_key(vector<int> P)
{
	int i;
	string Ps("");
	for (i=0;i<(int)P.size();i++){
		char c[100];
		sprintf(c,"%d,",P[i]);
		Ps+=string(c);
	}
	return Ps;
}

int search(vector<int> P_)
{
	int i;
	// そのまま減らす場合の終わり方
	vector<int> P;
	for (i=0;i<P_.size();i++){
		if (P_[i]>0){
			P.push_back(P_[i]);
		}
	}
	int Pmax=P[P.size()-1];
	// Maxを分割する場合の再帰探索
	int minute=Pmax;
	// max/2までの全パターンを試す
	for (i=1;i<=Pmax/2;i++){
		vector<int> P2=P;
		P2[P2.size()-1]-=i;
		P2.push_back(i);
		sort(P2.begin(),P2.end());
		int ret;
		string P2key=make_key(P2);
		if (g_map.find(P2key)==g_map.end()){
			ret=search(P2);
			g_map[P2key]=ret;
		}
		else ret=g_map[P2key];
		if (ret+1<minute){
			minute=ret+1;
		}
	}
	return minute;
}

int main(void)
{
	int t,T;
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		int i;
		int D;
		scanf("%d\n",&D);
		vector<int> P;
		for (i=0;i<D;i++){
			int Pi;
			scanf("%d ",&Pi);
			P.push_back(Pi);
		}
#if 0
		int minute=0;
		while (1){
			int i;
			int total=0;
			sort(P.begin(),P.end());
			// temination condition
			//fprintf(stderr,"minute=%d,",minute);
			for (i=0;i<(int)P.size();i++){
				//fprintf(stderr,"%d ",P[i]);
				total+=P[i];
			}
			//fprintf(stderr,"\n");
			if (total==0)break;
			// Gain (special)
			int Pmax=P[0],Pimax=0;
			for (i=1;i<(int)P.size();i++){
				if (P[i]>Pmax){
					Pmax=P[i];
					Pimax=i;
				}
			}
			int gain_sp=Pmax/2;
			// Gain (normal)
			int gain_n=0;
			for (i=0;i<(int)P.size();i++){
				gain_n+=(P[i]>0)?1:0;
			}
			if (gain_sp>=gain_n){
				P[Pimax]-=gain_sp;
				P.push_back(gain_sp);
			}
			else{
				for (i=0;i<(int)P.size();i++){
					if (P[i]>0)P[i]--;
				}
			}
			minute++;
		}
#else
		g_map.clear();
		sort(P.begin(),P.end());
		int minute=search(P);
#endif
		printf("Case #%d: %d\n",t,minute);
	}
	return 0;
}
