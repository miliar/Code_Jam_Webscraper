#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<fstream>
#include<map>   
using namespace std;

int a[200][200];
int r,c;

bool check(int x,int y){

	bool okv=true,okh=true;

	for(int i=0;i<c;i++){
		if(a[x][i]>a[x][y]) okv=false;
	}

	for(int i=0;i<r;i++){
		if(a[i][y]>a[x][y]) okh=false;
	}

	return (okv || okh);

}

int main(){
	ifstream cin;
	ofstream cout;
	cin.open("B-large.in");
	cout.open("out.txt");
	int n;
	cin>>n;
	for(int k=0;k<n;k++){
		cin>>r>>c;
		for(int i=0;i<r;i++) for(int j=0;j<c;j++) cin>>a[i][j];
		bool OK=true;
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++) {
				OK=(OK && check(i,j));
			}
		cout<<"Case #"<<k+1<<": ";
		if(OK) cout<<"YES";
		else cout<<"NO";

		cout<<endl;

	

	}





	return 0;

}


