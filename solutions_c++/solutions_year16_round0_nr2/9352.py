#include<iostream>
using namespace std;
int RFIND(char t[101],char val)
{
    int i,flag=0;
    for(i=strlen(t)-1;i>=0;i--)
    if(t[i]==val)
    {
    flag=1;
    break;
    }
    if(flag==1)
    return i+1;
    else
    return 0;
}
int main()
{
    int T,i,index=0,count=0,pos,k,output[101];
    char s[101],ns[101];
    cin>>T;
    for(k=0;k<T;k++)
    {
    cin>>s;
    index=count=0;
    while(pos=RFIND(s,'-'))
    {
    pos--;
    for(i=0;i<=pos;i++)
    {
    if(s[i]=='+')
    s[i]='-';
    else
    s[i]='+';
    ns[i]=s[i];
    }
    ns[i]='\0';
    strrev(ns);  
    index=strlen(ns); 
    for(i=pos+1;i<strlen(s);i++)
    ns[index++]=s[i];
    ns[index]='\0';
    count++;
    }
    output[k]=count;
    }
    for(i=0;i<T;i++)
    cout<<"Case #"<<i+1<<":  "<<output[i]<<endl;
    return 0;
}



