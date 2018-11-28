#include<iostream>
#include<fstream>
using namespace std;
int checkarray(int flags[10])
{
	for(int i=0;i<10;i++)
	{
		if(flags[i]==0)
		return 0;
	}
return 1;
}
int main()
{
int t;
ifstream infile;
infile.open("A-large.in",ios::in);
infile>>t;
int arr[t];
int res[t];
int i;
for(i=0;i<t;i++)
{
	infile>>arr[i];
	if(arr[i]==0)
	res[i]=-1;	
	else
	{
		int flags[10]={0};
		int temp;
		int j=1;
			while(1)
			{
				int temp=arr[i]*j;
				int r;
				while(temp>0)
				{
				r=temp%10;
				temp=temp/10;
				if(flags[r]==0)
				flags[r]=1;
				else
				continue;
				}
				if(!checkarray(flags))
				{
					
					j++;
				}
				else
				break;
			}
			
						
		res[i]=j*arr[i];		
		}
		
	}
infile.close();
ofstream outfile;
outfile.open("sleepoutput.txt",ios::out);

for(i=0;i<t;i++)
{
if(res[i]==-1)
outfile<<"Case #"<<i+1<<": "<<"INSOMNIA\n";
//cout<<"Case #"<<i+1<<": "<<"INSOMNIA\n";
else
outfile<<"Case #"<<i+1<<": "<<res[i]<<"\n";	
//cout<<"Case #"<<i+1<<": "<<res[i]<<"\n";
}
outfile.close();
return 0;	
}
