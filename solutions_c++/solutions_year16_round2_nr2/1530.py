#include<iostream>
#include<deque>
#include<algorithm>
#include<fstream>
#include<cmath>
#include<math.h>
#include<vector>
#include <stdlib.h>  
#include<string>
using namespace std;
	string one,two;
		int x;
		deque<string> first,second;
		void onegen(string now){
			if(now.size()==one.size()){
				first.push_back(now);
				//cout<<"ok"<<now<<endl;
				return;
			}
			int i=now.size();
			if(one[i]=='?'){
				now.push_back(' ');
				for(int j=0;j<10;j++){
					now[i]=(char)(j+48);
					onegen(now);
				}
			}else{
				now.push_back(one[i]);
			//	cout<<now<<endl;
				onegen(now);
			}
		}
			void twogen(string now){
			if(now.size()==two.size()){
				second.push_back(now);
				return;
			}
			int i=now.size();
			if(two[i]=='?'){
				now.push_back(' ');
				for(int j=0;j<10;j++){
					now[i]=(char)(j+48);
					twogen(now);
				}
			}else{
				now.push_back(two[i]);
				twogen(now);
			}
		}
		int check(long long int r,long long int t){
			if(r>t){
				return r-t;
			}else{
				return t-r;
			}
		}
int cmp(string q,string w){
long long 	int numone=0,numtwo=0;
	long long int i=1;
	for(int j=q.size()-1;j>=0;j--){
		numone+=(i*((int)q[j]-48));
			numtwo+=(i*((int)w[j]-48));
			i*=10;
	}
//	cout<<i<<endl;
	return check(numone,numtwo);
}
int main (){
	ifstream cin("Bsmall.in");
	ofstream cout("AE.txt");
string outputone,outputtwo;
	cin>>x;
long long int large=0;
	for(int i=1;i<=x;i++){
		cin>>one>>two;
		large=9223372036854775806;
		cout<<"Case #"<<i<<": ";
		string now="";
		onegen(now);
		twogen(now);
		//cout<<first.size()<<second.size()<<endl;
		for(int j=0;j<first.size();j++){
			for(int k=0;k<second.size();k++){
				//cout<<cmp(first[j],second[k]);
				if(cmp(first[j],second[k])<large){
					large=cmp(first[j],second[k]);
					outputone=first[j];
					outputtwo=second[k];
				}
			}
		}
		while(first.size()!=0){
			first.pop_front();
		}while(second.size()!=0){
			second.pop_front();
		}
		cout<<outputone<<" "<<outputtwo<<endl;
	}
}
