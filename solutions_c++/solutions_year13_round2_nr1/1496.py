#include<stdio.h>
#include<cmath>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<set>
#include<algorithm>

using namespace std;

typedef unsigned long long int llint;

llint res = 1<<31;

void visit(llint atual,llint n, vector<llint> v, llint mote, llint custo){
	if(custo > res) return;
	//cout<<atual<<" --- "<<mote<<" --- "<<custo<<endl;
	//end path
	if(atual==n){
		//cout<<mote<<endl;
		//cout<<"Custo: "<<custo<<endl;
		res = min(res,custo);
		return;
	}
	if(mote > v[atual]){
		visit(atual+1,n,v,mote+v[atual],custo);
	}else{
		//add
		if(mote>1) visit(atual,n,v,mote+mote-1,custo+1);
		//remove
		visit(atual+1,n,v,mote,custo+1);
	}
}

void dfs(llint start,llint n, vector<llint> v, llint mote){
	visit(start,n,v,mote,0);
}

int main(){

	int tt;
	scanf("%d",&tt);
	int casos=1;
	
	while(tt-- > 0){
		res = 1<<31;
		printf("Case #%d: ",casos++);
		
		unsigned long long int ini,n;
		scanf("%lld %lld",&ini,&n);
		vector<unsigned long long int> v(n);
		
		for(int i = 0;i<n;i++){
			scanf("%lld",&v[i]);
		}
		sort(v.begin(),v.end());
		
		dfs(0,n,v,ini);
		
		cout<<res<<endl;
	}

	return 0;
}
