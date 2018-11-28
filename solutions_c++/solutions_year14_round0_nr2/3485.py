#include<iostream>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<math.h>
#include<iomanip>
#include<algorithm> 
#include<string>
#include<vector>
using namespace std;


int main()
{
int inc=1;
	ifstream file("i1.in");
	ofstream file2("o1.txt",ios::trunc);
	int t,i,j,k;
	file>>t;
	
	
	
	for(int x=1;x<=t;x++)
	{
		double c,f,x;
		
		file>>c; file>>f; file>>x;
		double t1=x/2,t2,k;
		k=2+f;
		t2=c/2+x/k;
		
		while(t2<t1){
			t1=t2;
			
			t2=t2+(c-x)/k;
			k=k+f;
			t2=t2+x/k;
		}
		
		
		
		file2<<"Case #"<<inc++<<": ";
		
	    
		file2<<setprecision(12)<<t1;
		
		
		file2<<endl;
	}
}
