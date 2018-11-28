#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<stack>
using namespace std;
main(){
	ifstream in("A-small-attempt1.in");
	ofstream out("out.txt");
	int count=0;
	int add=0;
	int sum=0;
	int t;
	in>>t;
	for(int i=1;i<=t;i++){
		add=0;sum=0;
		stack <int> s;
		int x;int y,k;
		in >>x;
		in>>y;
		for(int j=0;j<=x;j++){
			k=y%10;
			y=y/10;
			s.push(k);
		}
		for(int j=0;j<=x;j++){
			k=s.top();
		    
			s.pop();
			if(sum>=j){
				sum+=k;
			}
			else{
			 add+=(j-sum);
			 sum+=(j-sum)+k;
		   }
		}
		out<<"Case #"<<i<<": "<<add<<endl;
	}
}
