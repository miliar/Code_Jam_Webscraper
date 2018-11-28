#include<bits/stdc++.h>
typedef long long int lli;
using namespace std;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif

    int tt;
    cin>>tt;
    for(int k=1; k<=tt; k++)
    {
        string str;
        cin>>str;
        int sz=str.length();
        int bck,j;
        for(j=sz-1; j>=0; j--)
        {
            if(str[j] == '-')
            {
                break;
            }
        }
        bck=j;
        // cout<<"Before bck="<<bck<<endl;
        int ans=0,cnt=4;
        if(bck == 0)
            ans=1;
        if(bck == -1)
            bck=0;
        while(bck)
        {
            ans++;
            if(str[0] == '-' && str[bck] == '-')
            {
                //flip
                for(int i=0,j=bck; i<=j; i++,j--)
                {
                    char temp;
                    temp=str[i];
                    str[i]=(str[j]=='-')?'+':'-';
                    str[j]=(temp == '-')?'+':'-';
                }


            }
            else
            {
                if(str[0] == '+')
                {
                    //flip unil there are +
                    for(int i=0; i<=bck; i++)
                    {
                        if(str[i] == '+')
                        {
                            str[i]='-';
                        }
                        else
                            break;
                    }
                }

            }

            //repositioing bck
            for(j=bck; j>=0; j--)
            {
                if(str[j] == '-' )
                {
                    break;
                }
            }
            bck=j;
            if(j == -1)
                bck=0;
            else if(j == 0)
            {
                ans++;
            }

            //displaying changes
          /*    cout<<"Step = "<<ans<<" ";
              for(int i=0; i<sz; i++)
              {
                  cout<<str[i];
              }
              cout<<endl;
              cout<<"bck="<<bck<<endl;*/


        }
        cout<<"Case #"<<k<<": ";
        cout<<ans<<endl;
    }
    return 0;
}
