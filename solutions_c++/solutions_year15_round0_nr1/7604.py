#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("gcj1-large.out");
	
	int N=0;
	fin>>N;
	
	for(int i=0;i<N;i++){
		int ans=0;
		int max=0;
		string str;
		fin>>max;
		fin>>str;
		
		int acu=0;
		for(int j=0;j<=max;j++){
			if(str[j]=='0');
			else{
				if(j>acu){
					ans+=j-acu;
					acu+=j-acu;
				}
			}
			
			acu+=(int)(str[j]-'0');
		}
		
		cout<<"Case #"<<i+1<<": ";
		cout<<ans;
		cout<<endl;
		
		fout<<"Case #"<<i+1<<": ";
		fout<<ans;
		fout<<endl;
	}
}