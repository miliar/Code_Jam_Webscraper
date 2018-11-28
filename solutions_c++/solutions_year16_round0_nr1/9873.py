#include<fstream>
using namespace std;
int main()
{
	int t,n,i,m,count,j,arr[15],a;
	ifstream fin;
	ofstream fout;
	fin.open("abc.in");
	fout.open("out.out");
	fin>>t;
	int k=1;
	while(t--)
	{
		fin>>n;
		count=0;
		i=1;
		if(n==0)
		{
			fout<<"Case #"<<k++<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
			while(1)
			{
				m=n*i;
				while(m>0)
				{
					a=m%10;
					for(j=0;j<count;j++)
					{
						if(arr[j]==a)
							break;
					}
					if(j==count)
					    arr[count++]=a;
					m/=10;  
				}
				if(count==10)
					break;
				i++;
			}
			fout<<"Case #"<<k++<<": "<<n*i<<endl;
		}
	}
	fin.close();
	fout.close();
}
