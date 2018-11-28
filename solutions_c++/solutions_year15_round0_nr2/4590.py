// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <stdlib.h> 
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

bool compare (int i,int j) { return (i>j); };

int gyl (vector <int> v)
{

	int nb;
	int reste;
	sort (v.begin(), v.end(), compare);
	nb=count(v.begin(),v.end(),v[0]);
	if(v[0]<=3)
	{
		return(v[0]);
	}
	else
	{
		int minn=v[0];
		vector <int> v2=v;
		for(int n=2;n<=floor(sqrt(v[0])) && n<=ceil(v[0]/nb);n++)
		{
			vector <int> v2=v;
			v2.erase(v2.begin(),v2.begin()+nb);
			reste=v[0]%n;
			for(int i=0;i<(nb*n);i++)
			{			
					if(i%n<reste)	
					{
						v2.push_back(floor(v[0]/n)+1);
					}
					else
					{
						v2.push_back(floor(v[0]/n));	
					}
			}
			int tmp=(int)ceil(v[0]/n);
			int tmp1=gyl(v2);
			int tmp2=max(tmp1,tmp)+(n-1)*nb;
			if(minn>tmp2)
			{
				minn=tmp2;
			}
		}
		return(minn);
	}
};



int main() {

	ifstream myfile ("example.txt");
	ofstream output;
	output.open("output.txt");
	int Nb;
	myfile>>Nb;
	for (int i=0;i<Nb;i++)
	{
		output<<"Case #"<<(i+1)<<": ";
		int size;
		int tmp;
		
		myfile>>size;
		vector <int> v;
		
		
		for (int j=0;j<size;j++)
		{
			myfile>>tmp;
			v.push_back(tmp);
		}
		
		output<<gyl(v)<<endl;


	}
	return 0;
}
