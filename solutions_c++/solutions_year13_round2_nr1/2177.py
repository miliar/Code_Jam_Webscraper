#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;

ifstream in("input.txt",ios::in);
ofstream out("output.txt",ios::out);

int check(long long int my,int others, int* oth, int pos)
{
	if(pos>others)
		return 0;
	if(oth[pos]>=my)
	{
		if(my==1)
			return check(my,others,oth,pos+1)+1;
		int first=check(my+my-1,others,oth,pos)+1;
		int sec=check(my,others,oth,pos+1)+1;
		if(first<sec)
			return first;
		else 
			return sec;
	}
	else
	{
		return check(my+oth[pos],others,oth,pos+1);
	}
	
}

void main()
{
	int num;
	in>>num;
	for(int i=1 ; i<=num ; i++)
	{
		out<<"Case #"<<i<<": ";
		long long int my;
		int others;
	
		in>>my;
		in>>others;
		int* oth=new int[others];
		for(int i=0 ; i<others ; i++)
			in>>oth[i];
		for(int i=0 ; i<others ; i++)
			for(int j=0 ; j<others-1 ; j++)
				if(oth[j]>oth[j+1])
				{
					int temp=oth[j];
					oth[j]=oth[j+1];
					oth[j+1]=temp;
				}
		int res=check(my,others,oth,0);
		out<<res<<endl;
	}
}
