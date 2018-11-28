#include<iostream>
#include<conio.h>

using namespace std;

int nvalue(char [], int);

void main()
{
	int T;
	char str[150];
	int n;

	cin>>T;

	for(int c=1;c<=T;c++)
	{
		cin>>str;
		cin>>n;

			
		cout<<"Case #"<<c<<": "<<nvalue(str,n)<<endl;;
	}


	_getch();
}


int nvalue(char str[], int n)
{

		int s;
		int k,c,len,con1,count,j;
		count =0;
		
	len=strlen(str);
	
	
	for(int c=n;c<=len;++c)
		{
			for(int s=0,k=s+c-1;k!=len;++s,++k)
			{
				con1=0;
				for(j=s;j<=k;++j)
				{
					switch(str[j])
					{
					case 'a':
					case 'e':
					case 'i':
					case 'o':
					case 'u':
					con1=0;
					break;

					default:++con1;

					}

					if(con1>=n)
					{
						++count;
						break;
					}
				}
			}
		}
	return count;
}






