#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

#define LL long long

using namespace std;

bool vowel(char c)
{
    if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
        return true;
    return false;
}

int main()
{
    int T, n, i, j;
    char s[105];
    int sum, c;
    int prev=-1;
    cin>>T;
    c=1;
    while(T--)
    {
        sum=0; prev=-1;
        cout<<"Case #"<<c++<<": ";
        cin>>s;
        cin>>n;
        i=0;
        while(i<strlen(s))
        {
            for(j=i; j<n+i && s[j]; j++)
            {
                if(vowel(s[j]))
                {
                    i=j+1;
                    //prev=i;
                    break;
                }
                //cout<<j<<' ';
            }
            if(j==n+i)
            {
                //if(!flag)
                //{
                    sum+=((i-prev)*(strlen(s)-j+1));
                  //  flag=true;
                //}
                //else
                  //  sum+=(strlen(s)-j+1);
                  prev=i;
                i++;
            }
            if(j>=strlen(s))
                break;
        }
        cout<<sum<<'\n';
    }
    return 0;
}
