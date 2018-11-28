#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc , char* argv[]){
	ifstream in(argv[1],ios::in);
	ofstream out(argv[2],ios::out);
	
	int cases;
	in>>cases;
	int count=0;

	while(count<cases)
	{
		int A,B,K;
		in>>A ; in>>B; in>>K;
		int count1=0, count2=0;
		for(int i=0; i<A; i++)
			for(int j=0 ;j<B; j++)
			{  if((i&j)<K)count1++;
			   if(i==j)count2++;
			}

		//if(x!=1)cout<<"Case #"<<count+1<<": "<<"NOT POSSIBLE"<<endl;
	    out<<"Case #"<<count+1<<": "<<count1<<endl;
	    count++;
	}

}
