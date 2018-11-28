#include<stdio.h>
#include<string.h>
#include<vector>
#include<iostream>
#include<algorithm>
#include<set>

using namespace std;

FILE *fin;
FILE *fout;

int n;
double a[1010],b[1010];

int dewar(){
	int ret = 0;
	int pa = n,pb = n;
	while(pa > 0 && pb > 0){
		if(a[pa] > b[pb]){
			++ret;
			--pa;
			--pb;
		}else{
			--pb;	
		}
	}
	return ret;
}

int war(){
	int ret = 0;
	set<double> ken;
	for(int i = 1;i <= n;++i)
		ken.insert(b[i]);
	for(int i = 1;i <= n;++i){
		set<double>::iterator it = ken.upper_bound(a[i]);
		if(it == ken.end()){
			ken.erase(ken.upper_bound(-1));	
			++ret;
		}else{
			ken.erase(it);	
		}
	}
	return ret;
}

int main(){
	fin = fopen("D-large.in","r");
	fout = fopen("gcj.out","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int cas = 1;cas <= T;++cas){
		fscanf(fin,"%d",&n);
		for(int i = 1;i <= n;++i)
			fscanf(fin,"%lf",&a[i]);
		for(int i = 1;i <= n;++i)
			fscanf(fin,"%lf",&b[i]);
		sort(a + 1,a + 1 + n);
		sort(b + 1,b + 1 + n);
		int a1 = dewar();
		int a2 = war();
		fprintf(fout,"Case #%d: %d %d\n",cas,a1,a2);
	}
	fclose(fin);
	fclose(fout);
	system("pause");
	return 0;
}

