#include <stdio.h>
#include <string.h>

int main()
{
int p,q; scanf("%d",&p);

for(q=0;q<p;q++)
{
char s[105]; scanf("%s",&s);
int len,i,cnt=0,n_c=0,p_c=0; len=strlen(s);

for(i=0;i<len;i++)
	{
	if(s[i]=='+' && p_c==0) { n_c=0; p_c=1; cnt++; }
	else if(s[i]=='-' && n_c==0) { n_c=1; p_c=0; cnt++; }

	}
if(s[len-1]=='+') cnt--;

printf("Case #%d: %d\n",q+1,cnt);

}

return 0;
}
