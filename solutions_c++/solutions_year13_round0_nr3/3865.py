// fair.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>

using namespace std;


int main()
{
	int a,b,t,ans;
	//1,4,9,121,484
	ifstream fp;
	ofstream fout;
	fp.open("input.txt",ios::beg);
	fout.open("output.txt",ios::beg);
	fp >> t;
	
	
	

	for(int i=0;i<t;++i){
		ans=5;
		fp>>a;
		fp>>b;
		if(a>1)
			ans--;
		if(a>4)
			ans--;
		if(a>9)
			ans--;
		if(a>121)
			ans--;
		if(a>484)
			ans--;
		if(b<484)
			ans--;
		if(b<121)
			ans--;
		if(b<9)
			ans--;
		if(b<4)
			ans--;
		if(b<1)
			ans--;
		
		fout<<"Case #"<<i+1<<": "<<ans<<endl;
	}

		
	return 0;
}

