#include <iostream>
#include <fstream>
using namespace std;
int main()
{
  string line;
    ifstream infile ("example.txt");
    ofstream outfile ("output.txt");
    if ((infile.is_open())&&(outfile.is_open()))
    {
     	int T;
      	int casecurrent=1;
      	infile>>T;
      	while ( casecurrent<=T )
      	{
      		int d;
      		infile>>d;
      		int arr[d];
      		int max=0;
      		for(int i=0;i<d;i++)
      		{
      			infile>>arr[i];
      			if(arr[i]>max)
      				max=arr[i];
      		}

      		int sec=max;
      		for(int i=max;i>0;i--)
      		{
      			int c=0;
      			for(int j=0;j<d;j++)
      			{
					int tem=arr[j];
					while(tem>i)
					{
						c++;
						tem=tem-i;
					}
      			}
      			if(sec>(c+i))
      				sec=c+i;
			}
			outfile<<"Case #"<<casecurrent++<<": "<<sec<<endl;
		}
	}
}
