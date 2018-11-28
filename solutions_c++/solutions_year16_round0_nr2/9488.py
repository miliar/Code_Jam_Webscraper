#include <iostream>
#include <stdio.h>
#include <math.h>
#include <map>
using namespace std;

void flip(char s[],int e)
{
    int i,j;
    char tmp;
    for(i=0,j=e;i<j;i++,j--)
    {
        tmp=s[i];
        s[i]=s[j];
        s[j]=tmp;
    }
    for (i = 0; i <= e; ++i)
    {
        if (s[i]=='-') s[i]='+';
        else s[i]='-';
    }
}

int main()
{
    int t,i,j,tmp;
    std::ios::sync_with_stdio(false);
    cin >> t;
    for (i = 1; i <= t; ++i) 
    {
        char s[105];
        cin >> s;
        int n=0,ans=0;
        for (j = 0; s[j]!='\0'; ++j) n++;
        if(n==1) 
        {
            if(s[0]=='-') cout << "Case #" << i << ": " << 1 <<endl;
            else cout << "Case #" << i << ": " << 0 <<endl;
            continue;
        }
        int curr=n-1;
        while (curr>=0 && s[curr]=='+') curr--;
        if(curr==-1)
        {
            cout << "Case #" << i << ": " << 0 <<endl;
            continue;
        }
        while(curr>=0)
        {
            if (s[0]=='-')
            {
                flip(s,curr);
                ans++;
                while (curr>=0 && s[curr]=='+') curr--;
            }
            else
            {
                int k=0;
                while(k<=curr && s[k]=='+') k++;
                if(k>curr) break;
                flip(s,k-1);
                ans++;
            }
            //cout << s << endl;
        }
        cout << "Case #" << i << ": " << ans <<endl;

    }
    return 0;
}