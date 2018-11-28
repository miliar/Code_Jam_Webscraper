#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
int main(){
	ifstream in;
	string ss;
	cin>>ss;
	in.open(ss.c_str());
	int t;
	in>>t;
	string asd[t];
	
	for(int i = 0;i<t;i++){
		string s="RICHARD";
		int x,r,c;
		in>>x>>r>>c;
		if(x==1) s="GABRIEL";
		else if (x==2) {
			if(r*c%2==0) s="GABRIEL";
		}
		else if (x==3)
		{
			if (r>=2&&c>=2)
			{
				if( r>=3 || c>=3 )
				{
					if(r*c%3==0) s="GABRIEL";
				}
			}
		}
		else if (x==4)
		{
			if(r>=3 && c>=3)
			{
				if(r>=4 || c >= 4 )
				{
					s="GABRIEL";
				}
			}
		}
		asd[i]=s;
	}
	ofstream out;
	string outFile="test.out";
	out.open(outFile.c_str());
	for(int i=0;i<t;i++){
		out<<"Case #"<<i+1<<": "<< asd[i]<<"\n";
	}
	return 0;
}
