#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<cstring>
using namespace std;
int N,P,n;
bool w[2000],l[2000];

vector<int> f(vector <int> v){
	if(v.size() == 1) return v;
	vector <int> W ,L;
	for(int i = 0;i < v.size(); i += 2){
		if(v[i] < v[i+1]){	W.push_back(v[i]);	L.push_back(v[i+1]);}
		else{ W.push_back(v[i+1]);L.push_back(v[i]);	}
	}
	W = f(W);
	L = f(L);
	for( int i = 0; i < L.size();i++) W.push_back(L[i]);
	return W;
}
int main(){
	int runs,a,b;	
	scanf("%d",&runs);
	for( int r = 1; r <= runs; r++){
		memset( w, 0 , sizeof w);
		memset( l, 0 , sizeof l);
		scanf("%d %d",&N,&P);
		
		n = ( 1 << N);
		for( int i = 0; i < n; i++){
			vector <int> v;
			v.push_back(i);
			for( int j = i + 1; j < n; j++)	v.push_back(j);
			for( int j = 0; j < i ; j++) 	v.push_back(j);
			v = f(v);
			for( int j = 0; j < v.size(); j++) if(v[j]==i && j<P) w[ i ] = true;
		}
		for( int i = 0; i < n; i++){
			vector <int> v;
			v.push_back( i );
			for( int j = 0; j < i; j++) v.push_back( j );
			for( int j = i + 1 ; j < n; j++) v.push_back( j );
			v = f(v);
			for( int j = 0; j < v.size(); j++) if(v[j] == i && j >= P) l[ i ] = true;
		}
		for( int i = 0; i < n; i++)  if(!l[ i ]) a = i;
		for( int i = 0; i < n ; i++) if(w[ i ]) b = i;
		printf("Case #%d: %d %d\n",r, a,b);
	}
	return 0;

}
