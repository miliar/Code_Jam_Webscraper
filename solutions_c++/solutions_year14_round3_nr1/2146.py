#include<iostream>
#include<cstring>
#include<fstream>
#include<cmath>
#include<stdlib.h>        //for qsort()
#include<string>

using namespace std;

int main()
{
	int cases,nr,dr,answer,t;
	double mynum;
	char nstr[6],dstr[6];
	ifstream fin("input.txt",ios::in);
	ofstream fout("output.txt",ios::out);
	fin>>cases;
	t = 1;
	while(t<=cases)
	{
		fin.getline(nstr,6,'/');
		nr = atoi(nstr);
		fin.getline(dstr,6,'\n');
		dr = atoi(dstr);
		cout<<nr<<" "<<dr<<" ";
		mynum = static_cast<double>(nr)/dr;
		cout<<mynum<<"\n";
		if(mynum==1)
		{
			answer = 0;		
		}
		else if(mynum>1)
		{
			answer = -1;
		}
		else
		{
			int count = 1;
			for(double i = 0.5 ; ; )
			{
				if(mynum>=i)
				{
					answer = count;
					break;
				}
				i = i/2.0;
				count++;
			}
		}
		/*if(answer>0)
		{
			while(mynum<1)
				mynum*=2;
			if(mynum!=1)
				answer = -1;
		}*/
		/*if(answer>0)
		{
			if(dr%2!=0)
				answer = -1;
		}*/
		if(answer>0)
		{
			
			while(floor(mynum)<mynum)
				mynum*=10;
			if(static_cast<int>(mynum)%5!=0)
				answer=-1;
		}
		if(answer!=-1)
			fout<<"Case #"<<t<<": "<<answer<<"\n";
		else
			fout<<"Case #"<<t<<": impossible\n";
		t++;
	}
	fin.close();
	fout.close();
	return 0;
}
