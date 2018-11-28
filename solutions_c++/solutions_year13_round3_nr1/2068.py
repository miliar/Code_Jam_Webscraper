#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

bool IsCon(char t){
	if(t!='a' && t!='e' && t!='i' && t!='o' && t!='u')
		return true;
	return false;
}

bool IsConCon(unsigned long long n,unsigned long long i,string tmp){
	unsigned long long LN=tmp.length(),EN=n+i;
	if(EN>LN)
		return false;
	for(unsigned long long j=0;j<n;j++){
		char t=tmp.at(i+j);
		if(!IsCon(t))
			return false;
	}
	return true;
}

unsigned long long n_value(unsigned long long n,string tmp){
	unsigned long long LN=tmp.length(),a,b,nv=0;
	for(unsigned long long i=0;i<LN;i++){
		a=i;b=LN-i-n;
		if(IsConCon(n,i,tmp)){
			for(unsigned long long j=i+1;j<LN;j++){
				if(IsConCon(n,j,tmp)){
					b=j-i-1;
					break;
				}
			}
			//cout<<tmp<<" "<<i<<" "<<a<<" "<<b<<endl;
			nv+=(a+1)*(b+1);
		}
	}
	return nv;
}

int main(){
	ifstream inp;
	ofstream out;
	out.open("d:/out.txt");
	inp.open("d:/a.in");
	int T;
	inp>>T;
	for(int z=1;z<=T;z++){
		unsigned long long n,ans;
		string tmp;
		inp>>tmp>>n;
		ans=n_value(n,tmp);
		cout<<"Case #"<<z<<": "<<ans<<endl;
		out<<"Case #"<<z<<": "<<ans<<endl;
	}
	system("pause");
	return 0;
}