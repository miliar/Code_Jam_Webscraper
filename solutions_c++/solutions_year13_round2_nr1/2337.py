#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
using namespace std;
ifstream filein;
ofstream fileout;
int size;
int mote;
int* motev;
int process();
int main(int argc,char* argv[])
{
	filein.open(argv[1]);
	fileout.open("result.out");
	int counter;
	filein>>counter;
	for(int i=0;i<counter;i++)
	{
		filein>>mote>>size;
		motev=new int[size];
		for(int j=0;j<size;j++)
		{
			filein>>motev[j];
		}
		sort(motev,motev+size);
		int result=process();
		fileout<<"Case #"<<i+1<<": "<<result<<endl;
		//delete motev;
	}
	return 0;
}

int step(int p1,int p2,int & num)
{
	int st=1;
	int c=p1;
	while(true)
	{
		c=2*c-1;
		if(c>p2)
			break;
		else
		{
			st++;
			continue;
		} 
			
	}
	num=c;
	return st;
}

int process()
{
	int op=0;
	int tmp;
	int* opt=new int[100];
	int co=0;
	//bool flag=false;
	if(mote==1)
		return size;
	for(int i=0;i<size;i++)
	{
		if(mote>motev[i])
		{
			mote+=motev[i];
			continue;
		}
		else
		{
			opt[co]=op+size-i;
			co++;
			int st=step(mote,motev[i],tmp);
			op+=st;
			mote=tmp;
			mote+=motev[i];
			continue;
		}
	}
	opt[co]=op;
	sort(opt,opt+co+1);
	return opt[0];
}