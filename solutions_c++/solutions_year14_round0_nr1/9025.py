#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;
int main(){
	int t1;
	cin>>t1;
	for(int ty1=0;ty1<t1;ty1++){
		int x1,y1,a1[16],b1[16];
		cin>>x1;
		for(int i=0;i<16;i++){
			cin>>a1[i];
		}
		cin>>y1;
		for(int i=0;i<16;i++){
			cin>>b1[i];
		}
		int count1=0;
		int num1=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(a1[4*x1+i-4]==b1[4*y1+j-4]){
					
					count1++;
					num1=a1[4*x1+i-4];
				}
			}
		}
		if(count1==1) cout<<"Case #"<<ty1+1<<": "<<num1<<endl;
		if(count1>=2) cout<<"Case #"<<ty1+1<<": Bad magician!"<<endl;
		if(count1==0) cout<<"Case #"<<ty1+1<<": Volunteer cheated!"<<endl;
	}
}
