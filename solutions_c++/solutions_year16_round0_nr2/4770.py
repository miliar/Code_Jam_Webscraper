#include<bits/stdc++.h>
using namespace std;
char str[105];
int fun(int x,int flg)
{
    if(x==0){if(str[x]=='+'&&flg==0)return 1;
    else if(str[x]=='-'&&flg==1)return 1;
    else return 0;
    }
    if(str[x]=='+')
    {   if(flg==0)
        return fun(x-1,1)+1;
        else return fun(x-1,1);
    }
    else {
          if(flg==1)
        return fun(x-1,0)+1;
        else return fun(x-1,0); 
    }
    
    
}
int main()
{
    int t;
    int k=1;
    freopen("B-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        int i;
        
        cin>>str;
        cout<<"Case #"<<k++<<": ";
        
        int x= strlen(str);
        int j=x-1;int cnt=0;
        
        if(str[j]=='+'&&j>0)
         {cnt=fun(j-1,1);}
         else if(j>0)
         {
             cnt=fun(j-1,0)+1;
         }
         if(j==0){
            if(str[j]=='-')cnt=1;
         }
        cout<<cnt<<endl;
    }
    return 0;
}
