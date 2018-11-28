#include <bits/stdc++.h>

using namespace std;

int where(char s[],int l)
{int i;
for(i=0;i<l-1;i++)
{
if(s[i]!=s[i+1])
{
    break;
}
}
return i;
}

void change(char s[],int p)
{
if(s[0]=='-')
{for(int i=0;i<p;i++)
{

    s[i]='+';
}
}
else
{for(int i=0;i<p;i++)
{

    s[i]='-';
}
}
}
int main()
{
int t;
cin >> t;
int y=1;
while(t--)
{
char s[101];
cin >> s;
int c=0;
int h=0;
while(s[h]!='\0')
{
h++;
}

for(int i=0;i<h-1;i++)
{
if(s[i]!=s[i+1])
{
c++;
}
}



if(s[h-1]=='-'){c++;}

cout<<"Case #"<<y<<": "<<c<<endl;

y++;
}
}
