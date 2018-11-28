#include<bits/stdc++.h>

using namespace std;

main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    string s;
    int T,cs,i,j,x,flag,k,pos;

    cin>>T;

    for(cs=1;cs<=T;cs++)
    {
        x=0;
        k=0;
        cin>>s;
        flag = 1;
        for(i=0;i<s.size();)
        {
            j=0;
            while(s[i]=='+')
            {
                if(j==0)
                    x++;
                j++;
                i++;
                pos=0;
            }
            if(j==s.size())
            {
                k=1;
                cout<<"Case #"<<cs<<": 0"<<endl;
                break;
            }
            j=0;
            while(s[i]=='-')
            {
                if(i==0)
                    flag=0;
                if(j==0)
                    x++;
                j++;
                i++;
                pos=1;
            }


        }
        if(flag==0&&x==2&&k==0)
            cout<<"Case #"<<cs<<": 1"<<endl;
        else if(pos==0&&k==0)
            cout<<"Case #"<<cs<<": "<<x-1<<endl;
        else if(k==0)
            cout<<"Case #"<<cs<<": "<<x<<endl;
    }

    return 0;
}
