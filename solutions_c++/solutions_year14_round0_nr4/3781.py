#include <bits/stdc++.h>
using namespace std;
int main()
{
	double temp,t,x[1000],y[1000];
	int cnt=1,j=0,flag=1,n,i=0;
	string s;
	fstream fin;
	fin.open("D-large.in",ios::in);
	fstream fout;
	fout.open("output_codejam3.out",ios::out);
	if(fin.is_open())
	{
		while(getline(fin,s))
		{
			istringstream iss(s);
			while(iss>>temp)
			{
				if(j==0)
				{
					t=temp;
					j=1;
				}
				else if(j==1)
				{
					n=temp;
					j=2;
				}
				else if(j==2)
				{
					x[i++]=temp;
					if(i==n)
					{
						i=0;
						j=3;
					}
				}
				else if(j==3)
				{
					y[i++]=temp;
					if(i==n)
					{
						i=0;
						j=1;
						flag=2;
					}
				}
			}
			if(j==1 && flag==2)
			{
				sort(x,x+n);
				sort(y,y+n);
			
				int p=0,q=0,point1=0,point2=0;
				if(n==1)
				{
					if(x[0]>y[0])
						point1=point2=1;
					else
						point1=point2=0;
				}
				else
				{
					while(q!=n)
					{
						if(x[p]>y[q])
						{
							q++;
						}
						else if(x[p]<y[q])
						{
							p++;
							q++;
							point1++;
						}
					}
					point1=n-point1;
					p=q=0;
					while(p!=n)
					{
						if(x[p]>y[q])
						{
							p++;
							q++;
							point2++;
						}
						else if(x[p]<y[q])
						{
							p++;
							
						}
					}
					
				}
				fout<<"Case #"<<cnt++<<": "<<point2<<" "<<point1<<endl;
			}
		}
	}
	return 0;
}