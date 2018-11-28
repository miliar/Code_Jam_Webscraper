#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream infile;
	infile.open("A-large.in");
	int T;
	infile>>T;
	ofstream outfile;
	outfile.open("largeoutput2016.in");
	for(int l=1;l<T+1;)
	{
		int n,flag=0,arr[10],k=0;
		infile>>n;
		for(int i=1;;i++)
		{
			if(n==0)
			{
				outfile<<"Case #"<<l++<<": "<<"INSOMNIA"<<endl;
				break;
			}
			if(k==10)
			{
				outfile<<"Case #"<<l++<<": "<<(i-1)*n<<endl;
				break;
			}
			int p=i*n;
			while(p>0)
			{
				int no=p%10;
				bool flag=true;
				for(int j=0;j<k;j++)
				{
					flag=true;
					if(no==arr[j])
					{
						flag=false;
						break;
					}
				}
				if(flag==true)
				{
					arr[k++]=no;
				}
				p=p/10;
			}
		}
	}
}
