#include"header.h"

void sol(int T)
{
	for(int t=1;t<=T;t++)
	{
		int i,j,mid,k,ctr=0;
		char ch,str[101];
		cin>>str;
		int len = strlen(str);
		for(i=len-1;i>=0;i--)
		{
			if(str[i]=='-')
			{
				len = i+1;
				for(j=len-1;j>=0;j--)
				{
					if(str[0]==str[j])
					{
						for(k=j;k>=0;k--)
						{
							switch(str[k])
							{
								case '-':
								str[k] = '+';
								break;
								case '+':
								str[k] = '-';
								break;
								default:
								;
							}
						}
						mid = j/2;
						for(k=0;k<=mid;k++,j--)
						{
							ch = str[k];
							str[k] = str[j];
							str[j] = ch;
						}
						ctr++;
						break;
					}
				}
				i = len-1;
			}
		}
		cout<<"Case #"<<t<<": "<<ctr<<"\n";
	}
}