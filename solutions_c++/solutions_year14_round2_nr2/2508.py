#include<iostream>
#include<fstream>
using namespace std;
typedef unsigned long long int longx;
int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("output_1B_2.txt");
 	int T;
 	longx a,b,k,count=0;
 	fin>>T;
 	for(int t=0;t<T;t++)
 	{
 		count=0;
 		fin>>a>>b>>k;
 		for(longx i=0;i<a;i++)
 		for(longx j=0;j<b;j++)
 		{
 			longx x=i&j;
 			if(x<k)
 			count++;
 		}
 		
 		fout<<"Case #"<<t+1<<": "<<count<<endl;
 	}
}
