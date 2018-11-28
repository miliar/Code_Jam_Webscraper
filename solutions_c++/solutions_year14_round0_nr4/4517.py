#include<fstream>
#include<iostream>
#include<algorithm>
using namespace std;
const int MAXN=1001;
class war{
private:
	double Naomi[MAXN];
	double Ken[MAXN];
	int N;
	int DFS_h(int i,int j);
	int DFS_c(int n1,int k1,int k2);
public:
	void set(ifstream& fin);
	int honest();
	int cheat();
};

void war::set(ifstream& fin){
	fin>>N;
	int j;
	for(j=0;j<N;j++)
		fin>>Naomi[j];
	for(j=0;j<N;j++)
		fin>>Ken[j];
	sort(Naomi,Naomi+N);
	//cout<<Naomi[0]<<endl;
	sort(Ken,Ken+N);
}

int war::DFS_h(int i,int j){
	if( i==N || j==N )
		return 0;
	else{
		if(Naomi[i]<Ken[j])
		{
			return DFS_h(i+1,j+1);
		}
		else{
			return 1+DFS_h(i,j+1);		
		}
	}
}

int war::DFS_c(int n1,int k1,int k2){

	if(n1 == N)
		return 0;
	else{
		if(Naomi[n1]<Ken[k1])
			return DFS_c(n1+1,k1,k2-1);
		else
			return 1+DFS_c(n1+1,k1+1,k2);
	}
}

int war::honest(){
	return DFS_h(0,0);
}

int war::cheat(){
    return DFS_c(0,0,N-1);
}


void main(){
	ifstream fin;
	ofstream fout;
	fin.open("D-large.in");
	fout.open("D-large.out");
	int T;
	fin>>T;
	war solve;
	for( int i=1; i<=T; i++){
		solve.set(fin);
		fout<<"Case #"<<i<<": "<<solve.cheat()<<" "<<solve.honest()<<endl;
	}
	fin.close();
}