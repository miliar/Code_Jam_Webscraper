#include<bits/stdc++.h>
using namespace std;
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input1.in","r",stdin);
    freopen("output2.txt","w",stdout);
    #endif

    char str[1000]="";
    long long t,cnt=0,ctr,flag,i;
    long long len;

    cin>>t;
    while(t>0)
    {
        ctr=0;
        flag=1;
        gets(str);
        len = strlen(str);
        if(str[0]=='+' || str[0]=='-')
        {
            cnt++;
                while(1)
                {
                    i=0;
                    if(str[i]=='+')
                    {
                        while(str[i]=='+')
                        {
                            i++;
                            if(i==len )
                            {
                                flag=0;
                                break;
                            }
                        }
                        if(flag==0)
                            break;
                    }
                    else
                    {
                        while(str[i]=='-')
                        {
                            i++;
                        }
                    }
                    if(str[i]=='+' || i==len)
                    {
                        for(int j=0;j<i;j++)
                        {
                            str[j]='+';
                        }
                        ctr++;
                    }
                    else
                    {
                        for(int j=0;j<i;j++)
                        {
                            str[j]='-';
                        }
                        ctr++;
                    }

                }
                cout<<"Case #"<<cnt<<": "<<ctr<<"\n";
                t--;
        }

    }

}
