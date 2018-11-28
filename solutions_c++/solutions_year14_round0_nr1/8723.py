#include<fstream>
#include<iostream>

using namespace std;


int main()
{	
	ifstream input;
 	ofstream output;
 	input.open("one.txt");
 	output.open("two.txt");
	int t;
	input>>t;
	int s=t;
	while(t--)
	{   int r1,r2,a1[4][4],a2[4][4],i,j,b1[16],b2[16],g;
		input>>r1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				input>>a1[i][j];
				b1[a1[i][j]-1]=i+1;
			}
		}
		input>>r2;
	
		for(i=0;i<4;i++)
		{for(j=0;j<4;j++)
		{input>>a2[i][j];
				b2[a2[i][j]-1]=i+1;
		}
		}
		int sum=0;
		for(i=0;i<16;i++)
		{
			if(b1[i]==r1&&b2[i]==r2)
			{g=i+1;
			
			sum++;
		    }
		}
		if(sum==0)
		output<<"Case #"<<s-t<<": Volunteer cheated!\n";
		else if(sum==1)
		output<<"Case #"<<s-t<<": "<<g<<'\n';
		else
		output<<"Case #"<<s-t<<": Bad magician!\n";	
	}
	return 0;
}

