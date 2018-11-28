/*
 * Lawnmower.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: Loc Ngo
 */
#include<iostream>
#include<fstream>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("out.txt");
int T;
int N,M;
int L[100][100];
int P[100][100];
int MR[100];
int MC[100];
bool H[101];
int K[100];
int k;

void lawn(int height) {
	for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
			if(L[i][j]==height){
				if(height >= MR[i])
				{
					//cut the row i
					for(int k=0;k<M;k++)
						P[i][k] = height;
				}
				if(height >= MC[j])
				{
					//cut the column j
					for(int k=0;k<N;k++)
						P[k][j] = height;
				}
			}
}

void process(int t) {
	fin>>N>>M;
	fill(H,H+101,false);
	fill(MR,MR+100,0);
	fill(MC,MC+100,0);
	for(int i=0;i<N;i++)
		for(int j=0;j<M;j++){
			fin>>L[i][j];
			if(MR[i]<L[i][j])
				MR[i] = L[i][j];
			if(MC[j]<L[i][j])
				MC[j] = L[i][j];
			H[L[i][j]] = true;
		}
	k=0;
	for(int i=1;i<=100;i++)
		if(H[i])
			K[k++] = i;

	for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
			P[i][j] = K[k-1];
	k--;



	for(int i=k-1;i>=0;i--)
		lawn(K[i]);

	bool OK = true;
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++)
			if(P[i][j]!=L[i][j])
				OK = false;
	}
	fout<<"Case #"<<t<<": ";
	if(OK)
		fout<<"YES\n";
	else
		fout<<"NO\n";
}

int main(){
	fin>>T;
	for(int i=0;i<T;i++)
		process(i+1);
	return 0;
}
