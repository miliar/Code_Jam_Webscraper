#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;
ifstream fin("A-small-attempt0.in");
ofstream fout("magic.output.txt");



int main()
{
	
	int n;
	fin>>n;
	
	
	for(int i=1;i<=n;i++)
	{
		
		  int n1;
		  fin>>n1;
	// cout<<n1<<endl;
		  int a1[4];
		  string garbage;
		  for(int j=1;j<=4;j++)
		  {
		  	
	//	  	cout<<"j = "<<j;
		  	if(j==n1)
		  	{
		  		for(int k=0;k<4;k++)
		  		{
		  			fin>>a1[k];
		  		
	//	  		cout<<a1[k]<<endl;
				  }
		//  	break;	
		  		
		  	}
		  	else
		  	{
		  		getline(fin>>ws,garbage);
		  	//	cout<<garbage<<endl;
		  	}
		  	
		  }
		
		  int n2;
		  fin>>n2;
		  int a2[4];
		 // string garbage;
	//	 cout<<n2<<endl;
		  for(int j=1;j<=4;j++)
		  {
		  	
		 // 	cout<<"j = "<<j;
		  	if(j==n2)
		  	{
		  		for(int k=0;k<4;k++)
		  		{
		  			fin>>a2[k];
		  		
	//	  		cout<<a2[k]<<endl;
				  }
		  //	break;	
		  		
		  	}
		  	else
		  	{
		  		getline(fin>>ws,garbage);
		  	//	cout<<garbage<<endl;
		  	}
		  	
		  }
		
		  		int count=0,num;
		
		for(int l=0;l<4;l++)
		{
			
			for(int m=0;m<4;m++)
			{
				
				if(a1[l]==a2[m])
				{
					num=a1[l];
					count++;
					
				//	break;
					
				}
				
				
			}
			
			
		}
		
		cout<<"Case #"<<i<<": ";
		fout<<"Case #"<<i<<": ";
		
		if(count==0)
          {
          	cout<<"Volunteer cheated!\n";		
		fout<<"Volunteer cheated!\n";
	    }
		 if(count==1)
		{
		
		cout<<num<<"\n";
		fout<<num<<"\n";
          	}
		if(count>1)
		{
		
			cout<<"Bad magician!\n";
		fout<<"Bad magician!\n";
        	
	}
		
		
		
		
		
		
		
		
	}
	
	
	
//	system("pause");
	
	return 0;
}
