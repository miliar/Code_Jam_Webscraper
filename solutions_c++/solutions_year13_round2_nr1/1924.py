#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long addGlob();
int T;
long A;
int N;
long temp;
string s;
vector<vector<int> > grid2D (5, vector<int>(5));
vector<int> grid1D(5); 
vector<long> xsize(101); 

int i;
int j;
int k;
int x;
long y;
int z=0;
int q;
long answer;
long xanswer;
bool boolm=1;
int main(int argc, char *argv[]) {
	ifstream in("A-large.in");
	in>>T;
	ofstream out("A-large.out");
	
	for(i=1;i<=T;i++){
		xanswer=2000001;
		boolm=1;
		z=0;
		answer=0;
		q=0;
		for(j=1;j<=101;j++){
			xsize[j]=0;
		}
		in>>A;
		in>>N;
			for(j=1;j<=N;j++){
			in>>temp;	
			xsize[j]=temp;
			k=xsize[j];
			}
			std::sort (xsize.begin(), xsize.begin()+N+1);
			if(A==1){
				out << "Case #" << i << ": "<<N<< endl;
				goto B;
			}
			for(k=1;k<=N;k++){
				if(A>xsize[k]){
					y=xsize[k];
					A=A+y;
					xsize[k]=0;
					z++;
				}
				else{
					goto A;
				}
			}
			A:
				if(q>5*N+1){
					out << "Case #" << i << ": "<<xanswer<< endl;
					goto B;
				}
				if((N-z)==0){
					if(xanswer<answer){
						answer=xanswer;
					}
					out << "Case #" << i << ": "<<answer<< endl;
					goto B;
				}
				if(boolm){
					xanswer=answer+N-z;
					boolm=0;
				}
				if((N-z)==1){
					answer++;
					if(xanswer<answer){
						answer=xanswer;
					}
						out << "Case #" << i << ": "<<answer<< endl;
						goto B;
				}
				/*
				if((N-z)==2){
					if(addGlob()>xsize[N-1]){
						A=A+A-1+xsize[N-1];
						answer++;
					}
					if(A>xsize[N]){
						if(xanswer<answer){
							answer=xanswer;
						}
						out << "Case #" << i << ": "<<answer<< endl;
						goto B;
					}
					else{
						answer++;
						if(xanswer<answer){
							answer=xanswer;
						}
						out << "Case #" << i << ": "<<answer<< endl;	
						goto B;
					}
				}
				*/
				
				while(1){
					A=addGlob();
					answer++;
					for(k=z+1;k<=N;k++){
						if(A>xsize[k]){
							A=A+xsize[k];
							xsize[k]=0;
							z++;
						}
						else{
							q++;
							goto A;
						}
					}
					q++;
					goto A;
				}
				B:
					int cool=1;
	}
	
	return 0;
}

long addGlob(){
	long b;
	b=A+A-1;
	return b;
}
