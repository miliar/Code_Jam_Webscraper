#include<bits/stdc++.h>
using namespace std;
int freq[110][110][2];
int main()
{
    int t,i,j,k,l,m,n,o,p;
    char ch;
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>j;
        memset(freq,0,sizeof(freq));
        string str[j];
        for(k=0;k<j;k++)
        cin>>str[k];
        m=0;
        for(k=0;k<j;k++)
        {
            n=0;m=0;
            ch=str[k][0];
            freq[k][m][0]=int(ch);
            for(l=0;l<str[k].length();l++)
            {
                if(str[k][l]==ch)
                {
                    n++;
                }
                else
                {
                    freq[k][m][1]=n;
                 //   cout<<k<<" "<<m<<" "<<freq[k][m][0]<<" "<<freq[k][m][1]<<endl;
                    m++;
                    n=1;
                    ch=str[k][l];
                    freq[k][m][0]=(int)ch;
                }
            }
            freq[k][m][0]=(int)ch;
            freq[k][m][1]=n;
           // cout<<k<<" "<<m<<" "<<freq[k][m][0]<<" "<<freq[k][m][1]<<endl;
        }
        int ans=0;
        for(l=0;l<=100;l++)
        {
            m=freq[0][l][0];
            n=0;
            for(k=0;k<j;k++)
            {
             //   cout<<m<<" "<<freq[k][l][0]<<endl;
                if(m!=freq[k][l][0])
                {
                    cout<<"Case #"<<i+1<<": Fegla Won"<<endl;
                    goto x;
                }
                else
                n+=freq[k][l][1];
            }
            n/=j;
            o=0;m=0;
            for(k=0;k<j;k++)
            {
                o+=abs(freq[k][l][1]-n);
                m+=abs(freq[k][l][1]-n-1);
            }
           // cout<<o<<" "<<m<<endl;
            ans+=min(o,m);
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
        x:
        ;
    }
    return 0;
}

