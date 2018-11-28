#include<cstdio>
#include<iostream>
#include<map>
#include<string>
using namespace std;

void MagicTrick(){
	int t;
	cin>>t;
	int f[5][5], e[5][5];
	for (int cases=1; cases<=t; cases++) {
		int a;
		cin>>a;
		for (int i=1; i<=4; i++) 
			for (int j=1; j<=4; j++)
				cin>>f[i][j];
		int b;
		cin>>b;
		for (int i=1; i<=4; i++) 
			for (int j=1; j<=4; j++)
				cin>>e[i][j];
		int count = 0;
		int val;
		for (int j=1; j<=4; j++)
			for (int k=1;k<=4;k++)
				if (f[a][j] == e[b][k]){
					count++;
					val = f[a][j];
				}
		cout<<"Case #"<<cases<<": ";
		if (count==0) cout<<"Volunteer cheated!"<<endl;
		else if (count == 1) cout<<val<<endl;
		else cout<<"Bad magician!"<<endl;
	}
};


int main() {
	freopen("D:\\A-small-attempt0.in","r",stdin);
	freopen("D:\\A.out","w",stdout);
    MagicTrick();
    return 0;
}
