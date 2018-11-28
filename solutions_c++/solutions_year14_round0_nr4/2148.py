#include<iostream>
#include<fstream>
#include<stdlib.h>

using namespace std;

int sorting(long double *ke1,int a,int b)
{
	int i,j;
	long double x,k;
	x=*(ke1+b);
	i=a-1;
	for(j=a;j<=(b-1);j++)
	{
		if(*(ke1+j)<=x)
		{
			i=i+1;
			k=*(ke1+i);
			*(ke1+i)=*(ke1+j);
			*(ke1+j)=k;
		}
	}
	k=*(ke1+i+1);
	*(ke1+i+1)=*(ke1+b);
	*(ke1+b)=k;
	return (i+1);
}
void quicksort(long double *ke1,int beg,int end)
{
	if(beg<end)
	{
		int a=sorting(ke1,beg,end);
		quicksort(ke1,beg,a-1);
		quicksort(ke1,a+1,end);
	}
}

int swar(long double *na,long double *ke,int n)
{
    int i,j,k,win=0;
    long double *ke1=new long double[n];
    for(i=0;i<n;i++)
        ke1[i]=ke[i];
    quicksort(ke1,0,n-1);
    for(i=0;i<n;i++)
    {
        j=0;
        while(na[i]>ke1[j] && j<n)
            j++;
        if(j<n)
            ke1[j]=0;
        else
        {
            for(k=0;k<n;k++)
            {
                if(ke1[k]!=0)
                    break;
            }
            ke1[k]=0;
            win++;
        }
    }   
    delete []ke1;
    return win;
}
int dswar(long double *na,long double *ke,int n)
{
    int i,j,k,win=0,e1=n-1,e2=n-1;
    long double *na1=new long double[n];
    long double *ke1=new long double[n];
    for(i=0;i<n;i++)
    {    
        na1[i]=na[i];
        ke1[i]=ke[i];
    }
    quicksort(na1,0,n-1);
    quicksort(ke1,0,n-1);
    for(i=0;i<n;i++)
    {
        if(na1[e1]>ke1[e2])
        {    
             win++;
             e1--;
        }
        e2--;
    }
    delete []na1;
    delete []ke1;
    return win;
}

int main()
{
    char dsv[30];
    int T,n,i,s,ds,d=1;
    ifstream f1;
	f1.open("F:\\TC\\BIN\\Code_Jam_2\\IS4_A_B.in");
	ofstream f2;
 	f2.open("F:\\TC\\BIN\\Code_Jam_2\\OS4_A_B.out");
 	f1.getline(dsv,30,'\n');
 	T=atoi(dsv);
    while(T>0)
    {
        f1.getline(dsv,30,'\n');
 	    n=atoi(dsv);
        long double *na,*ke;
        na=new long double[n];
        ke=new long double[n];
        for(i=0;i<n;i++)
        {
            if(i!=n-1)
                f1.getline(dsv,30,' ');
            else
                f1.getline(dsv,30,'\n');
            na[i]=atof(dsv);
        }       
        for(i=0;i<n;i++)
        {
            if(i!=n-1)
                f1.getline(dsv,30,' ');
            else
                f1.getline(dsv,30,'\n');
            ke[i]=atof(dsv);
        }
        s=swar(na,ke,n);
        ds=dswar(na,ke,n);
        delete []na;
        delete []ke; 
        if(d!=1)
            f2<<"\n";
        f2<<"Case #"<<d<<": "<<ds<<" "<<s;
        T--;
        d++;
    }
    f1.close();
    f2.close();
    return 0;
}
