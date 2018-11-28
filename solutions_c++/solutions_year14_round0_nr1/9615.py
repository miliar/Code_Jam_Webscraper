#include<conio.h>
#include<iostream.h>
#include<fstream.h>
#include<stdio.h>
void main()
{
clrscr();
char s[15];
int t,a[100],z;
ifstream fin("C:\\TC\\bin\\vijitd\\gcodejam\\i1.txt");
ofstream fout("C:\\TC\\bin\\vijitd\\gcodejam\\outA.txt");
fin>>t;
fin.get();
z=t;
do
{
	int arr[2][4][4], v[2],ans=17,m;
	for(int i=0;i<2;i++)
	{
	fin>>v[i];
	fin.get();
	--v[i];
		for(int j=0;j<4;j++)
		{
			fin.getline(s,15,'\n');
			sscanf(s,"%d %d %d %d",&arr[i][j][0],&arr[i][j][1],&arr[i][j][2],&arr[i][j][3]);
		}
	}
	for(i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(arr[0][v[0]][i]== arr[1][v[1]][j])
			{
				m=arr[0][v[0]][i];
				++ans;
				break;
			}
		}
	}
	if(ans==18)
	a[t-1]=m;
	else
	a[t-1]=ans;
}while(--t);

for(int i=z-1;i>=0;i--)
	{
		fout<<"Case #"<<z-i<<": ";
		if(a[i]==17)
		fout<<"Volunteer cheated!\n";
		else if(a[i]>18)
		fout<<"Bad magician!\n";
		else
		fout<<a[i]<<endl;
	}
getch();

}