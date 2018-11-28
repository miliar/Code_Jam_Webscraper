#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>

using namespace std;

int i,j,l,x,y,t;
char a[101],b[101];
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
			if(a[j]=='-')
				b[l-j-1]='+';
			else
				b[l-j-1]='-';
		}
		b[l]='\0';
		x=0;
		for(j=1;j<l;j++){
			if(a[j]=='+' && a[j-1]=='-' || a[j]=='-' && a[j-1]=='+'){
				x++;
			}
		}
		// if(x>0 && a[0]=='+')
		// 	x++;		
		if(a[l-1]=='-')
			x++;
		y=0;
		// if(b[0]=='+')
		// 	y++;
		for(j=1;j<l;j++){
			if(b[j]=='+' && b[j-1]=='-' || b[j]=='-' && b[j-1]=='+'){
				y++;
			}
		}
		if(b[l-1]=='-')
			y++;
		y++;
		x= (x<y)?x:y;
		fout<<"Case #"<<i<<": "<<x<<endl;
		// if(a[l-1]=='+' && a[0]=='-' || b[l-1]=='+' && b[0]=='-')
		// 	fout<<"Case #"<<i<<": "<<x<<endl;
		// else if(a[l-1]=='+' && a[0]=='+' || b[l-1]=='+' && b[0]=='+' || a[l-1]=='-' && a[0]=='-' || b[l-1]=='-' && b[0]=='-')
		// 	fout<<"Case #"<<i<<": "<<x+1<<endl;
		// else
		// 	fout<<"Case #"<<i<<": "<<x+2<<endl;
	}
	return 0;
}

