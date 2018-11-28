#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<cstring>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()

map<int,int> fatora(int x){
	map<int, int> m;
	int d=2;
	while(x!=1){
		if(x%d==0){
			m[d]++;
			x/=d;
		}
		else d++;
	}
	return m;
}


map<int,int> cruza(map<int,int> a, map<int, int>b){
	for(map<int,int>::iterator it=b.begin();it!=b.end();it++){
		if(it->second > a[it->first]){
				a[it->first] = it->second;
		}
	}
	return a;
}


int main(){
	int T,R,N,M,K;
	scanf("%d",&T);
	scanf("%d %d %d %d",&R,&N,&M,&K);
	printf("Case #1:\n");
	while(R--){
		map<int,int> atual;
		for(int i=0;i<K;i++){
			int x;
			scanf("%d",&x);
			map<int,int> v = fatora(x);
			/*
			printf("VAI %d\n",x);
	    for(map<int,int>::iterator it=v.begin();it!=v.end();it++){
				printf("%d->%d\n",it->first,it->second);
			}
			printf("#\n");
			*/
			atual = cruza(atual,v);
	    /*for(map<int,int>::iterator it=atual.begin();it!=atual.end();it++){
				printf("%d->%d\n",it->first,it->second);
			}
			printf("##\n");
			*/
		}
		int pos=0;
		while(atual[3]){
			printf("3");
			pos++;
			atual[3]--;
		}
		while(atual[5]){
			printf("5");
			atual[5]--;
			pos++;
		}
		if(atual[2]==1){
			printf("2");
			pos++;
		}
		else if(atual[2] > 3-pos){
			printf("4");
			pos++;
		}
		while(pos<3){
			printf("%d",rand()%4+2);
			pos++;
		}
		printf("\n");
	}
	return 0;
}
