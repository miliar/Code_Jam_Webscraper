#include<iostream>
#include<cctype>

using namespace std;

long tll(char *str,int size)
{
	long length=strlen(str);
	char *ss;
	ss=new char[1000000];
	long count=0;
	for(long i=0;i<length-size+1;i++)
	{
		for(long j=i+size-1;j<length;j++)
		{
			long index=0,flag=1;
			for(long s=i;s<=j;s++)
			{
				ss[index]=str[s];
				index++;
			}
			ss[index]=NULL;
			long con=0;
			for(long l=0;l<index;l++)
			{
				ss[l]=tolower(ss[l]);
				if(ss[l]=='a'||ss[l]=='i'||ss[l]=='e'||ss[l]=='u'||ss[l]=='o')
				{
					con=0;
				}
				else
				{
					con++;
					if(con>=size)
						break;
				}
			}
			if(con>=size)
				count++;
		}
	}
	return count;
}

int main()
{
	int t;
	long l,n;
	char *ch=new char[1000000];
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>ch;
		cin>>l;
		n=tll(ch,l);
		cout<<"Case #"<<i+1<<": "<<n<<endl;
	}
	return 0;
}