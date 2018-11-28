#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int ans,i,j,k,t,no,l[2],u[2];
	unsigned long int tmp,ar[2][1000];
	float f;
    ifstream fin;
	ofstream fout;

	fin.open("D-large.in",ios::in);
	fout.open("D-large.out",ios::out);
    fin>>t;
    for(k=0;k<t;k++)
    {
		fin>>no;
		fout<<"Case #"<<k+1<<": ";
		
		for(i=0;i<no;i++)
		{
			fin>>f;
			f*=100000;
			ar[0][i]=unsigned long int(f);
		}
		for(i=0;i<no;i++)
		{
			fin>>f;
			f*=100000;
			ar[1][i]=unsigned long int(f);
		}
		
		for(i=0;i<no;i++)
		{
			for(j=i+1;j<no;j++)
			{
				if(ar[0][i]>ar[0][j])
				{
					tmp=ar[0][i];
					ar[0][i]=ar[0][j];
					ar[0][j]=tmp;
				}
			}
		}
		for(i=0;i<no;i++)
		{
			for(j=i+1;j<no;j++)
			{
				if(ar[1][i]>ar[1][j])
				{
					tmp=ar[1][i];
					ar[1][i]=ar[1][j];
					ar[1][j]=tmp;
				}
			}
		}
		l[0]=0;		l[1]=0;
		u[0]=no-1;	u[1]=no-1;
		ans=0;

		for(i=0;i<no;i++)
		{
			if(ar[0][l[0]]>ar[1][l[1]])
			{
				l[0]++;	l[1]++;
				ans++;
			}
			else
			{
				l[0]++;	u[1]--;
			}
		}


		fout<<ans<<" ";
		ans=0;
		l[0]=0;		l[1]=0;
		u[0]=no-1;	u[1]=no-1;
		
		
		for(i=0;i<no;i++)
		{
			if(ar[0][l[0]]<ar[1][l[1]])
			{
				l[0]++;
				l[1]++;
				continue;
			}
			for(j=l[1]+1;(ar[1][j]<ar[0][l[0]])&&(j<=u[1]);j++);
			if(j>u[1])
			{
				ans++;
				l[0]++; l[1]++;
				continue;
			}
			for(j;j>l[1];j--)
				ar[1][j]=ar[1][j-1];
			l[1]++;
			l[0]++;
		}
		fout<<ans<<endl;
	}
	
	fin.close();
	
	return 0;
}
