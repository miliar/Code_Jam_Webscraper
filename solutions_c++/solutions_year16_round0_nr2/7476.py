#include<iostream>
#include<string.h>
using namespace std;
void pap(int *a,int g)
{
    for(int i=0;i<=g;i++)
    {
        a[i]=!a[i];

        }

}
int main()
{
int n;
cin>>n;
for(int t=0;t<n;t++)
{
char s[100];
int i[100],c=0,g;
cin>>s;

while(c<strlen(s))
{
    if(s[c]=='+')
        i[c]=1;
    else
        {i[c]=0;
        g=c;
        }
    c++;
}
c=0;
while(g>=0)

{while(i[g]!=0&&g>=0)
{
g--;
}
if(i[g]==0)
{pap(i,g);
c++;
}
}
cout<<"Case #"<<t+1<<": "<<c<<"\n";;
}

return 0;
}
