#include<iostream>
using namespace std;
int main()
{
    int t,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        int s;
        cin>>s;
        char str[s+2];
        cin>>str;
        int cot=str[0]-48,dif=0,f=0,i;
        for(i=1;i<s+1;i++)
        {
            if(str[i]-48!=0)
            {
                if(cot>=i)
                    cot+=str[i]-48;
                else
                {
                    dif=i-cot;
                    f+=dif;
                    cot+=dif+str[i]-48;
                }
            }
        }
        cout<<"Case #"<<j<<": "<<f<<endl;
    }
    return 0;
}
