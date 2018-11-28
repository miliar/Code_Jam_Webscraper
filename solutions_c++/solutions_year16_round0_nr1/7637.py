#include<bits/stdc++.h>
#include<string>
using namespace std;

int to_string(long long value, char* buffer, int bufsz )
{
    if( value < 0 && bufsz > 2 )
    {
        value = -value ;
        buffer[0] = '-' ;
        int n = to_string( value, buffer+1, bufsz-1 ) ;
        if( n != -1 ) return n+1 ;
    }

    else if( value < 10  && bufsz > 1 )
    {
        buffer[0] = value + '0' ;
        buffer[1] = 0 ;
        return 1 ;
    }

    else
    {
        int digit = value%10 ;
        int n = to_string( value/10, buffer, bufsz-1 ) ;
        if( n != -1 && bufsz > (n+1) )
        {
            buffer[n] = digit + '0' ;
            buffer[n+1] = 0 ;
            return n+1 ;
        }
    }

    buffer[0] = 0 ;
    return -1 ;
}

int main()
{
	fstream fin("A-large.in",ios::in);
	fstream fout("outp.txt",ios::out);
	int t;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		long long int n;
		fin>>n;
		char num[1000000];
		to_string(n,num,1000000);
		int count=0;		
		int arr[10]={0};
		long long int j=0;
		for(;j<10000000;j++)
		{
			for(int k=0;k<strlen(num);k++)
			{
				if(!arr[num[k]-'0'])
				{
					count++;
					arr[num[k]-'0']=1;
				}
			}
			if(count==10)
				break;
			long long int o=n*(j+1);
			to_string(o,num,1000000);
		}
		if(count==10)
			fout<<"Case #"<<i+1<<": "<<num<<endl;
		else
			fout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
	}
	return 0;
}
