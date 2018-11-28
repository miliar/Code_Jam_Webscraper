#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
int main(){
int count=0,state=0,n,i=0,t,j=1;
freopen("src.in","r",stdin);
freopen("src.out","w",stdout);

char a[100];
cin>>t;
while(t>0)
{ cout<<"Case #"<<j<<": ";  
state=count=i=0;
    cin>>a;
    n=strlen(a);
    while(i<n){

        if(a[i]=='+')
        {
            while(a[i]=='+'&&i<n)
            {state=0;
                i++;}

            while(a[i]=='-'&&i<n)
            {
                i++;state=6;
            }

            if(state==0)
               count=count;
            else
            count=count+2;
        }


        else
            {



        while(a[i]=='-'&&i<n)
        {
            i++;state=1;
        }
        while(a[i]=='+'&&i<n)
        {
            i++;state=2;
        }

        while(a[i]=='-'&&i<n)
        {
            i++;state=3;
        }

        if(state==1||state==2)
            count=count+1;
        else if(state==3)
            count=count+3;
            }

    }
    cout<<count<<endl;
j++;


t--;}
return 0;
}
