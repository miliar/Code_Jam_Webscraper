
//Problem B. Lawnmower

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <cmath>

using namespace std;

int n,m;
int field[20][20];
int check[20][20];

int rowmax(int index){
	int max=0;
	for (int i=0;i<m;i++)
		if (field[index][i]>max) max=field[index][i];
	return max;
}

int colmax(int index){
	int max=0;
	for (int i=0;i<n;i++)
		if (field[i][index]>max) max=field[i][index];
	return max;
}

int compute(){
	int i,j,k;
	int res=1;
	
	for (i=0;i<n;i++){
		k=rowmax(i);
		for (j=0;j<m;j++)
			if (field[i][j]==k) check[i][j]=1;
	}
	for (i=0;i<m;i++){
		k=colmax(i);
		for (j=0;j<n;j++)
			if (field[j][i]==k) check[j][i]=1;
	}
	k=0;
	for (i=0;i<n;i++)
		for (j=0;j<m;j++)
			if (check[i][j]==1) k++;

	if (k==n*m) res=1;
	else res=0;
	return res;
}

int main(){
	int t;
	int i,j,k;
	
	cin>>t;
	for (i=0;i<t;i++){
		cin>>n>>m;
		for (j=0;j<n;j++)
			for (k=0;k<m;k++) {
				cin>>field[j][k];
				check[j][k]=0;
			}
			
		k=compute();
		cout<<"Case #"<<(i+1)<<": ";
		if (k==0) cout<<"NO";
		else cout<<"YES";
		cout<<endl;
	}
}
