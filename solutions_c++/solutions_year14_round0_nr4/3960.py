#include<iostream>
#include<cstdlib>
#include<iostream>
#include<stdio.h> 
#include<stdlib.h>
#include<fstream>
#include<set>
#include <limits>
#include<iomanip>
#include<cmath>
using namespace std;
ifstream fin("D-large.in");
ofstream fout("D-large.out");
int cmp(const void* a,const void* b)
{
	if ((*(double*)a ) - (*(double*)b) > 0 )return 1;
	if ((*(double*)a ) - (*(double*)b) == 0 )return 0;
	if ((*(double*)a ) - (*(double*)b) < 0 )return -1;
}
int main()
{
	int n,p,ct1,ct2,size,pa,pb,l;
	double a[1001],b[1001],ca[1001],cb[1001];
	fin>>n;
	for(int k=0;k<n;k++)
	{
		fin>>size;
		ct1=0;
		ct2=0;
		pa=0;
		pb=0;
		for(int i=0;i<size;i++) {
			fin>>a[i];
			ca[i]=a[i];
		}
		for(int i=0;i<size;i++) {
			fin>>b[i];
			cb[i]=b[i];
	    }
		qsort(a,size,sizeof(double),cmp);
		qsort(b,size,sizeof(double),cmp);
		qsort(ca,size,sizeof(double),cmp);
		qsort(cb,size,sizeof(double),cmp);
		l=0;
		for(int i=0;i<size;i++){
			for(int j=l;j<size;j++){
				if(a[j]!=-100&&a[j]>b[i]){
						l = j+1;
						a[j]=-100;
						b[i]=-100;
						ct1++;
						break;
					
				}
			}
		}
		l = 0;
		for(int i=0;i<size;i++){
			for(int j=0;j<size;j++){
				if(cb[j]!=-100&&cb[j]>ca[i]){
						l = j+1;
						ca[i]=-100;
						cb[j]=-100;
						ct2++;
						break;
				}
			}
		}
		fout<<"Case #"<<k+1<<": "<<ct1<<" "<<size-ct2<<endl;
	}
}
