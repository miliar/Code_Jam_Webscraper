#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
	int t,i,j,k,n,mot,rem,nop,pop;
	int a[100];
	ifstream fin("c:/a.txt");
	ofstream fout("c:/o.txt");

	fin>>t;
	for(k=0;k<t;k++)
	{
		fin>>mot>>n;
		//fout<<mot<<" "<<n<<endl;
		memset(a,0,sizeof(a));
		for(j=0;j<n;j++)
		{
		    
			fin>>a[j];
			
		}
		
		sort(a+0,a+n);
		//for(j=0;j<n;j++)
			//fout<<a[j]<<" ";
		rem=n;
		nop=0;
		for(i=0;i<n;i++)
		{
			if(mot==1)
			{
				nop=rem;
				break;
			}
			else if(mot>a[i])
			{
				mot+=a[i];
				rem--;
			}
			else
			{
				pop=nop;
				do
				{
					mot=mot+mot-1;
					nop++;
					if(mot>a[i])
						break;

				}while(1);
				if((nop-pop)>rem)
				{
					nop=pop+rem;
					break;
				}
				else
				{
					rem--;
					mot+=a[i];
				}
			}
		}
		//fout<<endl;
		if(nop>n)
			nop=n;
		fout<<"Case #"<<(k+1)<<": "<<nop<<endl;
		//fout<<endl;
	}


	
	
	return 0;
}