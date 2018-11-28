#include<iostream>
#include<string.h>
#include<algorithm>
#include<cstdio>
using namespace std;


int main()
{
	char str1[200],str2[200];
	int T,cases=0,N,chng,i=0,j=0;
	int hash[26]={0};
	freopen("A-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	do
	{
		cases++;
		cout<<"Case #"<<cases<<":";
		chng = 0, i=0 ,j=0;
		cin>>N;
		scanf("%s%s",str1,str2);
		while( (i!= strlen(str1) || (j != strlen(str2))))
		{
			if(str1[i]==str2[j])
			{
					i++,j++;
			}
			
			else
			{
				if(str1[i]==str2[j-1])
				{
			
						chng++,i++;
						
				}
				
				else if(str1[i-1] == str2[j])
				{
						chng++,j++;
			
				}
				
				else
					{
						chng = -1;
			
						break;
					}
			}
			
		}
		if(chng == -1)
			cout<<" Fegla Won\n";
		else
			cout<<" "<<chng<<endl;
		
	}while(T!=cases);
}
