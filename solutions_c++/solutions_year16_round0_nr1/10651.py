// basic file operations
#include <iostream>
#include <fstream>
using namespace std;
int dig[10] = {0,0,0,0,0,0,0,0,0,0};
bool checkdig(){
	for(int i=0; i<10; i++){
		if(dig[i]==0){
			return false;
		}
	}
	return true;
};
int main () {
	ifstream infile;
	infile.open("A-large.in.txt");

	ofstream outfile;
	outfile.open ("A-large.out.txt");
	
	int T;
	infile >> T;
	for(int i=0; i<T; i++){
		long long N;
		infile >> N;
		outfile << "Case #"<<i+1<<": ";
		if(N!=0){
			bool ch = false;
			long long temp = N;
			int j = 1;
			while(ch==false){
				cout<<temp<<"-";
				while(temp>0){
					int d = temp%10;
					temp = temp/10;
					dig[d] = 1;
				}
				ch = checkdig();
				cout<<ch<<endl;
				if(ch==false){
					j++;
					temp = j*N;
				}
			}
			outfile <<j*N<<"";
		}else{
			outfile << "INSOMNIA";
		}
	  	outfile<<endl;
	  	for(int i=0; i<10; i++){
			dig[i]=0;
		}
	}
	infile.close();
	outfile.close();
  return 0;
}