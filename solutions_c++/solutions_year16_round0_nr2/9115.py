#include <iostream>
#include<string.h>
#include<bits/stdc++.h>

using namespace std;
void flip(char s[],int j)
{
    int i=0;
    while(i<=j)
    {
        char t1=s[i];
        char t2=s[j];
        if(t1=='-')
            s[j]='+';
        else
            s[j]='-';
        if(t2=='-')
            s[i]='+';
        else
            s[i]='-';
        i++;
        j--;
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("codekrle.o","w",stdout);
    int t;
    cin>>t;
    int i;
    for(i=1;i<=t;i++)
    {
        char str[200];
        cin>>str;
        int l=strlen(str);
        int count=0;
        if(l==1)
        {
            if(str[0]=='-')
                cout<<"Case #"<<i<<": 1"<<endl;
            else
                cout<<"Case #"<<i<<": 0"<<endl;
            continue;
        }
        int j=0,k=l-1;
        while(j<k)
        {
            while(str[j]=='-')
                j++;
            if(j>0)
            {
                flip(str,j-1);
                count++;
            }
            while(str[k]=='+')
                k--;
            if(str[0]=='+')
            {
                while(str[j]=='+')
                    j++;
                if(j<=k){
                    flip(str,j-1);
                    count++;
                }
            }
            if(k>=j)
            {
                flip(str,k);
                count++;
            }
            else
                break;
            j=0;
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}
