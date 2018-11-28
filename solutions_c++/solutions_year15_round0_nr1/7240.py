#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(int argc, char **argv)
{
	if(argc!=3)
	{
		cout<<"Error"<<endl;
		return 0;
	}

	ifstream input(argv[1]);
	ofstream output(argv[2]);

	if(!input.is_open())
	{
		cout<<"File not found '"<<argv[1]<<"' "<<endl;
		return 0;
	}

	int T;
	
	input>>T;

	for(int t=0;t<T;t++)
	{
		char aux;
		int S_max;
		input>>S_max;
		
		cout<<S_max;
		input.get(aux);
		cout<<aux;
		int sum=0;
		int add=0;
		for(int k=0;k<S_max+1;k++)
		{
			input.get(aux);
			cout<<aux;
			int audience=(int)aux-48;
			//cout<<audience<<" ";
				
			if(sum<k)
			{
				int ds=k-sum;
				sum+=ds;
				add+=ds;
			}	

			sum+=audience;
		}
		cout<<"\nCase #"<<(t+1)<<" "<<add<<endl;
		output<<"Case #"<<(t+1)<<": "<<add<<endl;
		
		cout<<endl;		
	
	}

}
