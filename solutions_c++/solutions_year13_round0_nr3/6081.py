#include<iostream>
#include<fstream>
#include<cstdio>
#include<math.h>


using namespace std;
int palindrome(int n)
{
	int rev=n;
	int temp=0;
	while(rev>0)
	{
		temp= temp*10 + rev%10;
		rev=rev/10;
	}
	if(temp == n)
		return 1;
	else
		return 0;

}


int main()
{
	int T;
	int a,b;
	ifstream infile;
	ofstream outfile;
  	infile.open("C-small-attempt0.in");
  	outfile.open("c-output.out");

  	if (infile.is_open())
	{
	  		infile>>T;

	  		int count=1;

	  		while(T--)
	  		{
	  			infile>>a;
	  			infile>>b;
	  			int count_fair=0;
                for(int i=a;i<=b;i++)
	  			{
	  				int root=0;
	  				if(palindrome(i) == 1)
	  				{
		  				root=sqrt(i);

		  				if((i == root*root) && palindrome(root))
		  				{
			  				count_fair++;
		  				}
		  			}
	  			}
	  			outfile<<"Case #"<<count++<<":"<<" "<<count_fair<<endl;
  			}
  	}
    infile.close();
   	outfile.close();
  return 0;
}
