#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream out("A-large.out");
   	ifstream in("A-large.in");
	int t,sum,u,n,o=1;
	char aux;
	in>>t;
	while(t--){
		in>>n;
		sum=u=0;
		for(int i=0;i<=n;i++){
			in>>aux;
			if(u<i){
				sum+=(i-u);
				u=i;
			}
			u+=aux-48;
		}
		out<<"Case #"<<o++<<": "<<sum<<endl;
	}
	out.close();
   	in.close();
	return 0;
}
