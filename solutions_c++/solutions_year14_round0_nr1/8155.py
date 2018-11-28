#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
int a[4][4];
int b[4][4];
int cuenta[17];

int main(){
	int tc;	
	cin>>tc;
	
	for(int caso=1;caso<=tc;caso++){
		cout<<"Case #"<<caso<<": ";
		int f1;
		cin>>f1;
		f1--;
		memset(cuenta,0,sizeof(cuenta));
		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>a[i][j];
		
		int f2;
		cin>>f2;
		f2--;
		
		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>b[i][j];
		
		
		for(int i=0;i<4;i++){
			cuenta[a[f1][i]]++;
			cuenta[b[f2][i]]++;
		}
		
		int tot=0;int num=-1;
		for(int i=1;i<=16;i++){
			if(cuenta[i]==2){
				tot++;
				num=i;	
			}
		}
		
		if(tot==0){
			cout<<"Volunteer cheated!"<<endl;
		}
		
		if(tot==1){
			cout<<num<<endl;
		}
		
		if(tot>1){
			cout<<"Bad magician!"<<endl;
		}
		
		
	}
	
    return 0;
}


