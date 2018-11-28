#include<iostream>
#include<string.h>

using namespace std;
int main()
{
    int t, len; char s[1100], s1[1100], temp;
    cin>>t;
    for(int j=0; j<t; j++)
    {
        cin>>s;
        len=strlen(s);
        for(int i=0; i<len; i++)
        {
             if(s[i]>=s1[0])
             {
                 for(int x=0; x<i+1; x++)
                 {
                    temp=s1[i-x-1];
                    s1[i-x]=temp;
                 }
                s1[0]=s[i];
                s1[i+1]='\0';

             }
             else
             {
                s1[i]=s[i];
                s1[i+1]='\0';
             }
        }
        cout<<"Case #"<<j+1<<": "<<s1<<endl;
        for(int i=0; i<len; i++)
        {
            s1[i]='\0';
        }
    }
    return 0;


}
