#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int T,n1,n2;

	fstream inf("A-small-attempt0.in",ios::in);
	fstream outf("outA.txt",ios::out);
	int arr[4][4];
	int temp1[4];
	int temp2[4];

	inf>>T;

	int k=0;
	while(k<T)
	{
		int arr1[4][4];
		int arr2[4][4];
		int temp1[4];
		int temp2[4];


		inf>>n1;
		int t1=0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				inf>>arr2[i][j];
				if((n1-1)==i)
				{
					temp1[t1++]=arr2[i][j];
				}
			}

			inf>>n2;
			t1=0;
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
				{
					inf>>arr2[i][j];
					if((n2-1)==i)
					{
						temp2[t1++]=arr2[i][j];
					}
				}

				int num=0;
				int count=0;
				bool b=false;
				for(int i=0;i<4;i++)
					for(int j=0;j<4;j++)
					{
						if(temp1[i]==temp2[j])
						{
							num=temp1[i];
							count++;
		
							break;
						}
					}

					outf<<"Case #"<<k+1<<": ";
					if(count==1)
						outf<<num<<endl;
					else if(count==0)
						outf<<"Volunteer cheated!"<<endl;
					else if(count>1)
						outf<<"Bad magician!"<<endl;
					k++;
	}
	return 0;
}
