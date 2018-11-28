#include <iostream>
#include <string>
#include <fstream>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;
using std::ios;

void exch(double* a, int i, int j)
{
	double t=a[i];
	a[i]=a[j];
	a[j]=t;
}

void Sort(double * source, int length)
{
	for( int i=0; i<length; i++)
	{
		int min= i;
		for (int j= i+1;j<length;j++)
		{
			if(source[j]<source[min]) min = j;
		}
		exch(source, i,min);
	}
}

int Find(double data, double * source, int min, int max)
{
	for(int i=min;i<=max;i++)
	{
		if(data<source[i])
		{   
			for(int j=i;j<=max;j++)
			{
				source[j]=source[j+1];
			}
			return i;
		}
	}
	return -1;
}



int main()
{
	cout<<"Please input file name: ";
	string infilename;
	string number;
	cin >> infilename;
	ifstream infile(infilename.c_str());
	if(!infile)
	{
		cout<<"error: unable to open input file"<<endl;
		return -1;
	}
	ofstream outfile("out.txt");

	int T;
	infile>>T;
	double Naomi[1002], Ken[1002];
	double NaomiCopy[1002], KenCopy[1002];
	for(int i=1; i<=T; i++)
	{
		int column;
		infile>>column;
		for(int j=0; j<column; j++)
		{
			infile>>Naomi[j];
			
		}
		Sort(Naomi,column);
		for(int j=0; j<column; j++)
		{
			NaomiCopy[j]=Naomi[j];
			
		}

		for(int j=0; j<column; j++)
		{
			infile>>Ken[j];
			
		}
		Sort(Ken,column);
		for(int j=0; j<column; j++)
		{
			KenCopy[j]=Ken[j];
			
		}
		
		outfile<<"Case #"<<i<<": ";

		int Score=0;
		int Nmin,Kmin;
		int Nmax,Kmax;
		Nmin=Kmin=0;
		Nmax=Kmax=column-1;

		for(int j=0;j<column;j++)
		{
			if(Naomi[Nmin]<Ken[Kmin])
			{
				if(Naomi[Nmin]>Ken[Kmax])
					Score++;
				Nmin++;
				Kmax--;
			}
			else
			{
				Score++;
				Nmin++;
				Kmin++;
			}
		}
		outfile<<Score<<" ";

		Score=0;
		Nmin=Kmin=0;
		Nmax=Kmax=column-1;

		for(int j=0;j<column;j++)
		{
			if(Find(Naomi[Nmin],Ken,Kmin,Kmax)!=-1)
			{
				Nmin++;
				Kmax--;
			}
			else
			{
				Nmin++;
				Kmax--;
				Score++;
			}
		}

		outfile<<Score<<'\xA';


		
		


	}


	return 0;
}