#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define lli long long int
char s[100000];

int main()
{
freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
    lli t,i,n,st,count,add,j=1;
    cin>>t;
    while(t--)
    {
              cin>>n;
              scanf("%s",s);
              //cout<<s;
              n++;
              st=s[0]-48;count=0;
              
              for(i=1;i<n;i++)
              {//cout<<"st"<<st;
              add=0;
                              if(st<(i))
                              {//cout<<"id" ;
                                              count+=(i-st);
                                              add=i-st;
                              }
                              st+=s[i]-48+add;
              }
              
              cout<<"Case #"<<j<<": "<<count<<endl;
              j++;
    }
    
    return 0;
}
              
