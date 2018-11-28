#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
        int smax;
        cin>>smax;
        char str[smax+2];
        scanf("%s",str);
        int count=0;
        int prev=0;

        for(int i=0;i<=smax;)
        {
            if(prev>=i)
            {
                prev+=str[i]-'0';
                i++;
            }
            else
            {
                count++;
                prev++;
            }

        }
        cout<<"Case #"<<cas<<": "<<count<<endl;
        cas++;
    }
}
