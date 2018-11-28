#include<bits/stdc++.h>
char str[1000]={NULL};
char comp[1000]={NULL};
int rec();
int check(char arr[1000]);
void flip(char arr[1000], int ch);
int main()
{
//freopen("input.in","r",stdin);
//freopen("output.in","w",stdout);
int test,t;
scanf("%d",&test);
t=test;
while(test--)
{
  scanf("%s",str);
  printf("Case #%d: %d\n",t-test,rec());
}
}
int rec()
{
int i=0;
int k = check(str);
while(k!=0)
{
	if(str[0] == '-')
	{
		flip(str,0);
		i = i+1;
	}
	else
	{
		flip(str,1);
		i=i+2;
	}
	k = check(str);
}
return i;
}
int check(char arr[1000])
{
int i=strlen(arr)-1;
while(arr[i]=='+')
	i--;
arr[i+1]='\0';
return strlen(arr);
}
void flip(char arr[1000], int ch)
{
char b[1000] = {NULL};
int j=0,i;
	if(ch == 1)
	{
	while(arr[j]=='+')
	arr[j++] = '-';
	j=0;
	}
	for(i=strlen(arr)-1;i>=0;i--)
		{
			if(arr[i]=='-')
			b[j++] = '+';
			else
			b[j++] = '-';
		}
		b[j]='\0';
for(i=0;i<strlen(b);i++)
	str[i]=b[i];
    str[i]='\0';
}
