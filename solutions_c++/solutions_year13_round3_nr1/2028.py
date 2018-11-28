#include<iostream>
#include<cctype>

using namespace std;

long fun(char *str,int k)
{
	long length=strlen(str);
	char sub[1000];
	long count=0;
	for(long i=0;i<length-k+1;i++)
	{
		for(long j=i+k-1;j<length;j++)
		{
			long index=0,flag=1;
			for(long s=i;s<=j;s++)
			{
				sub[index]=str[s];
				index++;
			}
			sub[index]=NULL;
			long con=0;
			for(long l=0;l<index;l++)
			{
				sub[l]=tolower(sub[l]);
				if(sub[l]=='a'||sub[l]=='i'||sub[l]=='e'||sub[l]=='u'||sub[l]=='o')
				{
					con=0;
				}
				else
				{
					con++;
					if(con>=k)
						break;
				}
			}
			//cout<<sub<<"  "<<con<<endl;
			if(con>=k)
				count++;
		}
	}
	return count;
}
int main()
{
	int t;
	long k,n;
	char str[1000];
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>str;
		cin>>k;
		n=fun(str,k);
		cout<<"Case #"<<i+1<<": "<<n<<endl;
	}
	return 0;
}