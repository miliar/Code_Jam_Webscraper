#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <stdio.h>
using namespace std;

int main(){
	int n,x,y;
	string linex,liney;
	vector<int> vx(4),vy(4);
	string temp;
	cin>>n;
	int num=1;
	while(num<=n){
		cin>>x;
		getchar();
		//cout<<endl<<"x: "<<x<<endl;
		for(int i=1;i<=4;i++){
			if(i==x){
				getline(cin,linex);
				//cout<<"i: "<<linex<<endl;
			}
			else{
				getline(cin,temp);
				//cout<<"i: "<<temp<<endl;
			}
		}
		cin>>y;
		getchar();
		//cout<<endl<<"y: "<<y<<endl;
		for(int i=1;i<=4;i++){
			if(i==y){
				getline(cin,liney);
				//cout<<"i: "<<liney<<endl;
			}
			else{
				getline(cin,temp);
				//cout<<"i: "<<temp<<endl;
			}
		}
		stringstream strmx(linex);
		stringstream strmy(liney);
		//cout<<endl<<linex<<"  !!!  "<<liney<<"  !!! "<<endl;

		int a,b;
		for(int i=0;i<4;i++){
			strmx>>a;
			strmy>>b;
			vx[i]=a;
			vy[i]=b;
		}
		int count=0;
		int magic;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(vx[i]==vy[j]){
					magic=vx[i];
					count++;
				}
			}
		}
		if(count==1)
			cout<<"Case #"<<num<<": "<<magic<<endl;
		else if(count>1)
			cout<<"Case #"<<num<<": Bad magician!"<<endl;
		else
			cout<<"Case #"<<num<<": Volunteer cheated!"<<endl;
		++num;
	}
}