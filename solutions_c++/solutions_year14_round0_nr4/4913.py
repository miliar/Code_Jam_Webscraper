#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<limits.h>
#include<vector>
#include<algorithm>
using namespace std;
struct node{
	double x;
};
int cmp(node a,node b){
	return a.x>b.x;
}
float k[11],v[11];
vector< node > kk,vv;
int main(){
	int test,n,i;
	scanf("%d",&test);
	for(int g=1;g<=test;g++){
		vv.clear();
		kk.clear();
		scanf("%d",&n);
		double x;
		for(i=0;i<n;i++){
			scanf("%lf",&x);
			vv.push_back( (node) {x} );
		}
		for(i=0;i<n;i++){
			scanf("%lf",&x);
			kk.push_back( (node) { x });
		}
		sort(vv.begin(),vv.end(),cmp);
		sort(kk.begin(),kk.end(),cmp);
		for(i=0;i<n;i++){
			v[i]=vv[i].x;
			k[i]=kk[i].x;
		}
		int cnt2=0,l=0,r=n-1;
		while(1){
			int f=1,t;
			for(int p=l,t=0;p<n,t<=r;p++,t++){
				if(v[t]<k[p]){
					f=0;
					break;
				}
			}
			if(!f){
				++l;
				--r;
			}
				else if(f)	break;
		}
		//cout<<"Case #"<<g<<": "<<n-l<<" ";
		int cnt1=0,vis[11]={0};
		for(i=0;i<n;i++){
			double min=10000000.00;
			int idx=-1;
			for(int j=0;j<n;j++){
				if(k[j]>v[i]&&min>k[j]-v[i]&&!vis[j]){
					idx=j;
				}
			}
			if(idx==-1)
				++cnt1;
			else
				++vis[idx];
		}
		printf("Case #%d: %d %d\n",g,n-l,cnt1);
		//cout<<cnt1<<endl;
	}
	return 0;
}


