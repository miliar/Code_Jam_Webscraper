#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.o", "w", stdout);


    string s;
    int t,c=1;
    cin>>t;

    while(t--)
    {
        int flag = 0,l,co=0;
        cin>>s;
        l = s.size();
        if(s[0]=='-')flag = 1;
        for(int i =0; i<l-1;i++)
        {
            if(s[i] == '+' && s[i+1] == '-')
            {
                co++;
                i++;
            }
        }
        printf("Case #%d: %d\n",c++,co*2+flag);
    }
    return 0;
}
