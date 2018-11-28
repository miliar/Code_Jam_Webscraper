#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("CJ_large_1","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        int A[500]={0},cou=0;
        string s,ans="";
        cin>>s;
        int i,n=s.length();
        for(i=0;i<n;i++)
        {
            A[s[i]]++;
        }

            if(A['Z']>0)
            {
                int u=A['Z'];
                for(i=0;i<A['Z'];i++)
                {
                    ans=ans+'0';
                }
                A['E']-=u;
                cou+=u;
                A['R']-=u;

                A['O']-=u;

                A['Z']-=u;
                cou+=u;
            }
            if(A['W']>0)
            {
                int u=A['W'];
                for(i=0;i<A['W'];i++)
                {
                    ans=ans+'2';
                }
                A['T']-=u;
                cou+=u;
                A['W']-=u;
                cou+=u;
                A['O']-=u;
                cou+=u;
            }
            if(A['G']>0)
            {
                int u=A['G'];
                for(i=0;i<A['G'];i++)
                {
                    ans=ans+'8';
                }
                A['E']-=u;
                cou+=u;
                A['I']-=u;

                A['G']-=u;

                A['H']-=u;

                A['T']-=u;

            }
            if(A['X']>0)
            {
                int u=A['X'];
                for(i=0;i<A['X'];i++)
                {
                    ans=ans+'6';
                }
                A['I']-=u;
                cou+=u;
                A['S']-=u;

                A['X']-=u;

            }
            if(A['S']>0)
            {
                int u=A['S'];
                for(i=0;i<A['S'];i++)
                {
                    ans=ans+'7';
                }
                A['S']-=u;
                cou+=u;
                A['E']-=u;

                A['V']-=u;

                A['E']-=u;

                A['N']-=u;

            }
            if(A['U']>0)
            {
                int u=A['U'];
                for(i=0;i<A['U'];i++)
                {
                    ans=ans+'4';
                }
                A['F']-=u;
                cou+=u;
                A['O']-=u;

                A['U']-=u;

                A['R']-=u;


            }
            if(A['R']>0)
            {
                int u=A['R'];
                for(i=0;i<A['R'];i++)
                {
                    ans=ans+'3';
                }
                A['T']-=u;
                cou+=u;
                A['H']-=u;

                A['R']-=u;

                A['E']-=u;

                A['E']-=u;

            }
            if(A['F']>0)
            {
                int u=A['F'];
                for(i=0;i<A['F'];i++)
                {
                    ans=ans+'5';
                }
                A['F']-=u;
                cou+=u;
                A['I']-=u;

                A['V']-=u;

                A['E']-=u;

            }
            if(A['I']>0)
            {
                int u=A['I'];
                for(i=0;i<A['I'];i++)
                {
                    ans=ans+'9';
                }
                A['N']-=u;
                cou+=u;
                A['I']-=u;

                A['N']-=u;

                A['E']-=u;

            }
            if(A['O']>0)
            {
                int u=A['O'];
                for(i=0;i<A['O'];i++)
                {
                    ans=ans+'1';
                }
                A['O']-=u;
                cou+=u;
                A['N']-=u;

                A['E']-=u;

            }
        int l=ans.length();
        sort(ans.begin(),ans.end());
        printf("Case #%d: ",cas);
        cout<<ans<<endl;
        cas++;
    }
    return 0;
}
