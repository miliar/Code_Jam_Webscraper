#include<iostream.h>
#include<stdio.h>
#include<conio.h>
class codejam
{
	private:
		int a[100][100];
		int row[100],col[100];
	public:
	int m,n;
	void setvalue()
	{
		cin>>m;
		cin>>n;
		for(int i=0;i<m;i++)
		row[i]=0;
		for(int i=0;i<n;i++)
		col[i]=0;
		for(int i=0;i<m;i++)
		for(int j=0;j<n;j++)
		cin>>a[i][j];
	}
	void getvalue()
	{
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			cout<<a[i][j];
			cout<<endl;
		}
	}
	void rowmax(int rown)
	{
		row[rown]=0;
		for(int i=0;i<n;i++)
		if(row[rown]<a[rown][i])
		row[rown]=a[rown][i];
	}
	void colmax(int coln)
	{
		for(int i=0;i<m;i++)
		{
			if(col[coln] < a[i][coln])
			col[coln]=a[i][coln];
		}
	}
	int check(int rown)
	{
		for(int i=0;i<n;i++)
		{
			if(a[rown][i] < row[rown])
			{
				if(a[rown][i]<col[i])
				return 0;
			}
		}
		return 1;
	}
};
int main()
{
	codejam c;
	int t,z=1;
	cin>>t;
	while(t>0)
	{
		c.setvalue();
		for(int i=0;i<c.m;i++)
		c.rowmax(i);
		for(int i=0;i<c.n;i++)
		c.colmax(i);
		for(int i=0;i<c.m;i++)
		{
		if(c.check(i)==0)
		{
			cout<<"Case #"<<z<<": NO\n";
			goto end;
		}
		}
		cout<<"Case #"<<z<<": YES\n";
		end:
		t--;
		z++;
	}
	return 0;
}