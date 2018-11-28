#include<iostream>
#include<fstream>
using namespace std;
void resetarray(int arr[])
{
	for(int j=0;j<10;j++)
	{
		arr[j]=99;
	}
}
int main()
{

	ifstream fin("file.txt");
	ofstream fout("output.txt");
	int testcases=0;
	int number=0,rem=0,i=0,num=0,n=1,extra=0,casenumber=0;
	int arr[10];
	bool flag=false;

	fin>>testcases;

	while(testcases!=0)
	{
			fin>>number;
			num=number;
			casenumber++;

			resetarray(arr);

			if(number==0)
			{
				fout<<"Case #"<<casenumber<<": INSOMNIA";
			}
			else
			{
				i=0;n=0;
				while(i!=10)
				{
					while(number!=0)
					{
						rem=number%10;
						for(int j=0;j<10;j++)
						{
							if(arr[j]!=rem)
							{
								flag=true;
							}
							else{
								flag=false;
								break;
							}
						}
						if(flag==true)
						{
							arr[i]=rem;
							i++;
						}
						number=number/10;
					
					


					}
					n++;
					
					number=num*n;
					
						
				}
			


				/*for(int j=0;j<10;j++)
						{
						cout<<arr[j]<<endl;
						}*/

				fout<<"Case #"<<casenumber<<": "<<number-num;
				
			}
			fout<<" \n";
			testcases--;
	}	
	return 0;
}