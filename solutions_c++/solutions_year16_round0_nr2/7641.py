#include <bits/stdc++.h>
using namespace std;
char data[10000];
int t;
int idx=1;

int main()
{
    cin>>t;
    while(t--)
    {
        int cnt=0;
        scanf("%s",data);
        for(int i=strlen(data);i>=0;i--)
        {
            if(data[i]=='-')
            {
                cnt++;
                for(int j=i-1;j>=0;j--)
                {
                    if(data[j]=='+')
                    data[j]='-';
                    else
                    data[j]='+';
                }
            }
        }
        cout<<"Case #"<<(idx++)<<": "<<cnt<<endl;
    }
    
    return 0;
}