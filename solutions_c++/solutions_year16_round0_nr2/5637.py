#include<bits/stdc++.h>
using namespace std;
int isLeft(char s[])
{
    for(int i=0;i<strlen(s);i++)
    {
        if(s[i]=='-')
        return 1;
    }
    return 0;
}
void flip(char* s,int l,int h)
{
    for(int i=l;i<h;i++)
    {
        if(s[i]=='+')
        s[i]='-';
        else
        s[i]='+';
    }

}

int main()
{
    long long int t,l,n,i,z=0;
    cin>>t;
    char s[101];
    while(z<t)
    {
        z++;
        scanf("%s",s);
        printf("Case #%lld: ",z);
        l=strlen(s);
        n=0;
        if(l==1)
        {

        }
        while(isLeft(s))
        {
            char c=s[0];
            for(i=0;i<l;i++)
            {
                if(s[i]==c)
                {
                    if(i==l-1)
                    {
                        n++;
                        flip(s,0,l);
                    }
                    else
                    continue;
                }

                else
                {

                    flip(s,0,i);
                    n++;
                    break;
                }

            }
        }
        cout<<n<<endl;
    }

    return 0;
}
