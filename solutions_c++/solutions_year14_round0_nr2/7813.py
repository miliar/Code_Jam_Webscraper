#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outputlarge.txt","w",stdout);
    int t;
    cin>>t;
    for(int p=1;p<=t;p++)
    {
        double c,f,x,prev,curr;
        cin>>c>>f>>x;
        prev=x/2;
        for(int i=1;;i++)
        {
            curr=prev-((x-c)/(2+((i-1)*f)))+(x/(2+(i*f)));
            if(curr>prev)
                break;
            prev=curr;
        }
        printf("Case #%d: %.7lf\n",p,prev);
    }
    return 0;
}
