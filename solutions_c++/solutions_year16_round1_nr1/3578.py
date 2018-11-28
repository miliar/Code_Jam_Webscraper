#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>

using namespace std;

int i,j,l,x,y,t;
char *p,*f,*e;
char a[1001],b[1001];
int main(){
	ifstream fin;
	ofstream fout;
	fin.open("in.txt");
	fout.open("out.txt");
	fin>>t;
	for(i=1;i<=t;i++){
		fin>>a;
		l=strlen(a);
		for(j=0;j<l;j++){
			p=new char ;
			*p = a[j];
			if(j==0){
				f=p;
				e=p;
			}
			else{
				if(*p >= *f)
				{
					*(f-1) = *p;
					f--;
				}
				else{
					*(e+1)=*p;
					e++;
				}
			}
		}
		*(e+1) = '\0';
		fout<<"Case #"<<i<<": "<<f<<endl;
	}
	return 0;
}

