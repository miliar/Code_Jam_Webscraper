#define MAX 101
#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int T;
int N;
string one,two;
string S[MAX];

int C[MAX];
int V[MAX][MAX][2];
bool B[MAX][MAX][2];

ofstream fout("output.out");

void clear(){
	for(int i=0;i<MAX;i++){
		for(int j=0;j<MAX;j++){
			V[i][j][0]=0;
			V[i][j][1]=0;
			B[i][j][0]=false;
			B[i][j][1]=false;
		}
	}
}

int M(int x,int y,bool b){

	if(B[x][y][b]){
		return V[x][y][b];	
	}

	if(one.length()==x && two.length()==y)return 0;
	if(x>=one.length() || y>=two.length())return 99999;
	
	int min_val=99999;
	if(one[x]==two[y]){
		if(!b){
			min_val=min(min_val,M(x+1,y+1,false));
			min_val=min(min_val,M(x+1,y,true));
			min_val=min(min_val,M(x,y+1,true));
		}else{
			min_val=min(min_val,1+M(x+1,y,true));
			min_val=min(min_val,1+M(x,y+1,true));
			min_val=min(min_val,1+M(x+1,y+1,false));
		}
	}
	int index;
	if(b==true)index=1;
	if(b==false)index=0;
	V[x][y][index]=min_val;
	B[x][y][index]=true;
	return min_val;
}
	

int main(){
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>N;
		clear();
		for(int i=0;i<N;i++){
			cin>>S[i];
		}
		int v=0;
		//cout<<"#"<<t<<endl;
		one=S[0];
		two=S[1];

		v=M(0,0,false);
		
		/*
		for(int i=0;i<N;i++){
			for(int j=i+1;j<N;j++){
				one=S[i];
				two=S[j];
				v=M(0,0,false);
				//cout<<one<<" "<<two<<" "<<M(0,0,false)<<endl;
			}
		}*/

		fout<<"Case #"<<t<<": ";
		if(v<99999){
			fout<<v<<endl;
		}else{
			fout<<"Fegla Won"<<endl;
		}
		//cout<<v<<endl;
		//cout<<endl<<endl;

	}
	return 0;
}