#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main()
{
	int n,N;
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	
	fin>>N;

	for(n=0;n<N;n++){
		int S;
		string ss;
		fin>>S>>ss;
		int res = 0;
		int count = ss[0] - '0';
		
		for(int i=1;i<=S;i++){
			if(count < i){
				res++;
				count++;
			}
			count += ss[i]-'0';			
		}
		
		fout<<"Case #"<<n+1<<": "<<res<<endl;
	}


	return 0;
}