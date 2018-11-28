#include<bits/stdc++.h>

using namespace std;

int main()
{
    FILE *fin = freopen("input.txt","r",stdin);
    FILE *fout = freopen("output.txt","w",stdout);

    char s[105];
    int len,count,t,j=1,i;

    cin>>t;
    while(j<=t)
    {
        cin>>s;
        len=strlen(s);
        count=0;

        if(s[0]=='-')
            count++;

        for(i=1;i<len;i++)
        {
            if(s[i]=='-' && s[i-1]=='+')
            {
                count+=2;
            }
        }
        cout<<"Case #"<<j<<": "<<count<<endl;
        j++;
    }
    return 0;
}
