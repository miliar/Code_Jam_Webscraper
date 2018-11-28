#include<iostream>
#include<string.h>

using namespace std;



int main()
{
long long i,j,k,l,m,n,o,t;
cin>>t;
char str[101];
for(o=1;o<=t;o++)
{
cin>>str;
l=strlen(str);
cout<<"Case #"<<o<<": ";


for(i=0;;i++)
{
    for(j=0;j<l;j++)
        if(str[j]=='-')
            break;
    if(j==l)
        break;
if(str[0]=='+')
{

for(j=0;j<l&&str[j]=='+';j++)
str[j]='-';
}
else
{
for(j=0;j<l&&str[j]=='-';j++)
str[j]='+';

}


}
cout<<i<<endl;


}



}
