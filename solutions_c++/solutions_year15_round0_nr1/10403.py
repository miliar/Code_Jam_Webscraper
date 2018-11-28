#include<iostream>
using namespace std;
struct shy
{
int s;
};
int main()
{
int i,j ,t ,count,a,diff;
cin>>t;
shy *sh=new shy[t];
int **ar=new int*[t];
char **str=new char*[t];
for(i=0;i<t;i++)
{
cin>>sh[i].s;
str[i]= new char[sh[i].s+1];
ar[i]=new int [sh[i].s+1];
cin>>str[i];
for(j=0;j<(sh[i].s+1);j++)
{
ar[i][j]=str[i][j]-48;
}
}
for(i=0;i<t;i++)
{
if(ar[i][sh[i].s]!=0)
{
a=0;
count=0;
for(j=0;j<(sh[i].s);j++)
{
a=a+ar[i][j];
if((a<j+1))
{
diff=(j+1)-a;
a=a+diff;
count=count+diff;
}
}
cout<<"Case #"<<i+1<<": "<<count<<"\n";
}
}
return 0;
}