#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<algorithm>
#include<math.h>
#include <iomanip>
using namespace std;
int main(){
int t1,l=1;
cin>>t1;
while(t1--){
	int x,y,count=0,pos;
	int a[4][4],b[4][4];
	cin>>x;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++)
		cin>>a[i][j];
	}
	
	cin>>y;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++)
		cin>>b[i][j];
	}
	
	x--;
	y--;
	

	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(a[x][i]==b[y][j]){
			pos=a[x][i];
			count++;
			}
		}
		if(count>1)
		break;
	}
if(count==0)
cout<<"Case #"<<l<<": "<<"Volunteer cheated!\n";
else if(count==1)
cout<<"Case #"<<l<<": "<<pos<<"\n";
else
cout<<"Case #"<<l<<": "<<"Bad magician!\n";
l++;
	
}

system("pause");
  return 0;
}

