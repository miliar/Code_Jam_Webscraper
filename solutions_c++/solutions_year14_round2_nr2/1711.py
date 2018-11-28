#include<fstream>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int T,A,B,K,i,j;
	fin>>T;
	for(int times=1;times<=T;times++){
		fin>>A>>B>>K;
		int ans=0;
		for(i=0;i<A;i++){
			for(j=0;j<B;j++){
				if((i&j)<K)
					ans++;
			}
		}
		fout<<"Case #"<<times<<": "<<ans<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}