#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    int x=1;
    while(t--)
    {
        int k,c,s,i;
        cin>>k>>c>>s;
        printf("Case #%d: ",x);
        for(i=1; i<=k; i++)
            printf("%d ",i);
        cout<<endl;
        x++;
    }
    return 0;
}