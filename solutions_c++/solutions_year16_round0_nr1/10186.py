#include<iostream>
#include<fstream>
using namespace std;
int main(){
	ifstream file;
	file.open("A-large.in");
	ofstream out;
	out.open("656E.txt");
	int t;
	file >> t;
	for(int j=0; j<t ;j++){
		int app[10];
		for(int i=0; i<10 ;i++){
			app[i]=0;
		}
		int cnt=10;
		string n;
		int dig[10],tem[10];
		file >> n;
		if(n=="0"){
			out << "Case #" << j+1 << ": ";
			out << "INSOMNIA\n";
			continue;
		}
		for(int i=0; i<10 ;i++){
			dig[i]=0;
		}
		for(int i=0; i<n.size() ;i++){
			dig[n.size()-i-1]=n[i]-48;
			if(app[dig[n.size()-i-1]]==0){
				app[dig[n.size()-i-1]]=1;
				cnt--;
			}
		}
		for(int i=0; i<10 ;i++){
			tem[i]=dig[i];
		}
		int len=n.size();
		while(cnt!=0){
			for(int i=0; i<10 ;i++){
				dig[i]+=tem[i];
			}
			for(int i=1; i<10 ;i++){
				dig[i]+=dig[i-1]/10;
				dig[i-1]%=10;
			}
			if(dig[len]!=0){
				len++;
			}
			for(int i=0; i<len ;i++){
				if(app[dig[i]]==0){
					app[dig[i]]=1;
					cnt--;
				}
			}
		}
		out << "Case #" << j+1 << ": ";
 		bool fz=false;
		for(int i=9; i>=0 ;i--){
			if(dig[i]!=0){
				out << dig[i];
				fz=true;
			}
			else if(fz){
				out << dig[i];
			}
		}
		out << endl;
	}
}
