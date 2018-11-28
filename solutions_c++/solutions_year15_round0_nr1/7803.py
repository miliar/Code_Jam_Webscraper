#include<iostream>
#include<fstream>
using namespace std;

int main(){
	ifstream f("input.txt");
	ofstream of;
	of.open("output.txt");
	int T;
	f>>T;
	int count =1;
	while(T--){
		int S, c=0, inp, res=0;
		string str;
		f>>S;
		f>>str;
		for(int i = 0;i<=S;i++){
			if(res<(i-c))
			res=(i-c);
			c+= (int) (str[i]-48);
			//of<<res;
		}
		of<<"Case #"<<count<<": "<<res<<"\n";
		count++;
	}
	return 1;
}
