#include<iostream>
#include<cstdio>
#include<fstream>
#include <iomanip>
using namespace std;

ofstream myfile;

int main(){
	myfile.open ("output.txt");
	int t,i;
	int number=1;
	double c,f,x,megha,ans=0,dist,dist1,gupta;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		cin>>c>>f>>x;
		megha=0;
		dist=2.0;
		dist1=dist;
		ans=0;
		dist=dist+f;
		gupta=x-c;
		while(megha!=10){
			if((x/dist)<(gupta/dist1)){
				ans=ans+c/dist1;
				//cout<<"first"<<endl;
			}
			else{
				ans=ans+x/dist1;
				megha=10;
				//cout<<"Secound"<<endl;
			}
			dist=dist+f;
			dist1=dist-f;
		}
		myfile<<"Case #"<<number<<": "<<setprecision(7)<< fixed <<ans<<endl;
		number++;
	}
}
