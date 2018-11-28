#include<bits/stdc++.h>
using namespace std;
int main()
{
	int l,t,n,i,j,k,c;
	FILE *ptr,*ptr1;
	ptr=fopen("A1-large.in","r+");
	ptr1=fopen("A1-large2.in","w+");
	fscanf(ptr,"%d",&t);
//	printf("%d\n",t);
	char s[2009];
	int b[]={0,2,4,6,8,1,3,5,7,9};
	char st[][20]={"ZERO","TWO","FOUR","SIX","EIGHT","ONE","THREE","FIVE","SEVEN","NINE"};
	for(k=1;k<=t;k++)
	{
		char v[2009];
		l=0;
		int a[29]={0};
		fscanf(ptr,"%s",&s);
		//printf("%s\n",s);
		for(i=0;s[i];i++)
		{
			a[s[i]-'A']+=1;
		}
		for(i=0;i<10;i++)
		{
			while(1)
			{
				c=0;
				for(j=0;st[i][j];j++)
				{
					if(a[st[i][j]-'A']<1)
					{
						c=1;
						break;
					}
				}
				if(c==1)
				{
					break;
				}
				else
				{
		//			printf("%d\n",b[i]);
					for(j=0;st[i][j];j++)
					{
						a[st[i][j]-'A']-=1;	
					}	
					v[l++]=b[i]+'0';
				}
			}
		}
		v[l]='\0';
		sort(v,v+l);
		//printf("%s\n",v);
		fprintf(ptr1,"Case #%d: %s\n",k,v);
	}
	return 0;
}

