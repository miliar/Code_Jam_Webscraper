#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int>pp;
typedef long long ll;

int main()
{
    int t;
    scanf("%d",&t);
    for(int counting=1; counting<=t; counting++)
    {
        int c=0;
        string s;
        cin>>s;
        int n= s.length();
        bool flag;
        if(n==0)
        {
            printf("Case #%d: %d\n",counting,0);
            continue;
        }
        else
        {
            flag=(s[0]=='+')?(true):(false);
            int i=1;
            while(i<n)
            {
                int j=i;
                while(j<n)
                {
                    if(s[j]=='+' && !flag)
                    break;
                    else if(s[j]=='-' && flag)
                    break;
                    else j++;


                }
                if(j==n)
                {
                    i=n; break;
                }
                else
                {
                    c++;
                    flag= !flag;
                    i=j;

                }
            }
        }
        if(!flag) c++;
        printf("Case #%d: %d\n",counting,c);
    }


return 0;
}
