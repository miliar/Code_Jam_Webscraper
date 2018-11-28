#include <iostream>
#include <cstdio>

using namespace std;


int main ()
{
	freopen("in","r", stdin);
	freopen("out","w", stdout);
	
	
	int T;
	
	cin >> T;
	
	for (int i=0;i<T;i++)
	{
		int n1,n2, arr1[4][4], arr2[4][4],tmp1[4],tmp2[4];
		
		cin >> n1;
		
		for (int j=0;j<4;j++)
			for (int h=0;h<4;h++)
			{
				cin >> arr1[j][h];
				if (j==n1-1)
					tmp1[h]=arr1[j][h];
			}
		
		cin >> n2;
		
		for (int j=0;j<4;j++)
			for (int h=0;h<4;h++)
			{
				cin >> arr2[j][h];
				if (j==n2-1)
					tmp2[h]=arr2[j][h];
			}
		
		int cntr=0,last;
		
		for (int j=0;j<4;j++)
			for (int h=0;h<4;h++)
				if (tmp1[j]==tmp2[h])
				{
					cntr++;
					last=tmp1[j];
				}
					
		cout << "Case #"<<i+1<<": ";
		
		if (cntr==1)
			cout << last<<'\n';
			
		if (cntr>1)
			cout<< "Bad magician!"<<'\n';
		
		if (cntr==0)
			cout << "Volunteer cheated!"<<'\n';
		
	}
	
	
		return 0;
}
