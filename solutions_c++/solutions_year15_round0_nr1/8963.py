#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
	ofstream output;
	ifstream input;

	input.open("input2.in");
	output.open("Out.txt");
	//output.clear();


	int T;
	int y=0;
	bool flag=0;
	int num=0;
	input>>T;
	for(int t=1; t<=T; t++)
	{
		int n1=0;

		input>>n1;
		int* S1=NULL;
		char* S=NULL;
		S1= new int[n1+1];
		S=new char[n1+1];
		for(int i=0;i<=n1;i++)
		{
			input>>S[i];
			S1[i]= atoi (&S[i]);
			//S=(int) s;
			//S>>S1[i];
		}
		for(int j=0;j<=n1;j++)
			if(j==0)
				num=num+S1[j];
			else
				if(S1[j]!=0)
				{
				if(num>=j)
					num=num+S1[j];
				else
				{
					y=y+(j-num);
					num=num+(j-num);
					num=num+S1[j];

				}
				}
      
			
				output<<"Case #"<<t<<": "<<y<<endl;
			y=0;
			num=0;
	}
	//char t;
	//cin>>t;
	output.close();
	input.close();
	return 0;
}

