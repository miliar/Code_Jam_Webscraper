#include <fstream>
#include <bits/stdc++.h>
using namespace std;
#define LL long long int
#define N 1009
int a[N];
int b[N];

int max(int a, int b)
{
	if(a==-1) return b;
	if(a>b) return a;
	return b;
}

int min(int a, int b)
{
	if(a==-1) return b;
	if(a<b) return a;
	return b;
}

int ceili(int a, int b) //ceiling of a/b
{
	if(a<=b) return 0;
	int c=a/b;
	if(a%b==0) return c-1;
	return c; 
}

int main()
{
	fstream cin1;
	cin1.open ("B-large.in");			// A-small-attempt1.in");
  	
  	fstream cout1;
  	cout1.open("Problem2sol.txt");
  	
  	int t;
	cin1>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int n,ans,i,j,k,maxi,maxc;
		cin1>>n;
		for(i=0;i<n;i++) {cin1>>a[i];} //a is array function
		
		maxi=-1;
		for(i=0;i<n;i++) {maxi=max(a[i],maxi);}
		
		for(j=0;j<=maxi;j++) {b[j]=0;} //b is count function
		
		for(i=0;i<n;i++) {b[a[i]]++;}
		
		//for(j=0;j<=maxi;j++) {cout<<b[j]<<"\t";} cout<<endl;

		int maxs=-1;
		for(k=1;k<=maxi;k++)
		{
			//cout<<"For all "<<k<<":"<<endl<<"\t";
			maxc=k;
			for(j=1;j<=maxi;j++)
			{
				//if(b[j])
				maxc+=b[j]*ceili(j,k);
				//cout<<j<<" - "<<k<<"/"<<ceili(j,k)<<"\t \t ";
			}
			//cout<<" = \t"<<maxc<<endl<<endl;
			maxs=min(maxs,maxc);
		}
		
		cout1<<"Case #"<<tt<<": "<<maxs<<endl;	
	}
	
	cout1.close();
  	cin1.close();
}
