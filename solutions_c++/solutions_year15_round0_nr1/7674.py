#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t,i,n;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        string audnc;
        cin>>audnc;
        int stand = 0 , ans =0 , len = audnc.size();
        for(int j=0;j<len;j++)
        {
            int temp = audnc[j]-'0';
            if(stand<=j && temp==0)
            {
                ans++,stand++;
            }
            else
            {
                stand+=temp;
            }
        }

        printf("Case #%d: %d\n",i,ans);
    }

    return 0;
}
