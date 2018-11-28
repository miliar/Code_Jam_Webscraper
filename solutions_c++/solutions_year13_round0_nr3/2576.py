#include<iostream>
#include<fstream>
#include<cstdio>
#include<math.h>
#define l_int long long
using namespace std;


l_int palindrome[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

l_int check(l_int a,l_int b)
{
	l_int count=0;
	for(int i=0;i<39;i++)
	{
		if(a<=palindrome[i])
		{
			for(int j=i;j<39;j++)
			{
				if(b>=palindrome[j])
				{
					++count;
					//cout<<palindrome[j]<<endl;
				}	
				else
				{
					return count;
				}
					
			}
		}
	}
	
}

int main()
{
	l_int T,A,B;
	ifstream infile;
	ofstream outfile;
  	infile.open("C-large-1.in");
  	outfile.open("c-output.out");
  	if (infile.is_open())
	{
	  	
	  		infile>>T;
	  		int k=1;
	  		
	  		while(T--)
	  		{
	  			infile>>A;
	  			infile>>B;
	  			l_int count=0;
	  			if(B<4004009004004)
	  				count=check(A,B);
	  			else 
	  				count=check(A,4004009004000);

	  			if(B>=4004009004004 && B<=100000000000000)
	  				++count;
	  			outfile<<"Case #"<<k++<<": "<<count<<endl;
	  		}

	  	
	}	
	infile.close();
	outfile.close();
  return 0;
}
