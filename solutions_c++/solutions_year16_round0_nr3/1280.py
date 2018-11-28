#include<fstream>
using namespace std;

int main(){
	int n, j, t;
	ifstream is;
	is.open("C-large.in");
	ofstream os;
	os.open("outC.txt");
	is>>t;
	for(int i=0; i<t; i++){
		os<<"Case #"<<i+1<<": "<<endl;
		is>>n>>j;
		int resp = 0;
		for(int a=0; resp<j; a+=2){
			for (int ini = 0; ini<n-a-2 && resp<j; ini++){
				for(int spc=1; spc<n-a-2-ini  && resp<j; spc+=2){
					os<<1;
					for(int b=0;b<a;b++) os<<1;
					for(int b = a; b< n-2; b++){
						if(b==ini+a) os<<1;
						else if(b==a+ini+spc)os<<1;
						else os<<0;
					}
					os<<1<<" ";
					os<<3<<" "<<2<<" "<<5<<" "<<2<<" "<<7<<" "<<2<<" "<<3<<" "<<2<<" "<<11<<endl;
					resp++;
				}
			}
		}
	}
	return 0;
}



