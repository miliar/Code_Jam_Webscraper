#include<bits/stdc++.h>
using namespace std;
bool chk(string str)
{
    for(int i=0;str[i];i++)
    {
        if(str[i]=='-')
            return 0;
    }
    return 1;
}
bool chk1(string str)
{
    for(int i=0;str[i];i++)
    {
        if(str[i]=='+')
            return 0;
    }
    return 1;
}
int main()

{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    string str;
    int i,t,len,cnt,j,x,y,iner;
    cin>>t;
    for(iner=1;iner<=t;iner++)
    {
        printf("Case #%d: ",iner);
        cin>>str;
        if(chk(str))
            cout<<"0";
        else if(chk1(str))
            cout<<"1";
        else
        {
            x=y=0;
            len=str.size();
            cnt=0;
            while(1)
            {
                cnt++;
                for(i=0;i<len-2;i++)
                {
                    if(str[i]==str[i+1])
                        continue;
                    else
                        break;
                }
                for(j=0;j<=i;j++)
                    str[j]=str[i+1];
                //cout<<str<<endl;
                if(chk(str))
                {
                    x=1;
                    break;
                }
                if(chk1(str))
                {
                    y=1;
                    break;
                }


            }
            if(x==1)
                cout<<cnt;
            else
                cout<<cnt+1;

        }
    cout<<endl;
    }
}
