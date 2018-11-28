#include<iostream>
#include<map>
#include<fstream>
#include<string>
using namespace std;
int main(){
	int t,i=1;
	unsigned long long int N,ans=-1;
	string str;
	ifstream inf("C:\\Users\\shyam gupta\\Downloads\\A-large.in");
	ofstream outf;
	outf.open("C:\\Users\\shyam gupta\\\Downloads\\output.txt");
	inf>>t;
	map<unsigned long long int,unsigned long long int> m;
	map<unsigned long long int,unsigned long long int>::iterator it;
	getline(inf,str);
	while(t--){
		inf>>N;
		getline(inf,str);
		if(N==0){
			ans=-1;
		}
		else{
			unsigned long long int x=1,y;
			while(m.size()!=10){
				y=x*N;
				while(y!=0){
					unsigned long long int z=y%10;
					it=m.find(z);
					if(it==m.end()){
						m[z]=z;
					}
					y=y/10;
				}
				++x;
			}
			ans=(x-1)*N;
		}
		outf<<"Case #"<<i<<":"<<" ";
		if(ans==-1){
			outf<<"INSOMNIA"<<endl;
		}
		else{
			outf<<ans<<endl;
		}
		++i;
		m.clear();
	}
	inf.close();
	outf.close();
	return 0;
}
