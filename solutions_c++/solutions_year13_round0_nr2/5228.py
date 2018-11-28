#include<iostream>

using namespace std;

const int MAXN = 100 + 3;

int T;
int N,M,a[MAXN][MAXN];
bool rowsk[MAXN],colsk[MAXN];
int dim[2];
bool done;
bool can;

int findMin() {
	int min = MAXN;
	for(int i=0;i<N;i++) {
		if(rowsk[i])	continue;
		for(int j=0;j<M;j++) {
			if(colsk[j])	continue;
			if(a[i][j]<min) min = a[i][j];
		}
	}
	return min;
}

void reduce() {
	int min = findMin();
	bool reduced = 0;
	//rows
	for(int i=0;i<N;i++) {
		if(rowsk[i])	continue;
		bool rowcan = 1;
		for(int j=0;j<M;j++) {
			if(colsk[j])	continue;
			if(a[i][j] != min) rowcan = 0;
		}
		if(rowcan) {rowsk[i] = 1; reduced = 1; dim[0]--;}
	}
	//cols
	for(int j=0;j<M;j++) {
		if(colsk[j])	continue;
		bool colcan = 1;
		for(int i=0;i<N;i++) {
			if(rowsk[i])	continue;
			if(a[i][j] != min) colcan = 0;
		}
		if(colcan) {colsk[j] = 1; reduced = 1; dim[1]--;}
	}
	
	if(!reduced || dim[0]<2 || dim[1]<2) done = 1;
	if(dim[0]<2 || dim[1]<2) can = 1;
}
int main() {
	cin>>T;
	for(int ti=0;ti<T;ti++) {
		//init
		cin>>N>>M;
		dim[0]=N;
		dim[1]=M;
		done = 0;
		can = 0;
		for(int i=0;i<N;i++)
			rowsk[i]=0;
		for(int i=0;i<M;i++)
			colsk[i]=0;
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				cin>>a[i][j];
			
		while(!done)
			reduce();
		
		cout<<"Case #"<<ti+1<<": ";
		if(can) cout<<"YES"<<endl;
		else	cout<<"NO"<<endl;
	}
	return 0;
}