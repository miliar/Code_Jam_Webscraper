#include<bits/stdc++.h>
#define ll unsigned long long int

using namespace std;

bool d[11];

int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	ll t,n,i,c,m,z = 0;
	fin>>t;
	while(t--){
		fout<<"Case #"<<++z<<": ";
		memset(d,0,sizeof(d));
		fin>>n;
		if(n==0){
			fout<<"INSOMNIA"<<endl;
			continue ;
		}
		i = 1;c = 0;
		while(c != 10){
			m = i*n;
			while(m){
				if(d[m%10]==0){
					++c;d[m%10] = 1;
				}
				m/=10;
			}
			++i;
		}
		fout<<(i-1)*n<<endl;
	}
	return 0;
}
