// Craciun Catalin
//  D
//   Google Code Jam
#include <iostream>
#include <algorithm>

#define NMax 205

using namespace std;

int t;
int n;
double A[NMax]; // Girl
double B[NMax]; // Boy

int P[NMax]; // Backtracking
int notFairGame=-1;

int notFairGamePlay()
{	
	// Sorting the arrays
	sort(A, A+n+1);
	sort(B, B+n+1);
	
	int leftAPoz=1;
	int rightBPoz=n;
	
	int obj=0;
	int ra=n, rb=n;
	while (A[ra]>B[rb])
	{
		ra--, rb--;
		obj++;
	}
	
	rightBPoz=rb;
	
	while (B[rightBPoz]>A[leftAPoz])
	{
		leftAPoz++;
		rightBPoz--;
	}

	return ra-leftAPoz+1+obj;
}

void found()
{
	int rez=0;
	int Aright=n, Aleft=1, Bright=n;
	
	for (int i=1;i<=n;i++)
	{
		if (P[i]==1)
		{
			if (A[Aright]>B[Bright])
				rez++;
			Aright--;
			Bright--;
		}
		else if (P[i]==2)
		{
			Aleft++;
			Bright--;
		}
	}
	
	if (notFairGame==-1)
		notFairGame=rez;
	else if (notFairGame<rez)
		notFairGame=rez;
}

void generate(int k)
{
	if (k>n)
		found();
	else
	{
		for (int i=1;i<=2;i++)
		{
			P[k]=i;
			generate(k+1);
		}
	}
}

int fairGamePlay()
{
	bool BU[NMax];
	int fairGame=0;
	
	// Sorting the arrays
	sort(A, A+n+1);
	sort(B, B+n+1);
	
	// Initialising BU
	for (int i=0;i<=n+1;i++)
		BU[i]=false;
	
	// Playing
	for (int i=n;i>=1;i--)
	{
		double min=-1;
		int poz;
		for (int j=1;j<=n;j++)
			if (BU[j]==false && B[j]>A[i])
			{
				if (min!=-1)
				{
					if (B[j]<min)
					{
						min=B[j];
						poz=j;
					}
				}
				else
				{
					min=B[j];
					poz=j;
				}
			}
		
		if (min==-1)
		{
			for (int j=1;j<=n;j++)
				if (BU[j]==false && A[i]==B[j])
				{
					min=B[j];
					poz=j;
				}
			if (min!=-1)
				BU[poz]=false;
			else
			{
				int j=1;
				while (BU[j]==true)
					j++;
				BU[j]=false;
				fairGame++;
			}
		}
		else
			BU[poz]=true;
	}
	
	return fairGame;
}

int main()
{
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		// Read
		cin>>n;
		for (int k=1;k<=n;k++)
			cin>>A[k];
		for (int k=1;k<=n;k++)
			cin>>B[k];
		
		// Solving
		int fairGame=0;
		notFairGame=-1;
		fairGame=fairGamePlay();
		generate(1);
		// Outputin
		cout<<"Case #"<<i<<": "<<notFairGame<<' '<<fairGame<<'\n';
	}
	
	return 0;
}
