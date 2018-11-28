#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<fstream>
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define fora(i,a,b) for(int i=a;i<(int)b;i++)
#define p(p) cout<<"Test: "<<p<<"\n";
using namespace std;
int main(){
	int a,b,c,t,flag=0;
	ifstream fin;
	fin.open("Omino.in");
	ofstream fout;
	fout.open("Omino.txt");
	fin>>t;
	string result;
	forn(it,t){
		result="";
		flag=0;
		fin>>a>>b>>c;
		if(b*c%a!=0){
			result="RICHARD";
			goto pri;
		}
		if(a==1){
			result="GABRIEL";
			goto pri;
		}
		if(a==2){
			if(b*c<2){
				result="RICHARD";
				goto pri;
			}
		}
		else if(a==3){
			if(b<2 || c<2){
				result="RICHARD";
				goto pri;
			}
		}
		else if(a==4){
			if(b<=2 || c<=2){
				result="RICHARD";
				goto pri;
			}
		}
		result = "GABRIEL";
		pri:
		if(it==0){
			fout<<"Case #"<<it+1<<": "<<result;
		}
		else{
			fout<<endl<<"Case #"<<it+1<<": "<<result;
		}
	}
}