#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>

using namespace std;

int a,b,i,j,x,y,flag[10],arr[1000001],t;

int main(){
	for(i=1;i<=1000000;i++){
		for(j=0;j<10;j++){
			flag[j]=0;
		}
		b=1;
		y=i;
		while(1){
			while(y){
				flag[y%10]=1;
				y/=10;
			}
			a=1;
			for(j=0;j<10;j++){
				if(flag[j]==0){
					a=0;break;
				}
			}
			if(a==1){
				arr[i]=i*b;
				break;
			}
			b++;
			y=i*b;
		}
//		cout<<arr[i]<<endl;
	}
	ifstream fin;
	ofstream fout;
	fin.open("in.txt");
	fout.open("out.txt");
	fin>>t;
	for(i=1;i<=t;i++){
		fin>>x;
		if(x==0)
			fout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		else
			fout<<"Case #"<<i<<": "<<arr[x]<<endl;
	}	
	return 0;
}