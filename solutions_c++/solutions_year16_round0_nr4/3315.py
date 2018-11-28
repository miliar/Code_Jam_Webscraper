#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int t,i=1;
	unsigned long long int k,c,s;
	string str;
	ifstream inf("C:\\Users\\shyam gupta\\Downloads\\D-small-attempt0.in");
	ofstream outf;
	outf.open("C:\\Users\\shyam gupta\\\Downloads\\output.txt");
	inf>>t;
	getline(inf,str);
	while(t--){
		inf>>k>>c>>s;
	//	unsigned long long int z=pow(k,c);
	//	z=z/k;
		getline(inf,str);
		outf<<"Case #"<<i<<":"<<" ";
		if(c==1){
			if(s<k)
			outf<<"IMPOSSIBLE"<<endl;
			else{
				for(int j=1;j<=k;j++)
				outf<<j<<" ";
				outf<<endl;
			}
			
		}
		else{
		if(s>=k){
			for(int j=1;j<=k;j++)
				outf<<j<<" ";
				outf<<endl;
		}
		else{
				
		}
	}
		++i;
	}
	inf.close();
	outf.close();
}
