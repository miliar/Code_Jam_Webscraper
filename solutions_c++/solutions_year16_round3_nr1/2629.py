#include<iostream>
using namespace std;

int main()
{
int t,i,j,sum=0,large=0,lp=0,large1=0,lp1=0;
char ch = 'A';
cin>>t;
int *nop = new int[t];
int **nom = new int*[t];
char **pa = new char*[t];

for(i=0;i<t;i++)
{
	cin>>nop[i];
	nom[i] = new int[nop[i]];
	pa[i] = new char[nop[i]];
	ch='A';
	for(j=0;j<nop[i];j++)
	{
		cin>>nom[i][j];
		pa[i][j] = ch;
		ch = ch+1;
	}
}

for(i=0;i<t;i++)
{
	cout<<"Case #"<<i+1<<": ";
	sum=0; 
	for(j=0;j<nop[i];j++)
	{
		sum = sum + nom[i][j];
		if(nom[i][j]>large)
		{
			large = nom[i][j];
	        lp = j;
		}
	}
	
	while(sum!=0)
	{
		large = nom[i][0];
        lp = 0;
		for(j=0;j<nop[i];j++)
	        {
		      if(nom[i][j]>large)
		      {
			   large = nom[i][j];
	           lp = j;
		      }
        	}
        	nom[i][lp] = nom[i][lp] - 1; 
        	
        	large1 = nom[i][0];
            lp1 = 0;
		 for(j=0;j<nop[i];j++)
	        {
		      if(nom[i][j]>large1)
		      {
			   large1 = nom[i][j];
	           lp1 = j;
		      }
        	}
        	nom[i][lp] = nom[i][lp] + 1;
        	
        	if(large1<=((sum-1)/2))
        	{
	        	nom[i][lp]=nom[i][lp]-1;
	        	sum=sum-1;
	        	cout<<pa[i][lp]<<" ";
	        }
	        else
	        {
        		nom[i][lp1]=nom[i][lp1]-1;
        		nom[i][lp]=nom[i][lp]-1;
        		sum = sum - 2;
        		cout<<pa[i][lp]<<pa[i][lp1]<<" ";
        	}
        	
    }
    cout<<"\n";
    
}

return 0;
}