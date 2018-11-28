#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("codejam2.out", "w", stdout);
    int testcases;
    cin>>testcases;
    char ar[110],currentstatus;
    int count=0;
    for(int k=1; k<=testcases; k++)
    {
        cin>>ar;
        printf("Case #%d: ",k);

        {
            currentstatus=ar[0];
            count=0;
            for(int i=1; i<strlen(ar); i++)
            {
                if(ar[i]==currentstatus)
                    continue;
                    else
                    {
                        count++;
                        currentstatus=ar[i];
                    }

            }
            if(currentstatus=='-')
                count++;
            cout<<count<<endl;
        }
    }

}
