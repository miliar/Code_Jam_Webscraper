#include <iostream>
#include <fstream>
using namespace std;
int main ()
{
	ofstream fout("output.txt");
	ifstream fin("data.txt");
	int T,Smax;
	int vector;
	int i,j,k;
	fin>>T;
	for (i=0;i<T;i++)
	{
		int vectorinv=0,r,vector2;
		fin>>Smax>>vector;
		vector2=vector;
		for(j=0;j<Smax+1;j++)
	    {
	    	r=vector%10;
	    	vector=vector/10;
	    	vectorinv=vectorinv*10+r;
		}
    	int inv=0,s=0;
		for(k=0;k<Smax+1;k++)
    	{
			if(k-s>0)
		    {
			 inv=inv+k-s;
			 s=k;
	     	}
	     	s=s+(vectorinv%10);
			 vectorinv=vectorinv/10;
    	}
  	 fout<<"case #"<<i+1<<": "<<inv<<endl;
	}
    return 0;
}

