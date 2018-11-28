#include <bits/stdc++.h>

using namespace std;

int main()
{
int t;
cin >>t;
int w=1;
while(t--)
{
char s[2001];
cin >> s;
int a[10];
for(int y=0;y<10;y++)
{
    a[y]=0;
}


int i=0;
while(s[i]!='\0')
{
if(s[i]=='Z')
{
   a[0]++;
}
else if(s[i]=='O')
{
    a[1]++;
}
else if(s[i]=='W')
{
    a[2]++;
}
else if(s[i]=='H')
{
    a[3]++;
}
else if(s[i]=='U')
{
    a[4]++;
}
else if(s[i]=='F')
{
    a[5]++;
}
else if(s[i]=='X')
{
    a[6]++;
}
else if(s[i]=='S')
{
    a[7]++;
}
else if(s[i]=='G')
{
    a[8]++;
}
else if(s[i]=='I')
{
    a[9]++;
}
i++;
}
a[3]=a[3]-a[8];
a[1]=a[1]-a[0]-a[2]-a[4];
a[5]=a[5]-a[4];
a[7]=a[7]-a[6];
a[9]=a[9]-a[5]-a[6]-a[8];

cout<<"Case #"<<w<<": ";
for(int j=0;j<10;j++)
{
for(int k=0;k<a[j];k++)
{
    cout << j;
}
}

cout<<endl;
w++;

}
    return 0;
}
