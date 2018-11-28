#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int t;
   // cout<<"Enter the number of test cases :";
    cin>>t;
    for(int e=1;e<=t;e++)
    {


    char str[101];
   // cout<<endl<<"Enter the string ";
    cin>>str;
    int len=strlen(str);
    int *cp=new int[len];
    for(int l=0;l<len;l++)
    {
        cp[l]=0;
    }
    for(int i=0;i<len;i++)
    {
        if(str[i]=='+')
        {
            cp[i]=1;
        }


    }

    int ans=0;
    while(1)
    {
        int sum=0,num1=0,ct,c=0;

        for(int k=0;k<len;k++)
        {
            sum=sum+cp[k];
        }
        if(sum==len)
        {
            break;
        }
        else if(sum==0)
        {
            ans=ans+1;
            break;
        }
        num1=cp[0];
        for(int s=0;s<len;s++)
        {
            if(cp[s]!=num1)
            {
                ct=cp[s];
                c=s;
                break;
            }

        }
        for(int h=0;h<c;h++)
        {
            cp[h]=ct;

        }
        ans=ans+1;
    }
    cout<<"Case #"<<e<<": "<<ans<<endl;
    }

    return 0;
}
