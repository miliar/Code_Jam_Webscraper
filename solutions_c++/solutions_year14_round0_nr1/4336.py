#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int ty=0;ty<t;ty++){
		int x,y,a[16],b[16];
		cin>>x;
		for(int i=0;i<16;i++){
			cin>>a[i];
		}
		cin>>y;
		for(int i=0;i<16;i++){
			cin>>b[i];
		}
		int count=0;
		int num=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(a[4*x+i-4]==b[4*y+j-4]){
					//cout<<"here "<<ty<<" "<<i<<" "<<j<<" "<<x<<" "<<y<<endl;
					count++;
					num=a[4*x+i-4];
				}
			}
		}
		if(count==1) cout<<"Case #"<<ty+1<<": "<<num<<endl;
		if(count>1) cout<<"Case #"<<ty+1<<": Bad magician!"<<endl;
		if(count==0) cout<<"Case #"<<ty+1<<": Volunteer cheated!"<<endl;
	}
}
