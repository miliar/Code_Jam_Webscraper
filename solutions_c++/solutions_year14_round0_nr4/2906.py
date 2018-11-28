#include <iostream>
#include <fstream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
//ifstream cin("D-small-attempt0.in");
//ofstream cout("B-small-attempt0.out"); 
int cases,testno=0,n,i,j,naocnt=0,naocntd=0,selected,selectedk;
double naomi[1010],ken[1010],temp,tempk;
char selnao[1010],selken[1010],flag=0;
cin>>cases;
while(cases--)
{
	testno++;
	naocnt=0;
	naocntd=0;
	cin>>n;
	for(i=0;i<n;i++)
	{
		cin>>naomi[i];
	}
	for(i=0;i<n;i++)
	{
		cin>>ken[i];
	}
	for(i=0;i<n;i++)
	{
		selnao[i]=1;
		selken[i]=1;
	}
	//war
	for(i=0;i<n;i++)
	{
		
		temp=1.0;
		
		for(j=0;j<n;j++)
		{
			if(naomi[j]<temp && selnao[j]==1)
			{
				temp=naomi[j];
				selected=j;
			}
			
		}	
		selnao[selected]=0;
		tempk=2.0;
		flag=0;
		for(j=0;j<n;j++)
		{
			if(ken[j]>temp && ken[j]<tempk && selken[j]==1)
			{
				tempk=ken[j];
				selectedk=j;
				flag==1;
			}
		}	
		if(tempk<1.1)
		{
			selken[selectedk]=0;
			//cout<<"debug:flag==1"<<endl;
		}
		else
		{
		
		tempk=1.0;
		for(j=0;j<n;j++)
		{
			if(ken[j]<tempk && selken[j]==1)
			{
				tempk=ken[j];
				selectedk=j;
			}
		}
		selken[selectedk]=0;
		naocnt++;
		}
		//cout<<"debug: temp="<<temp<<"tempk="<<tempk<<endl;
	}
	// d-war
	for(i=0;i<n;i++)
	{
		selnao[i]=1;
		selken[i]=1;
	}
	
	for(i=0;i<n;i++)
	{
	
	temp=2;
		
	   for(j=0;j<n;j++)
		{
			if(naomi[j]<temp && selnao[j]==1)
			{
				temp=naomi[j];
				selected=j;
			}
			
		}	
		selnao[selected]=0;
		tempk=2.0;
	
		for(j=0;j<n;j++)
		{	
			if(ken[j]<tempk  && selken[j]==1)
			{
				tempk=ken[j];
				selectedk=j;
				
			}
		}	
		if(temp>=tempk)
		{
			selken[selectedk]=0;
			naocntd++;
		}
		else
		{
			tempk=-2.0;
			for(j=0;j<n;j++)
		{	
			if(ken[j]>tempk  && selken[j]==1)
			{
				tempk=ken[j];
				selectedk=j;
				
			}
		}
		selken[selectedk]=0;
					
		}
		//cout<<"debug: temp="<<temp<<"tempk="<<tempk<<"naocntd="<<naocntd<<endl;
   }
	
	
	cout<<"Case #"<<testno <<": "<<naocntd<<" "<<naocnt<<endl;
}


	return 0;
}