#include <vector>
#include <queue>
#include <string.h>
#include <bits/stdc++.h>
using namespace std;

int main(){
	ifstream fin("A-large (1).in");
	ofstream fout("testrespuesta.txt");
	long int t;
	fin>>t;
	string palabra;
	for(long int j=0; j<t; j++){
		fin>>palabra;
		vector<long int> letra(10,0);
		for(long int i=0; i<palabra.length(); i++){
			if(palabra.at(i)=='Z') letra[0]++;
			if(palabra.at(i)=='W') letra[1]++;
			if(palabra.at(i)=='U') letra[2]++;
			if(palabra.at(i)=='V') letra[3]++;
			if(palabra.at(i)=='X') letra[4]++;
			if(palabra.at(i)=='R') letra[5]++;
			if(palabra.at(i)=='F') letra[6]++;
			if(palabra.at(i)=='H') letra[7]++;
			if(palabra.at(i)=='I') letra[8]++;
			if(palabra.at(i)=='N') letra[9]++;
		}
		vector<long int> numero(10,0);
		numero[0]=letra[0];
		numero[2]=letra[1];
		numero[4]=letra[2];			
		numero[6]=letra[4];
		letra[5]-=(numero[4]+numero[0]);
		numero[3]=letra[5];
		letra[6]-=numero[4];
		//cout<<letra[6];
		numero[5]=letra[6];
		letra[3]-=numero[5];
		numero[7]=letra[3];
		letra[7]-=numero[3];
		numero[8]=letra[7];
		letra[8]-=(numero[5]+numero[6]+numero[8]);
		numero[9]=letra[8];
		letra[9]-=(2*numero[9]+numero[7]);
		numero[1]=letra[9];
		fout<<"Case #"<<j+1<<": ";
		for(int i=0; i<10; i++){
			long int y=0;
			while(y<numero[i]){
				fout<<i;
				y++;
			}
		}
		fout<<"\n";
	}
}

