#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int isempty(int A[26])
{
    int x=0;
    for(int i=0;i<26;i++)
    {
        if(A[i]==0)
        x++;
    }
    if(x==26)
    return 1;
    else 
    return 0;
}
int main()
{
int t;
cin>>t;
int r=t;
while(t>0)
{
int A[26]={0};
int B[2000],c=0;
char S[3000];
cin>>S;
int n=strlen(S);
for(int i=0;i<n;i++)
A[S[i]-'A']++;
//for(int i=0;i<26;i++)
//cout<<A[i]<<" ";
//cout<<endl;
while(1){
int y=isempty(A);
//cout<<"y="<<y<<endl;
if(y==1)
break;
//for(int i=0;i<26;i++)
//cout<<A[i]<<" ";
//cout<<endl;
if(A[23]!=0)
{
B[c]=6;
c++;
A[23]--;
A[18]--;
A[8]--;
}
else if(A[25]!=0)
{
B[c]=0;
c++;
A[25]--;
A[4]--;
A[17]--;
A[14]--;
}
else if(A[6]!=0)
{
B[c]=8;
c++;
A[4]--;
A[8]--;
A[6]--;
A[7]--;
A[19]--;
}
else if(A[22]!=0)
{
B[c]=2;
c++;
A[22]--;
A[19]--;
A[14]--;
}
else if(A[20]!=0)
{
B[c]=4;
c++;
A[5]--;
A[14]--;
A[20]--;
A[17]--;
}
else if(A[14]!=0)
{
B[c]=1;
c++;
A[14]--;
A[13]--;
A[4]--;
}
else if(A[19]!=0)
{
B[c]=3;
c++;
A[19]--;
A[7]--;
A[17]--;
A[4]-=2;
}
else if(A[5]!=0)
{
B[c]=5;
c++;
A[5]--;
A[8]--;
A[21]--;
A[4]--;
}
else if(A[18]!=0)
{
B[c]=7;
c++;
A[18]--;
A[4]-=2;
A[21]--;
A[13]--;
}
else if(A[13]!=0)
{
B[c]=9;
c++;
A[13]-=2;
A[8]--;
A[4]--;
}
}
sort(B,B+c);
cout<<"Case #"<<r-t+1<<": ";
for(int i=0;i<c;i++)
cout<<B[i];
cout<<endl;
t--;
}
return 0;
}
