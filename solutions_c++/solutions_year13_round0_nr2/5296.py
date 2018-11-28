#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
using namespace std;
#define MAXN 100
int lawn[MAXN][MAXN];
int a[MAXN*MAXN];
int lawn2[MAXN][MAXN];
int counter;

void copyA(int m,int n){
	int i,j,k=0,s,ch=1;
	for(;k<MAXN*MAXN;k++){
		a[k]=101;
	}
	k=0;
	for(i=0;i<m;i++)
		for(j=0;j<n;j++){
			for(s=0;s<k;s++){
				if(a[s]==lawn[i][j])
				ch=0;}
			if(ch==1){	
			a[k]=lawn[i][j];
			k++;}
			ch=1;
	}
}

void lawninit(int m, int n){
	int i,j;
	for(i=0;i<MAXN;i++)
		for(j=0;j<MAXN;j++)
		lawn[i][j]=101;
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
		cin>>lawn[i][j];
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
		lawn2[i][j]=lawn[i][j];
}

void swap(int *i, int *j)
{
	int temp;
	temp=*i;
	*i=*j;
	*j=temp;
}

void quickSort(int l, int r)
{
	int x,i,j;
	int mid=(l+r)/2;
	i=l;
	j=r;
	x=a[mid];
	do
	{
		while (x>a[i]) i++;
		while (x<a[j]) j--;
		if(i<=j) { swap(&a[i], &a[j]);
		i++;
		j--;
	}
	}
	while(i<=j);
	if(j>l)
	quickSort(l, j);
	if(i<r)
	quickSort(i, r);
		
}
//p-th col for number a
bool checklawnCol(int m,int p,int e){
	int i;
	for(i=0;i<m;i++){
		if(lawn[i][p]!=e) return false;
	}
	return true;
}

bool checklawnRow(int n,int p, int e){
	int i;
	for(i=0;i<n;i++){
		if(lawn[p][i]!=e) return false;
	}
	return true;
}

void rebuildCol(int m,int p,int e){
	int i;
	for(i=0;i<m;i++){
		lawn2[i][p]=e;
	}
}

void rebuildRow(int m,int p,int e){
	int i;
	for(i=0;i<m;i++){
		lawn2[p][i]=e;
	}
}

void copylawns(int m,int n){
	int i,j;
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
			lawn[i][j]=lawn2[i][j];
}

void checklawn(int m,int n,int e){
	int i,j,c=e+1;
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			if(lawn[i][j]==a[e]){
			if(checklawnCol(m,j,a[e])) rebuildCol(m,j,a[c]);
			else{
				if(checklawnRow(n,i,a[e])) rebuildRow(n,i,a[c]);
				else {counter=1;}}
			}
		}
	}

	copylawns(m,n);
	if(a[c]!=101)
	checklawn(m,n,c);
}

int main(void){
	int T;
	int m,n;
	int i;
	scanf("%d",&T);
	int an[T];
	for(i=0;i<T;i++){
		counter=0;
		scanf("%d %d",&m,&n);
		lawninit(m,n);
		copyA(m,n);
		quickSort(0,m*n-1);
		checklawn(m,n,0);
		if(counter) an[i]=1;
		else an[i]=0;
	}
	for(i=0;i<T;i++)
	if(an[i]) printf("Case #%d: NO\n",i+1);
	else printf("Case #%d: YES\n",i+1);
	return 0;
}
	
	


	
