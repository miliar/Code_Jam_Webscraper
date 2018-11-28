/*#include<iostream> // place this '<' & '>' instead of '(' & ')' before iostream.h
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

*/
#include<iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
//	ifstream myfile ("ash.txt");
	ofstream myfile2 ("ash2.txt");
	int t;
	cin>>t;
	int max=t;
	int n;
	int b[17]={0};
	int save=0;
	int a[4][4];
		int n1;
		int i,j;
	int count=0;
		while(t>0)
		{
			cin>>n;
			for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
				cin>>a[i][j];
				}
			}
		for(j=0;j<4;j++)
		{
			b[a[n-1][j]]=1;
		}
		for(j=0;j<16;j++)
		{
		//	cout<<b[j]<<" ";
		}
		cin>>n1;
		//cout<<endl;
		for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
			cin>>a[i][j];
				}
			}
		for(j=0;j<4;j++)
		{
			b[a[n1-1][j]]++;
		}
		for(j=0;j<17;j++)
		{
		//	cout<<b[j]<<" ";
		}
		for(j=0;j<17;j++)
		{
			if(b[j]==2)
             {
             	count++;
             	save=j;
             }
		}
		if(count==1)
		{
			myfile2<<"Case #"<<max-t+1<<": "<<save<<endl;
		}
		if(count<1)
		{
         myfile2<<"Case #"<<max-t+1<<": "<<"Volunteer cheated!"<<endl;
		}
		if(count>1)
		{
		myfile2<<"Case #"<<max-t+1<<": "<<"Bad magician!"<<endl;
		}
		count=0;
		for(j=0;j<17;j++)
		{
			b[j]=0;
		}
t--;	
}
	
	return 0;
	
}
