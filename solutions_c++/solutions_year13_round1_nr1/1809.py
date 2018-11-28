#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<fstream>


using namespace std;


int main()
{
	ofstream out("soutput.txt");
	
	int tst;
	cin>>tst;
	
	for(int j=0;j<tst;j++)
	{
		long int r,t;
		cin>>r>>t;
		
		int cnt=0,tarea=0,i=r+1;
		
		while(tarea<=t)
		{
			tarea+=i*i-(i-1)*(i-1);
			
			if(tarea<=t)cnt++;
			
			i+=2;
		}
		
		out<<"Case #"<<j+1<<": "<<cnt<<endl;
	}
	
		out.close();
}	

			
	
	
	
