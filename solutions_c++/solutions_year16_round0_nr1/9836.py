#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	fstream fin,fout;
	fin.open("aa.in",fstream::in);
	fout.open("out2.txt",fstream::out);
	unsigned long int x,ans;
	int T,i,o,n,temp;
	bool f;
	int count[10];
	o=1;
	fin>>T;
	while(T--)
	{
		fin>>x;
		n=1;
		for(i=0;i<10;i++)count[i]=0;
		if(x!=0)
		{
			while(1)
			
			{
				ans=x*n;
			temp=ans;
			while(temp>0)
			{
				if(temp!=0)
				count[temp%10]++;
				temp/=10;
			}
			if(count[0]>0)f=true;
				for(i=0;i<10;i++)
				{
					if(count[i]>0&&f)f=true;
					else f=false;
				}
				if(f)break;
				n++;
			}
				
		}
		else ans=0;
		if(ans!=0)
		fout<<"Case #"<<o<<": "<<ans<<endl;
		else
		fout<<"Case #"<<o<<": INSOMNIA"<<endl;
		o++;
	}
	
	fin.close();
	fout.close();
	return 0;
}
