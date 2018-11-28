#include<iostream>
using namespace std;
#include<fstream>
#define DEBUG 0
#if DEBUG
#define cin inp
#define cout out
#endif
int main(){
long long int t,a,b,c;
fstream inp("inp.txt"),out("out.txt");
cin>>t;
int cc=1;
while(t--){
		cin>>a>>b>>c;
		int ct=0;
		for(int i=0;i<a;i++)
			for(int j=0;j<b;j++)
				{
					//cout<<i<<" "<<j<<" TEST "<<(i&j)<<endl;
				if((i&j) < c)ct++;//,cout<<i<<" "<<j<<endl;
			}
		cout<<"Case #"<<cc++<<": "<<ct<<endl;
}	
}
