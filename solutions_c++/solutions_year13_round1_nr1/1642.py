#include <stdio.h>
#include <string.h>
void print_in_binary(int n)
{
char b[]="00000000";
int i;
for (i=0; i<8; i++, n=n/2)
{
if (n%2) b[7-i] = '1';
}

printf("%s", b);

return ;
}

int main()
{
int i,l;
char str[10000];

gets(str);

l=strlen(str);

for (i=0;i<l;i++)
print_in_binary(str[i]);

return 0;
}