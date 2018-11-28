#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;
#define cin fin
#define cout fout


int main()
{

	ifstream fin("a.in");
	ofstream fout("b.out");
	int T;
//	  scanf("%d",&T);
	cin>>T;
	int S;
	string s;
	int sum=0,c=0,i=0,j=1;
	while(j!=T+1)
	{
		cin>>S;
		cin>>s;
		while(sum<S)
		{
			
			
			if(sum<i)
				{	
					
					c+=i-sum;
					sum=i;
				}
			sum+=(int)(s[i]-'0');
		
		
					
			i++;
		}
		cout<<"Case #"<<j++<<": "<<c<<endl;
		sum=0; 
		c=0;
		i=0;
				
	}
	return 0;
}

