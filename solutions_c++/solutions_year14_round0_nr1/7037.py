#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(){
	int cases,p,count,t,a[4],v;
	cin>>cases;
	string s;
	for(int i=0;i<cases;i++){
		count=0;
		cin>>p;
		for(int j=0;j<4;j++){
			if(j+1==p) cin>>a[0]>>a[1]>>a[2]>>a[3];
			else{
				 cin.ignore();
				 getline(cin,s);
			}
		}
		cin>>p;
		for(int j=0;j<4;j++){
			if(j+1==p){
				for(int k=0;k<4;k++){
					cin>>t;
					int *foo =find(a,a+4,t);
					if(foo!=a+4){
						count++;
						v=*foo;
					}
				}
			}
			else{
				 cin.ignore();
				 getline(cin,s);
			 }
		}
		if(count>=2) cout << "Case #"<<i+1<<": Bad magician!\n";
		if(count==1) cout << "Case #"<<i+1<<": "<<v<<endl;
		if(count==0) cout << "Case #"<<i+1<<": Volunteer cheated!\n";
	}
}
