#include<iostream>
#include<fstream>
using namespace std;

ofstream fout("magic.out");

int T;
int A1,A2;
int G1[4][4];
int G2[4][4];
int R1[4];
int R2[4];
int V[4];

int main(){
	cin>>T;
	for(int i=0;i<T;i++){
		cin>>A1;
		for(int r=0;r<4;r++){
			for(int c=0;c<4;c++){
				cin>>G1[r][c];
				if(r==A1-1){
					R1[c]=G1[r][c];
				}
			}
		}
		cin>>A2;
		for(int r=0;r<4;r++){
			for(int c=0;c<4;c++){
				cin>>G2[r][c];
				if(r==A2-1){
					R2[c]=G2[r][c];
				}
			}
		}
		for(int r=0;r<4;r++){
			V[r]=1;
			for(int c=0;c<4;c++){
				if(R1[r]==R2[c])V[r]++;
			}
		}
		int count=0;
		int num;
		for(int r=0;r<4;r++){
			if(V[r]==2){
				count++;
				if(count==2)break;
				if(count==1){
					num=R1[r];
				}
			}
		}
		if(count==1)fout<<"Case #"<<i+1<<": "<<num<<endl;
		if(count>1)fout<<"Case #"<<i+1<<": Bad Magician!"<<endl;
		if(count==0)fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl; 
	}

	return 0;
}