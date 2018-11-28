#include<iostream>
#include<fstream>
#include<conio.h>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
	ifstream inp("input.in");
	ofstream out("out.txt");
	if(!inp || ! out){
	//	return 100;
	}
	
	int cases;
	inp>>cases;
	for(int z=1;z<=cases;z++)
	{	
		int a,b,k;
		inp>>a>>b>>k;
		int count=0;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					count++;
				}
			}
		}
		out<<"case #"<<z<<": "<<count<<endl;
	
		
	}
	return 0;
}

