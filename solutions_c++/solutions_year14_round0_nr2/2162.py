#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,j;
    double farm,rate,req,d,till,curr;
    vector<double> answer;
    cin>>t;
    for(i=0;i<t;i++)
    {
        till=0.0;
        cin>>farm>>rate>>req;
        answer.clear();
        if(req<=farm)
        {
            printf("Case #%d: %.7lf\n",i+1,req/2.0);
            continue;
        }
        curr=2.0;
        for(j=0;;j++)
        {
            answer.push_back(till+req/curr);
           // printf("curr=%lf %lf ",curr,till+req/curr);
            till+=(farm/curr);
            curr+=rate;
            if(j>0&&answer[j]>answer[j-1])
            break;
        }
       // cout<<endl;
        printf("Case #%d: %.7lf\n",i+1,answer[j-1]);
    }
    return 0;
}
