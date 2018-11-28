#include<iostream>
#include<fstream>
using namespace std;

int main(){
ifstream fin;
fin.open("A-small-attempt5.in");
ofstream fout;
fout.open("OUTPUT1.txt");
int t;
fin>>t;
int len,count,ans;
char str[1000];
for(int i=0;i<t;i++){
	count=ans=0;
	fin>>len;
	fin>>str;
	for(int j=0;j<=len;j++){
		
		if(count<j){
			ans+=(j-count);
			count+=(j-count);
		}
		count+=str[j]-'0';
		
	}
	fout<<"Case #"<<i+1<<": "<<ans<<"\n";	
}
}
