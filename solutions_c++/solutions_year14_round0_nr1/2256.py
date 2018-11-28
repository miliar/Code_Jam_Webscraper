#include<iostream.h>
#include<fstream.h>
#include<conio.h>

void main()
{
	int T,n,p[4][4],q[4],c=0,k;
	ifstream fin;
	ofstream fout;
	clrscr();

	fin.open("A.in",ios::in);
	fout.open("F2.txt",ios::out);
	fin>>T;
	while(T--)
	{
			fin>>n;       c++;
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
					fin>>p[i][j];

			for(i=0;i<4;i++)
				q[i]=p[n-1][i];

			fin>>n;
			for(i=0;i<4;i++)
				for(j=0;j<4;j++)
					fin>>p[i][j];

			int f=0;
			for(i=0;i<4;i++)
				for(j=0;j<4;j++)
					if(p[n-1][j]==q[i])
					{
							k=q[i];
							f++;
					}
			switch(f)
			{
				case 0:  fout<<"Case #"<<c<<": Volunteer cheated!\n";
							cout<<"Case #"<<c<<": Volunteer cheated!\n";
							break;
				case 1:  fout<<"Case #"<<c<<": "<<k<<endl;
							cout<<"Case #"<<c<<": "<<k<<endl;
							break;
				default: fout<<"Case #"<<c<<": Bad magician!\n";
							cout<<"Case #"<<c<<": Bad magician!\n";
			}
	}
	getch();
}
