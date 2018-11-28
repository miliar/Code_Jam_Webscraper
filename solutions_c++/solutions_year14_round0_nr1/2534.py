#include<iostream>
#include<conio.h>
#include<string>
#include<fstream>
#include<algorithm>
using namespace std;
int send(int a[4][4],int b[4][4],int f, int s,int&c){
	int commons=0;
	sort(a[f],a[f]+4);
	sort(b[s],b[s]+4);
	int i=0,j=0;
	while(i<4&&j<4){
		if(a[f][i]==b[s][j]){
			commons++;
			c=a[f][i];
			i++;
			j++;
		}
		else if(a[f][i]>b[s][j]){
			j++;
		}
		else if(a[f][i]<b[s][j]){
			i++;
		}
	}
	return commons;
}

int main(){
	ifstream fin("A-small-attempt0.in");
	ofstream fout("sum.txt");
	int T;
	int ans[100],n[100];
	fin>>T;
	int a[4][4];
	int b[4][4],f,s,c;
	for(int i=0;i<T;i++){
		fin>>f;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				fin>>a[j][k];
		fin>>s;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				fin>>b[j][k];
		ans[i]=send(a,b,f-1,s-1,c);
		n[i]=c;
	}
	for(int i=0;i<T;i++){
		if(ans[i]==1)
			fout<<"Case #"<<i+1<<": "<<n[i]<<"\n";
		if(ans[i]>1)
			fout<<"Case #"<<i+1<<": Bad magician!\n";
		if(ans[i]<1)
			fout<<"Case #"<<i+1<<": Volunteer cheated!\n";
	}
}