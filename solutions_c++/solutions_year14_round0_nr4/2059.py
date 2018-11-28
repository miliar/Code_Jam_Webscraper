#include<iostream.h>
#include<fstream.h>
#include<conio.h>

void main()
{
	int T,num,c=0;
	float *N,*Ken,t;
	ifstream fin;
	ofstream fout;
	clrscr();
	fin.open("D.in");
	fout.open("D1.txt",ios::out);
	fin>>T;
	while(T--)
	{
		c++; int g=0,k=0,m=0;
		fin>>num;
		N=new float[num];
		Ken=new float[num];

		for(int i=0;i<num;i++)
			fin>>N[i];
		for(i=0;i<num;i++)
			fin>>Ken[i];

		for(int j=0;j<num-1;j++)
			for(i=0;i<num-j-1;i++)
			{
				if(N[i]>N[i+1])
				{
					t=N[i];
					N[i]=N[i+1];
					N[i+1]=t;
				}

				if(Ken[i]>Ken[i+1])
				{
					t=Ken[i];
					Ken[i]=Ken[i+1];
					Ken[i+1]=t;
				}
			}

		for(i=0;i<num;i++)
			for(j=g;j<num;j++)
				if(Ken[i]>N[j])
				{
					k++;
					g=j+1;
					break;
				}
		g=0;
		for(i=0;i<num;i++)
			for(j=g;j<num;j++)
				if(N[i]>Ken[j])
				{
					m++;
					g=j+1;
					break;
				}

			fout<<"Case #"<<c<<": "<<m<<" "<<num-k<<endl;
	}
	getch();
}
