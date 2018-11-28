#include<iostream>
#include<sstream>
#include<cstring>
#include<fstream>
#include<cmath>
using namespace std;

stringstream ss;
ifstream File("A-small-attempt0 (1).in");
ofstream oFile("output.io");
int main(){
	unsigned long long int j=0,ca=0,cr=0,pa=0,tca=0;
	unsigned long long int i=0,ir=0,it=0,tc=0;
	File>>tc;
	for(int k=0;k<tc;k++){
		i=0,j=0,ca=0,cr=0,pa=0,tca=0,ir=0,it=0;
		File>>ir>>it;
		cr=ir;
		ca=cr*cr;
		i=0;
		//cout<<"Cur Area: "<<ca<<", "<<cr<<", Remaining it: "<<it<<endl;
		for(j=0;;j++){
			pa=ca;
		//	cout<<"ca:"<<ca<<"::tca:"<<tca<<"::cr:"<<cr<<"::it:"<<it<<endl;
			cr++;
			ca=(cr*cr);
			tca=ca-pa;
			if(j % 2==0){
				if(tca>it)break;
			//	cout<<cr<<":entered"<<endl;
				it-=tca;
				i++;
				//cout<<"ca:"<<ca<<"::tca:"<<tca<<"::cr:"<<cr<<"::it:"<<it<<endl;
			}
			//cout<<"ca:"<<ca<<"tCA: "<<tca<<", CR: "<<cr<<", Remaining it: "<<it<<endl;
		}
		oFile<<"Case #"<<k+1<<": "<<i<<endl;
	}
	
    //system("pause");
    return 0;
}
