#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
char a[100][100];
int temp;
void rev(char a[],int s)
{
    for(int i=0;i<s/2;i++)
    {
        char temp=a[i];
        a[i]=a[s-i-1];
        a[s-i-1]=temp;
    }
    for(int i=0;i<s;i++)
    {
        if(a[i]=='+')
            a[i]='-';
        else
            a[i]='+';
    }
}
int main()
{
    int t,len,flag,temp,flag2,z,cnt[100];
    cin>>t;
    for(int j=0;j<t;j++)
    {
        flag=z=cnt[j]=0;
        cin>>a[j];
        len=strlen(a[j]);
        temp=len;
        while(flag!=temp)
        {
            flag=flag2=0;
            for(int i=0;i<temp;i++)
                if(a[j][i]=='-')
                    flag2++;
            if(flag2==temp-z)
            {
                for(int i=0;i<temp;i++)
                {
                    a[j][i]='+';
                }
                cnt[j]++;
            }
            else if(a[j][len-1]=='-')
            {
                if(a[j][0]!=a[j][len-1] && a[j][len-1]!=a[j][len-2])
                {
                    rev(a[j],len-1);
                    cnt[j]++;
                }
                else if(a[j][0]==a[j][len-1])
                {
                    rev(a[j],len);
                    cnt[j]++;
                }
                else
                    len--;
            }
            else if(a[j][len-1]=='+')
            {
                len--;
                z++;
            }
            for(int i=0;i<temp;i++)
                if(a[j][i]=='+')
                    flag++;
        }
    }
    for(int j=0;j<t;j++)
    {
    cout<<"Case #"<<j+1<<": "<<cnt[j]<<endl;
    }
}
