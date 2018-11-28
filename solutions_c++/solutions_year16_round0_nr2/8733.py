#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
void main()
{
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
	int t=1,r;
	cin>>r;
	while(t<=r)
	{
		string s;
		int i,l=0,k=0,c=0;
		cin>>s;
		for(i=0;s[i]!='\0';i++);
		l=i-1;
		while(l>=0)
		{
			if(s[l]=='-')		
				{
					for(k=l;k>=0;k--)
					{
						
						if(s[k]=='+')
						{
						s[k]='-';
						}
						else
						{
						s[k]='+';
						}	
					}
					c=c+1;
				}	
					l=l-1;
			}		
			cout<<"Case #"<<t<<": "<<c<<"\n";
			t=t+1;
		}
		
		
	}

	

