#include<bits/stdc++.h>
using namespace std;
int main()
{
    int tc, t=1;
    cin>>tc;

    while(tc--)
    {
        int l, sum=0, c=0;
        cin>>l;
        char a[l+1];
        cin>>a;

        for(int i=0; i<=l; ++i)
        {
            int p = a[i]-'0';
            if(sum<i && i!=0 && a[i]!='0')
            {
                c+=(i-sum);
                sum+=c;
            }

            sum+=p;
        }

        cout<<"Case #"<<t<<": "<<c<<endl;
        t++;
    }

return 0;
}
