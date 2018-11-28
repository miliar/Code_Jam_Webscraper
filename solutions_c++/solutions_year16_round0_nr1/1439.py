#include<fstream>

using namespace std;
int main(){
	long long int n;
	long long int in;
	ifstream is;
	is.open("A-large.in");
	ofstream os;
	os.open("outA.txt");
	is>>n;
	bool flag, a[10];
	long long int j;
	for(int i=0; i<n ; i++){
		is>>in;
		if(in==0) os<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		else{
			flag = false;
			for(j=0;j<10;j++)	a[j]=false;
			for(j=1; !flag; j++){
				for(int k=in*j; k>0;k/=10 ){
					a[k%10] = true;
				}
				if(a[0] && a[1] && a[2] && a[3] && a[4] && a[5] && a[6] && a[7] && a[8] && a[9]) flag = true;
			}
			os<<"Case #"<<i+1<<": "<<in*(j-1)<<endl;
		}
	}
	return 0;
}

