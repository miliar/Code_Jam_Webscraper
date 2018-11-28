#include<stdio.h>
#include<stdlib.h>
#include<fstream>

using namespace std;

int main(){
int t,smax,val, sum, rez;
string s;
ifstream in; ofstream out;
in.open("A-large.in"); out.open("test.out");
out.clear();

in>>t;
for(int i=1;i<=t;i++){
	in>>smax>>s;
	sum=0; rez=0;
	for(int j=0;j<=smax;j++){
		val=s[j]-'0';
		if(sum<j){
		 rez=rez+(j-sum);
		 sum=sum+(j-sum);	
		} 
		sum=sum+val;
	}
	out<<"Case #"<<i<<": "<<rez<<endl;
}

 
in.close(); out.close();	
return 0;	
}

