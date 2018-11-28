#include <stdio.h>
#include <string.h>
bool letter[26];
int main()
{
	FILE *in=fopen("a.in","r");
	FILE *out=fopen("a.out","w");
	letter['a'-'a']=1;
	letter['e'-'a']=1;
	letter['i'-'a']=1;
	letter['o'-'a']=1;
	letter['u'-'a']=1;
	long long cnt,useless,useful;int t,i,j,k,n,l;

	char s[1000010];
	fscanf(in,"%d",&t);
	for(i=0;i<t;i++)
	{
		cnt=0;useless=0,useful=0;
		
		fscanf(in,"%s",s);
		fscanf(in,"%d",&n);
		l=strlen(s);
		for(j=0;j<l;j++)
		{
			if(!letter[s[j]-'a'])
			{
				useful++;
				if(useful>=n)
				{
					cnt+=(long long)(l-j);
					if(useless>0)
						cnt+=(long long)useless*(long long)(l-j),useless=0;
					useful--;
				}
			}
			else 
			{
				useless++;
				if(useless>0)
				{
					useless+=useful;
					useful=0;
				}
			}
		}
		fprintf(out,"Case #%d: %lld\n",i+1,cnt);
	}
	return 0;
}

