#include<stdio.h>
#include<string.h>
#include<vector>
#include<iostream>

using namespace std;

FILE *fin;
FILE *fout;

double c,f,x;

double sum[1000100];

double calc(int num){
	double ret = sum[num];
	double rate = 2 + f * num;
	ret += x / rate;
	return ret;
}

int main(){
	fin = fopen("B-large.in","r");
	fout = fopen("gcj.out","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int cas = 1;cas <= T;++cas){
		fscanf(fin,"%lf%lf%lf",&c,&f,&x);
		sum[0] = 0;
		for(int i = 1;i < 1000010;++i)
			sum[i] = sum[i - 1] + c / (2 + (i - 1) * f);
	//	for(int i = 0;i <= 10;++i)
	//		printf("%f ",calc(i));
	//	puts("");
		int left = 0,right = 1000000;
		double ans = 1e9;
		while(left <= right){
			if(left == right){
				double tmp = calc(left);
				ans = min(ans,tmp);
				break;	
			}
			int mid = (left + right) >> 1;
			int midmid = (mid + right) >> 1;
			if(midmid == mid)
				++midmid;
			double am = calc(mid);
			double amm = calc(midmid);
		//	printf("l: %d, r: %d, %d %f, %d %f\n",left,right,mid,am,midmid,amm);
			if(am < amm){
				right = midmid - 1;
			}else{
				left = mid + 1;
			}
			ans = min(ans,amm);
			ans = min(ans,am);
		}
		fprintf(fout,"Case #%d: %.7f\n",cas,ans);
	}
	fclose(fin);
	fclose(fout);
	system("pause");
	return 0;
}

