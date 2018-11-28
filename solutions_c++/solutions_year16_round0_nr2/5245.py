#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    int num=1;
    string str;
    cin>>t;
    while(t--)
    {
        cin>>str;
        int  k =str.length();
        int cnt=0;
        for(int i=1;i<k;i++)
        {
           if(str[i]!=str[i-1])
                ++cnt;
        }
        if(str[k-1]=='+')
            printf("Case #%d: %d\n",num,cnt);
        else
            printf("Case #%d: %d\n",num,(cnt+1));
            ++num;

    }
}
