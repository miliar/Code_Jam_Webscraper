#include<iostream>
using namespace std;
int main()
{
    int a,i,j,chk,t,Smax;
    char s[1001];
    cin>>t;
    for(i=1;i<=t;i++)
    {
        chk=0;
    cin>>Smax;
    cin>>s;
    if(s!='\0')
        a=s[0]-'0';
    for(j=1;s[j]!='\0';j++)
    {
        if(a<j)
        {
            chk+=j-a;
            a=j;
            a+=s[j]-'0';

        }
        else
        {

            a+=s[j]-'0';
        }

    }
    cout<<"Case #"<<i<<": "<<chk<<endl;
}
return 0;
}
