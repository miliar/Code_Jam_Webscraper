#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

int map[100][100];
int T,n,m;
bool mark1,mark2;

int main(){
	freopen("B-large.in","r",stdin);freopen("std.out","w",stdout);
	cin>>T;
	for (int h=1;h<=T;h++){
		cin>>n>>m;
		cout<<"Case #"<<h<<": "; 
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++) cin>>map[i][j];
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++){
				mark1=false;mark2=false;
				for (int k=0;k<n;k++)
					if (map[i][j]<map[k][j]) {mark1=true;break;}
				for (int k=0;k<m;k++)
					if (map[i][j]<map[i][k]) {mark2=true;break;}
				if (mark1 && mark2) {cout<<"NO"<<endl;goto a;}
			}
		cout<<"YES"<<endl;
	a:	continue;
	}
	return 0;
}
