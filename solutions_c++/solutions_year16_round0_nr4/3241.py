#include <iostream>
#include <fstream>
using namespace std;
typedef long long int lli;
int l;



int main(){
	ios_base::sync_with_stdio(false);
	ifstream in;
	in.open("in.txt");
	ofstream out;
	out.open("out.txt");
	int t;
	in>>t;
	for(int i=1;i<=t;i++){
		out<<"Case #"<<i<<": ";
		lli k,c,s;
		in>>k>>c>>s;
		if(s<k-1||(c==1 && s<k)){
			out<<"IMPOSSIBLE"<<endl;
		}

		else{
			if(s==k){
				for(int i=1;i<=s;i++)
					out<<i<<" ";
				out<<endl;
			}
			else{
				if(c==1){
					out<<1<<" ";
					s-=1;
				}
				for(int j=2;j<=(s+1);j++)
					out<<j<<" ";
				out<<endl;
			}
		}
	}
	return 0;
}
