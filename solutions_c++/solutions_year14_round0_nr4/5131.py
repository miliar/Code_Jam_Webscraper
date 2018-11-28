#include<iostream> // place this '<' & '>' instead of '(' & ')' before iostream.h
#include<conio.h>
#include<fstream> // place this '<' & '>' instead of '(' & ')' before iostream.h
#include<iomanip>
#include<vector>
#include<algorithm>
using namespace std;
int fair(vector<double>ladki,vector<double>ladka,int n)
{
	int ladkiB=n-1;
	int ladkaB=n-1;
	int ladkiS=0;
	int ladkaS=0;
	
	sort(ladki.begin(),ladki.end());
	sort(ladka.begin(),ladka.end());

	int count=0;

	while(ladkiB>=ladkiS && ladkaB>=ladkaS)
	{
		if( ladki[ladkiB]>ladka[ladkaB])
		{ladkiB--;
			count++;ladkaS++;
		}
		else
		{ladkaB--;
		ladkiB--;
		}

	}
	return count;

}
int unfair(vector<double>ladki,vector<double>ladka,int n)
{
	int ladkiB=n-1;
	int ladkaB=n-1;
	int ladkiS=0;
	int ladkaS=0;
	
	sort(ladki.begin(),ladki.end());
	sort(ladka.begin(),ladka.end());

	int count=0;

	while(ladkiB>=ladkiS && ladkaB>=ladkaS)
	{
		while( ladkiB>=ladkiS && ladkiB>=ladkiS && ladki[ladkiS]<ladka[ladkaS] )
		{
			ladkiS++;
		}
		if(ladkiB>=ladkiS && ladkiB>=ladkiS)
		{
			count++; ladkaS++;ladkiS++;
		}

	}
	return count;


}
ofstream xs("o.txt");
void main( )
{
	int ntc;
	int n;
	vector<double>ladki,ladka; 
    cin>>ntc;int k=1;
	while(ntc--)
	{double x;
		cin>>n;
		ladki.clear();
		ladka.clear();
		for(int i=0;i<n;i++)
			{cin>>x;ladki.push_back(x);}
			for(int i=0;i<n;i++)
			{cin>>x;ladka.push_back(x);}


			//getch();
    int fairs=fair(ladki,ladka,n);
	int unfairs=unfair(ladki,ladka,n);
	xs<<"Case #"<<k++<<": ";

	xs<<unfairs<<" ";//<<fairs<<endl;
	xs<<fairs<<endl;
	}
	//getch();
}

