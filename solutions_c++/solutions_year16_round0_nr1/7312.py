#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

int flag[10];
int chk(){
	for(int i=0;i<10;i++){
		if(flag[i]==0)
			return 1;
	}
	return 0;
}
int main() {
	ofstream out;
	ifstream in;
	
	out.open("a.out");
	
	in.open("a.in");
	
	int t,T;
	in>>T;
	for(t=0;t<T;t++){
		long long int n,mul=1,num,val,test=1;
		in>>n;
		if(n==0){
			out<<"Case #"<<t+1<<": "<<"INSOMNIA\n";continue;
		}
		num=n;
		memset(flag,0,sizeof(flag));
		while(chk()){
			
			while(num){
				val=num%10;
				num/=10;
				flag[val]=1;
//				cout<<val<<" ";
			}
			mul++;
			num=n*mul;
		//	cout<<"\n"<<num<<endl;
		}
		out<<"Case #"<<t+1<<": "<<(mul-1)*n<<endl;
	}
	return 0;
}
