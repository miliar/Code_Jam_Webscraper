 #include<iostream>
#include<string.h>

#include<stdio.h>

using namespace std;

int main()
{int t;
cin>>t;
for(int z=1;z<=t;z++)
{char s[1000];
cin>>s;

char ans[1000]={'\0'};
ans[0]=s[0];
char k=0;
for(int i=1;s[i]!='\0';i++)
{if(s[i]>=ans[0])
{int x=k;
while(x>=0)
    {ans[x+1]=ans[x];
    x--;
    }
   ans[0]=s[i];
}
else
{ans[k+1]=s[i];
}
k++;
}
cout<<"Case #"<<z<<": "<<ans<<endl;}
}
