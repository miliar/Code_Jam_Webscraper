#include <iostream>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string.h>

using namespace std;

int main ()
{
int t;
ifstream file1;
ofstream file2;
file1.open("inpbl.txt",ios::in);
file2.open("outputbl.txt");
file1>>t;
cout<<t;
int cnt=1;
while (t--)
		{
		int n,m;
		file1>>n>>m;
		int rowmax[n];
		int colmax[m];
		int arr[n][m];
		for (int i=0;i<n;++i)
				{
					rowmax[i]=0;
					for (int j=0;j<m;++j)
					{
						file1>>arr[i][j];
						if (arr[i][j]>rowmax[i])
						{
							rowmax[i]=arr[i][j];
						}
					}
				}

				for (int j=0;j<m;++j)
				{
					colmax[j]=0;
					for (int i=0;i<n;++i)
					{
						if (arr[i][j]>colmax[j])
						{
							colmax[j]=arr[i][j];
						}
					}
				}
int flagbrk=0;
for (int i=0;i<n;++i)
	{
		for (int j=0;j<m;++j)
		{
			if (arr[i][j]<rowmax[i] && arr[i][j]<colmax[j])
			{
                                    
				file2<<"Case #"<<cnt<<": NO\n";
				flagbrk=1;
				break;

			}
		}
			if (flagbrk==1)
				break; 
	}
if (flagbrk==0)
{
file2<<"Case #"<<cnt<<": YES\n";	
}		
cnt++;
		}
return 0;
}
