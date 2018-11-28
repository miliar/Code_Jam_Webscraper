#include<fstream>
using namespace std;

long long int reverse(long long int x){
	int y=0;
	while(x>0){
		y=y*10+x%10;
		x/=10;
	}
	return y;
}

int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T;
	in>>T;

	for(int t=1;t<=T;t++){
		long long int a,b;
		int count=0;
		in>>a>>b;

		for(long long int i=1;i*i<=b;i++){
			if(i==reverse(i) && i*i==reverse(i*i) && i*i>=a)
				count++;
		}
		out<<"Case #"<<t<<": "<<count<<endl;
	}

}