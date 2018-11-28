#include<iostream>
#include<cstdlib>
using namespace std;

int main(){
	int testCase;
	cin>>testCase;
	for (int i=0;i<testCase;i++){
		int shyLvl;
		string jmlShy;
		cin>>shyLvl;
		cin>>jmlShy;
		int total=0;
		int teman=0;
		for (int j=0;j<=shyLvl;j++){
			int q= jmlShy[j] - '0';
			if ((total<j)&&(q!=0)){
				teman+=j-total;
				total+=teman+q;
			} else {
				total+=q;
			}
		}
		cout<<"Case #"<<i+1<<": "<<teman<<endl;
	}
}

