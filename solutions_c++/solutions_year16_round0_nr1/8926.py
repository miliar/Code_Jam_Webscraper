#include <stdafx.h>
#include <iostream>
#include <math.h>
#include <cstring>
#include <fstream>

using namespace std;

int main() {
	int testcases=0,sum=0;
	unsigned long N=0;
	int a[10]={0};
	ofstream f;
	f.open("D:\\op.txt",ios::app);
	
	cin>>testcases;
	
	for(int t=1;t<=testcases;t++)
	{
		int i = 0;
		unsigned long value=0;
		bool bFoundAll = false;
		
		cin>>N;
		
		memset(a,NULL,sizeof(a));
		sum=0;
		
		if(N==0)
		{
		 f<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
		 continue;
		}
		value=N;
		while(true)
		{
		   N = (i+1)*value;	
		   unsigned long new_val = N;
		
		 int digits = ((int)(log10(static_cast<double>(N))) + 1);
		
		 for(int d=0;d<digits;d++)
		 {
		 	
			int r = N%10;
		 	N = (N/10);
		 	
		 	if(a[r]==0)
		 	{
		 		a[r]++;
		 		sum++;
		 	}
		 	if(10==sum)
		 	{
		 	  bFoundAll = true;
			  f<<"Case #"<<t<<": "<<new_val<<endl;
		 	  break;
		 	}
		  }
		  if(true==bFoundAll)
		  {
		  	break;
		  }
		  i++;
		}
	  }
	f.close();
	
	return 0;
}