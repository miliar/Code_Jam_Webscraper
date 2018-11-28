#include<iostream>
#include<math.h>
#include<string.h>

char * strrev(char *str)

{

    int i = strlen(str)-1,j=0;

    char ch;
    while(i>j)
    {
        ch = str[i];
        str[i]= str[j];
        str[j] = ch;
        i--;
        j++;
    }
    return str;
}

using namespace std;
int main()
{
	long long int t,p=1,i;
cin>>t;
	while(t--)
	{	char str[1000000],*str2;
		cin>>str;
		long long int count=0,flag=0;
		str2=strrev(str);

		for(i=0;str2[i]!='\0';i++)
		{
			if(str2[i]=='-'&&flag==0)
				{count++;
				flag=flag^1;
				}

			if(str2[i]=='+'&&flag==1)
				{
					count++;
					flag=flag^1;
				}
		}


		cout<<"Case #"<<p<<": "<<count<<"\n";
		p++;

	}	

	return	0;

}