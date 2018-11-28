#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("output1.txt","w",stdout);
    int cs;
    cin>>cs;
    for(int k=1;k<=cs;k++)
    {
        static char str[4000];
        int s=1999,e=2001;
        string in;
        cin>>in;
        str[2000]=in[0];
        for(int i=1;i<in.size();i++)
        {
            char ch=in[i];
            if(ch>=str[s+1])
            {
                str[s]=ch;
                s--;
            }
            else
            {
                str[e]=ch;
                e++;
            }
        }
        printf("Case #%d: ",k);
        for(int i=s+1;i<e;i++)
        {
            cout<<str[i];
        }
        cout<<endl;
    }
    return 0;
}
