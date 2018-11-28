#include<fstream>
#include<string>

using namespace std;

int main(){
	ifstream fin("inp.txt");
	ofstream fout("out.txt");
	int t;
	fin>>t;
	for(int c=1;c<=t;c++){
		string str;
		fin>>str;
		int n=str.length(),i,j,move=0;
		while(1){
			if(str[0]=='+'){
				i=1;
				while(i<n && str[i]=='+')
					i++;
				if(i==n)
					break;
				move++;
				for(j=0;j<i;j++)
					str[j]='-';
			}
			else{
				i=1;
				while(i<n && str[i]=='-')
					i++;
				if(i==n){
					move++;
					break;
				}
				move++;
				for(j=0;j<i;j++)
					str[j]='+';
			}
		}
		fout<<"Case #"<<c<<": "<<move<<"\n";
	}
}