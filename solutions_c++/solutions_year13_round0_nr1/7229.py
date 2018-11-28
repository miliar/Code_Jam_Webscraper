#include<iostream>
#include<vector>
#include<string>
#include<cstdio>
using namespace std;

vector< string > A;
int horizontal(char c){
	int k;
	for(int i=0; i<4; i++){
		k=1;
		for(int j=0; j<4; j++)
			if(A[i][j]==c || A[i][j]=='.'){
				k=0;
				break;
			}
		if(k==1)
			return 1; //GANA el contrario al que se paso.
	}
	return 0;
}
int vertical(char c){
	int k;
	for(int i=0; i<4; i++){
		k=1;
		for(int j=0; j<4; j++)
			if(A[j][i]==c || A[j][i]=='.'){
				k=0;
				break;
			}
		if(k==1)
			return 1;
	}
	return 0;
}
int diagonal(char c, int x){
	int k=1;
	for(int i=0; i<4; i++){
		int t;
		if(x==0)
			t=i;
		else
			t=4-i-1;
		if(A[i][t]==c || A[i][t]=='.'){ 
			k=0;
			break;
		}
	}
	if(k==1)
		return 1;

	return 0;
}
int empty(){
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if(A[i][j]=='.')
				return 1;
	return 0;
}
int main(){
	int t;
	cin>>t;
	int xx=1;
	while(t--){
		string tmp;
		for(int i=0; i<4; i++){
			cin>>tmp;
			A.push_back(tmp);
		}
		
		if(horizontal('O')==1)
			cout<<"Case #"<<xx<<": X won\n";
		else if(horizontal('X')==1)
			cout<<"Case #"<<xx<<": O won\n";
		else if(vertical('O')==1)
			cout<<"Case #"<<xx<<": X won\n";
		else if(vertical('X')==1)
			cout<<"Case #"<<xx<<": O won\n";
		else if(diagonal('O',0)==1)
			cout<<"Case #"<<xx<<": X won\n";
		else if(diagonal('O',1)==1)
			cout<<"Case #"<<xx<<": X won\n";
		else if(diagonal('X',0)==1)
			cout<<"Case #"<<xx<<": O won\n";
		else if(diagonal('X',1)==1)
			cout<<"Case #"<<xx<<": O won\n";
		else if(empty()==1)
			cout<<"Case #"<<xx<<": Game has not completed\n";
		else
			cout<<"Case #"<<xx<<": Draw\n";
		A.clear();
		xx++;

	}
}
