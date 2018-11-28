#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	int t, i, j;
	char A[4][4];
	int count=0;
	cin>>t;
	for(;t>0;t--)
	{
		count++;
		int in=0;
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				cin>>A[i][j];
				if(A[i][j]=='.') in=1;
			}
		}

		int ans=-1;
		char temp;
		for(i=0; i<4; i++)
		{
			int f1=0, f2=0;
			for(j=0; j<4; j++)
			{
				if(A[i][j]!='T' && A[i][j]!='X')
					f1=1;
				if(A[i][j]!='T' && A[i][j]!='O')
					f2=1;
			}
			if(f1==0) 
			{
					ans=1;
					break;
			}
			if(f2==0) 
			{
					ans=2;
					break;
			}
		}
		if(ans==1)
		{
			cout<<"Case #" << count <<": X won\n";
			continue;
		}
		else if(ans==2)
		{
			cout<<"Case #" << count <<": O won\n";
			continue;
		}
		for(j=0; j<4; j++)
		{
			int f1=0, f2=0;
			for(i=0; i<4; i++)
			{
				if(A[i][j]!='T' && A[i][j]!='X')
					f1=1;
				if(A[i][j]!='T' && A[i][j]!='O')
					f2=1;
			}
			if(f1==0) 
			{
					ans=1;
				break;
			}
			if(f2==0) 
			{
					ans=2;
				break;
			}
		}
		if(ans==1)
		{
			cout<<"Case #" << count <<": X won\n";
			continue;
		}
		else if(ans==2)
		{
			cout<<"Case #" << count <<": O won\n";
			continue;
		}
		int f1=0, f2=0;
		for(i=0; i<4; i++)
		{
			if(A[i][i]!='X' && A[i][i]!='T')
				f1=1;
			if(A[i][i]!='O' && A[i][i]!='T')
				f2=1;
		}
		if(f1==0)
		{
			cout<<"Case #" << count <<": X won\n";
			continue;
		}
		else if(f2==0)
		{
			cout<<"Case #" << count <<": O won\n";
			continue;
		}
		f1=f2=0;
		for(i=0; i<4; i++)
		{
			if(A[i][3-i]!='X' && A[i][3-i]!='T')
				f1=1;
			if(A[i][3-i]!='O' && A[i][3-i]!='T')
				f2=1;
			
		}
		if(f1==0)
		{
			cout<<"Case #" << count <<": X won\n";
			continue;
		}
		else if(f2==0)
		{
			cout<<"Case #" << count <<": O won\n";
			continue;
		}
		if(in==1) cout<<"Case #"<<count<<": Game has not completed\n";
		else cout<<"Case #"<<count<<": Draw\n";
	}
}

