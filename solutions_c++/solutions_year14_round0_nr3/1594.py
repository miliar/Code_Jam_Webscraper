#include<iostream>
#include<stdio.h>
#include<stdint.h>
#include<fstream>
using namespace std;
#define QL 100000

/*
int main(){
	int CaseNum;
	ifstream in;
	ofstream out;
	in.open("test.txt");
	out.open("out.txt");
	in>>CaseNum;
	for(int Case=0;Case<CaseNum;Case++){



	out<<"Case #"<<Case+1<<":";
	}
	return 0;
}
*/

int map[60][60];



typedef struct{
	uint64_t state[60];
	uint64_t cand[60];
	int r,c;
	int k;
}item;

item que[QL];
int pl=0,pr=0;
int N,M,K;
uint64_t pw[60];

int flood(int r,int c){
	if(map[r][c]==0)return 0;
	map[r][c]=2;
	int t,ch;
	for(int i=r-1;i<=r+1;i++)
		for(int j=c-1;j<=c+1;j++){
			if(i>=0&&i<N&&j>=0&&j<M&&map[i][j]==1){
				map[i][j]=2;
				ch=0;
				for(int ii=i-1;ii<=i+1;ii++)
					for(int jj=j-1;jj<=j+1;jj++)
						if(ii>=0&&ii<N&&jj>=0&&jj<M&&map[ii][jj]==0)
							ch=1;
				if(ch==0){
					if(!flood(i,j))return 0;
				}
			}
		}
	return 1;
}
int check(uint64_t state[60]){
	int k=0;
	for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
			{if(pw[j]&state[i])k++;
			map[i][j]=(pw[j]&state[i])>0;
	}
	if(k!=K)
		return 0;
	if(!map[0][0])
		return 0;
	flood(0,0);
	k=0;
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			cout<<map[i][j];
			if(map[i][j]==2)k++;
		}
		cout<<endl;
	}
	if(k!=K)
		return 0;
	return 1;

}

void print(item &q){
	cout<<q.k<<":"<<K<<endl;
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			if(i==0&&j==0){cout<<"c";continue;}
			if(i==q.r&&j==q.c){cout<<"h";continue;}
			if(q.cand[i]&pw[j]){cout<<"o";continue;}
			if(q.state[i]&pw[j])cout<<".";
			else cout<<"*";
		}
		cout<<endl;
	}

}

int main(){
	int CaseNum;
	ifstream in;
	ofstream out;
	in.open("C-small-attempt4.in");
	//in.open("test.txt");
	out.open("Cout.txt");
	in>>CaseNum;
	for(int i=0;i<60;i++)
		pw[i]=1<<i;

	for(int Case=0;Case<CaseNum;Case++){
		in>>N>>M>>K;
		K=N*M-K;
		if(K<0){
			cout<<"Case #"<<Case+1<<": \nImpossible\n";
			continue;
		}

		pl=0;
		pr=1;
		fill(que[pl].state,que[pl].state+60,0);
		fill(que[pl].cand,que[pl].cand+60,0);
		que[pl].state[0]=1;
		que[pl].r=0;
		que[pl].c=0;
		que[pl].k=1;

		int pt,k,ck;
		while(que[pl].k!=K&&pl!=pr){
			pt=pr;
			//if(pr>=100000)cout<<"OUT OF MEMORY"<<endl;
			k=0;
			//print(que[pl]);
			if(que[pl].k>K){
					pl++;
					pl%=QL;
					continue;
			}
			//cout<<pr<<endl;
			que[pl].cand[que[pl].r]&=~pw[que[pl].c];
			for(int i=que[pl].r-1;i<=que[pl].r+1;i++){
				for(int j=que[pl].c-1;j<=que[pl].c+1;j++){
					if(i>=0&&i<N&&j>=0&&j<M&&(que[pl].state[i]&pw[j])==0){
						que[pl].state[i]|=pw[j];
						que[pl].cand[i]|=pw[j];
						k++;
					}
					if(i>=0&&i<N&&j>=0&&j<M&&(que[pl].cand[i]&pw[j])){
						que[pr].r=i;
						que[pr].c=j;
						pr++;
						pr%=QL;
						if(pr==pl)cout<<"OUT OF MEMORY"<<endl;
					}

				}
			}
			que[pl].k+=k;
			if(que[pl].k==K){
				break;
			}
			if(k==0||que[pl].k>K){
				pr=pt;
				pl++;
				pl%=QL;
				continue;
			}
			int p;
			for(p=pl+1;p<pt;p++){
				ck=1;
				for(int i=0;i<N;i++){
					if(que[pl].state[i]!=que[p].state[i]){
						ck=0;
						break;
					}
				}
				if(ck){
					pr=pt;
					pl++;
					pl%=QL;
					break;
				}
			}
			if(p<pt)continue;

			for(;pt<pr;pt++){
				for(int i=0;i<N;i++){
					que[pt].state[i]=que[pl].state[i];
					que[pt].cand[i]=que[pl].cand[i];
				}
				que[pt].k=que[pl].k;
			}
			pl++;
			pl%=QL;
		}

		if(que[pl].k!=K||(pl==pr)){
			out<<"Case #"<<Case+1<<":\nImpossible\n";
			//cout<<N<<":"<<M<<":"<<K<<endl;
			continue;
		}


		out<<"Case #"<<Case+1<<":"<<endl;
		//cout<<N<<":"<<M<<":"<<K<<endl;
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				if(i==0&&j==0){out<<"c";continue;}
				if(que[pl].state[i]&pw[j])out<<".";
				else out<<"*";
			}
			out<<endl;
		}
		//if(!check(que[pl].state))
			//cout<<"error"<<endl;

	}
	return 0;
}