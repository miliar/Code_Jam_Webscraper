#include<iostream>
#include<stdio.h>
#include<memory.h>
#include<stdlib.h>
using namespace std;

void msort(float s[],int start,int end){
	int i,j;
	i = start;
	j = end;
	float temp = s[start];
	while(i < j){
		while(i < j && temp < s[j])
			j--;
		if(i < j){
			s[i] = s[j];
			i ++;
		}
		while(i < j && s[i] <= temp)
			i ++;
		if(i < j){
			s[j] = s[i];
			j --;
		}
	}
	s[i] = temp;
	if(start < i)
		msort(s,start,j - 1);
	if(i < end)
		msort(s,j + 1,end);
}

int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int T;
	int N;
	float a[1000],b[1000];
	scanf(" %d",&T);
	for(int i = 0;i < T;i ++){
		scanf(" %d",&N);
		memset(a,1,sizeof(a));
		memset(b,1,sizeof(b));
		for(int j = 0;j < N;j ++)
			scanf(" %f",&a[j]);
		for(int j = 0;j < N;j ++)
			scanf(" %f",&b[j]);
		msort(a,0,N-1);
		msort(b,0,N-1);
		// 用第一种方法
		int ja = 0,jb = 0;
		while(jb < N){
			if(a[ja] < b[jb]){
				ja ++;
				jb ++;
			}
			else 
				jb ++;
		}
		int warwin = N - ja;
		// 用第二种方法
		ja = 0;

		jb = 0;
		int dwin = 0;
		while(ja < N){
			if(a[ja]>b[jb]){
				dwin += 1;
				ja++;
				jb++;
			}
			else{
				ja ++;
			}
		}
		printf("Case #%d: %d %d\n",i + 1,dwin,warwin);
	}
}