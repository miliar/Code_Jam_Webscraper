#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<new>
#include<iomanip>
#include<fstream>
#include<cstring>
#include<stdio.h>
using namespace std;
char str[300],ch;
long long int isPalindrome( long long  a){
	    char buff[15] = {'\0'};
	 
	    long long int i, len;
	    sprintf(buff,"%lld",a);
	    len = strlen(buff);
	    for(i=0;i<len/2;i++){
        if(buff[i] != buff[len-i-1])
	            return 0;
	    }
	    return 1;
	}

int main()
{
	long long int n,m,i,count=0,j,k,t;
	char ch,s;
	//cout<<sizeof(a)<<i;
	//scanf("%d",&t);
	ifstream p("p.txt");
	ofstream o("pra.txt");
	p>>t;
	p.get(ch);
	
	for(k=1;k<=t;k++)
	{
		count=0;
		p>>n;p.get(ch);
		p>>m;p.get(ch);
		for(i=n;i<=m;i++)
		if(sqrt(i)==(long long int)sqrt(i))
		{
			//cout<<i<<";"<<sqrt(i)<<endl;
			if(isPalindrome(i)&&isPalindrome(sqrt(i)))		
				{
					count++;
					//o<<i<<" ";
				}
		}
		o<<"Case #"<<k<<": ";
		o<<count<<endl;
	}
	p.close();
	o.close();
	return 0;
}
