#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;



int main()
{
long long i,j,k,l,h,m,n,o,t,c,s;
char str[2003];
cin>>t;
for(o=1;o<=t;o++)
{
    int fq[10]={0};
    int alpha[26]={0};
cin>>str;
cout<<"Case #"<<o<<": ";
long long len=strlen(str);
for(i=0;i<len;i++)
    alpha[str[i]-'A']++;
if(alpha[25]!=0)
{
    j=alpha[25];
    fq[0]+=j;
    alpha['Z'-'A']-=j;
    alpha['E'-'A']-=j;
    alpha['R'-'A']-=j;
    alpha['O'-'A']-=j;
}
if(alpha['X'-'A']!=0)
{
    j=alpha['X'-'A'];
    fq[6]+=j;
    alpha['S'-'A']-=j;
    alpha['I'-'A']-=j;
    alpha['X'-'A']-=j;
}



if(alpha['G'-'A']!=0)
{
    j=alpha['G'-'A'];
    fq[8]+=j;
    alpha['E'-'A']-=j;
    alpha['I'-'A']-=j;
    alpha['G'-'A']-=j;
    alpha['H'-'A']-=j;
    alpha['T'-'A']-=j;
}

if(alpha['W'-'A']!=0)
{
    j=alpha['W'-'A'];
    fq[2]+=j;
    alpha['T'-'A']-=j;
    alpha['W'-'A']-=j;
    alpha['O'-'A']-=j;

}
if(alpha['S'-'A']!=0)
{
    j=alpha['S'-'A'];
    fq[7]+=j;
    alpha['S'-'A']-=j;
    alpha['E'-'A']-=j;
    alpha['V'-'A']-=j;
    alpha['E'-'A']-=j;
    alpha['N'-'A']-=j;
}
if(alpha['V'-'A']!=0)
{
    j=alpha['V'-'A'];
    fq[5]+=j;
    alpha['F'-'A']-=j;
    alpha['I'-'A']-=j;
    alpha['V'-'A']-=j;
    alpha['E'-'A']-=j;

}
if(alpha['I'-'A']!=0)
{
    j=alpha['I'-'A'];
    fq[9]+=j;
    alpha['N'-'A']-=j;
    alpha['I'-'A']-=j;
    alpha['N'-'A']-=j;
    alpha['E'-'A']-=j;

}
if(alpha['N'-'A']!=0)
{
    j=alpha['N'-'A'];
    fq[1]+=j;
    alpha['O'-'A']-=j;
    alpha['N'-'A']-=j;
    alpha['E'-'A']-=j;

}
if(alpha['H'-'A']!=0)
{
    j=alpha['H'-'A'];
    fq[3]+=j;
    alpha['T'-'A']-=j;
    alpha['H'-'A']-=j;
    alpha['R'-'A']-=j;
    alpha['E'-'A']-=j;
    alpha['E'-'A']-=j;
}

if(alpha['R'-'A']!=0)
{
    j=alpha['R'-'A'];
    fq[4]+=j;
    alpha['F'-'A']-=j;
    alpha['O'-'A']-=j;
    alpha['U'-'A']-=j;
    alpha['R'-'A']-=j;

}


for(i=0;i<10;i++)
{
    j=fq[i];
    while(j--)
        cout<<i;
}

cout<<endl;


}



}
