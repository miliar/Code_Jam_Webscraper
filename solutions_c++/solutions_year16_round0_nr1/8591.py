#include<bits/stdc++.h>
using namespace std;
set<int> s;
#define ull unsigned long long int
void fn(ull a){
	while(a>0){
		int temp=a%10;
		s.insert(temp);
		a/=10;
	}
}
int main()
{
	int T;
	ifstream fin ("input.txt");        
  	ofstream fout("A-small-practice.out");  
	fin>>T;
	for(int t=1;t<=T;t++){
		ull a;
		fin>>a;
		fout<<"Case #"<<t<<": ";
		if(a!=0){
			s.clear();
			ull i=1,temp;
			while(s.size()!=10){
				temp=a*i;
				fn(temp);
				i++;
			}
			fout<<temp<<"\n";
		}
		else{
			fout<<"INSOMNIA\n";
		}
	}
}
