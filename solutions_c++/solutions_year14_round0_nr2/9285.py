#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <iomanip>
using namespace std;
string pre[105];
string las[105];
string lisen[105];

int main(int argc, char *argv[])
{
int t,n,m,case_num = 1;
char s[200],s1[20];
cin>>t;
while(t--)
{
cin>>n>>m;
for(int i = 0; i < m; i++ )
cin>>pre[i]>>las[i];
cin.get();
gets(s);
int j = 0,k = 0;
for(i = 0; i < strlen(s); i++)
{
if(s[i]==' ')
{
s1[k] = '\0';
lisen[j++] = s1;
k = 0;
i++;
}
s1[k++] = s[i];
}
s1[k] = '\0';
lisen[j++] = s1;
n = n-1;
while(n--)
{
for(int i = 0; i < j; i++)
{
for(int k = 0; k < m; k++)
{
if(pre[k] == lisen[i])
{
//cout<<"change "<<pre[k]<<" to "<<las[k]<<endl;
lisen[i] = las[k];
break;
}	
}
}
}
cout<<"Case #"<<case_num++<<": ";
for(i = 0; i < j-1; i++)
cout<<lisen[i]<<" ";
cout<<lisen[j-1]<<endl;
}
return 0;
}