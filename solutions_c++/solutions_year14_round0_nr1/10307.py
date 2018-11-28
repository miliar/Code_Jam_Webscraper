#include<stdio.h>
#include<iostream>
#include<sstream>
#include<fstream>
using namespace std;
int main()
{
	ifstream inp("A-small-attempt0.in");
	ofstream out("out.txt");
	int t,n,i,j,k;
	int a[4][4];
	inp>>t;
	for(i=0;i<t;i++){
		inp>>n;
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				inp>>a[j][k];
			}
		}
		int m;
		int b[4][4],tmp;
		inp>>m;
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				inp>>b[j][k];
			}
		
		}
		int c=0;
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				if(a[n-1][j] == b[m-1][k]){
					c++;
					tmp=a[n-1][j];
					
				}
				
			}
			if(c>1)
			break;
			
		}
		if(c == 1){
			out<<"Case #"<<i+1<<": "<<tmp<<endl;
		}else if(c>1){
			out<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}else if(c==0){
			out<<"Case #"<<i+1<<": Volunteer cheated!\n";
		}
	}
		return 0;
}
