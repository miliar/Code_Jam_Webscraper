#include<iostream>
#include<string.h>
using namespace std;
int main()
{
char S[100][200];
int T,c,l;
cin>>T;
for(int x=0;x<T;x++)
cin>>S[x];
for(int i=0;i<T;i++)
{
c=0;
l=strlen(S[i]);
for(int j=l-1;j>=0;j--)
{
  if(S[i][j]=='-')
    { 
     for(int p=j;p>=0;p--)
     {
     if(S[i][p]== '-')
       S[i][p]= '+';
     else
       S[i][p]= '-';
     }
     c++;
    }
}
cout<<"Case #"<<i+1<<": "<< c<<endl;
}
return 0;
}
