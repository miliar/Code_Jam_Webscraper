#include <bits/stdc++.h>
#include <fstream>
#include <stdio.h>
#define T pair<int,int>
#define x first
#define y second
using namespace std;

long double prob[201],ans,mid[201],arr[201];

void update(long double x){
	int i;
	for(i=0;i<201;i++)mid[i]=0.0;
	for(i=0;i<200;i++){
		mid[i+1]+=(prob[i]*x);
		mid[i]+=(prob[i]*((long double)1.0-x));
	}
	for(i=0;i<201;i++)prob[i]=mid[i];
}

int main(){
	int t,te,i,j,k,n,m,ans1;
	ifstream fin("input.txt");
	FILE *fp;
	fp=fopen("output.txt","w");
	fin>>t;
	for(te=0;te<t;te++){
		fin>>n>>k;
		for(i=0;i<n;i++)fin>>arr[i];
		sort(arr,arr+n);
		ans=0.0;
		for(i=0;i<=k;i++){
			for(j=0;j<n;j++)prob[j]=0.0;
			prob[0]=1.0;
			for(j=0;j<i;j++)update(arr[j]);
			for(j=0;j<(k-i);j++)update(arr[n-(j+1)]);
			ans=max(ans,prob[k/2]);
		}
		printf("Case #%d: %.9Lf\n",te+1,ans);
		fprintf(fp,"Case #%d: %.9Lf\n",te+1,ans);

	}
	return 0;
}