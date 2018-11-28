#include<fstream.h>
void main()
{
	int t,n,m,a[100][100],i,j,k=1,m1[100],m2[100],f;
	ifstream fin;
	ofstream fout;
	fin.open("abc.in",ios::in);
	fout.open("out.out",ios::out);
	fin>>t;
	while(t--)
	{
		fin>>n>>m;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				fin>>a[i][j];
		for(i=0;i<n;i++)
			m1[i]=0;
		for(j=0;j<m;j++)
			m2[j]=0;
		f=0;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(a[i][j]>m1[i])
					m1[i]=a[i][j];
		for(i=0;i<m;i++)
			for(j=0;j<n;j++)
				if(a[j][i]>m2[i])
					m2[i]=a[j][i];
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(a[i][j]!=m1[i]&&a[i][j]!=m2[j])
					f=1;
		if(f==1)
			fout<<"Case #"<<k++<<": NO\n";
		else
			fout<<"Case #"<<k++<<": YES\n";
	}
}