#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <sstream>
#include<map>
#include<limits.h>

using namespace std;
unsigned long long solve(vector<int>S,int i, int sum,int C)
{
    if(i==S.size())
    {
        return C;
    }
    if(sum>S[i])

    {
        return solve(S,i+1,sum+S[i],C);
    }

    else
    {
        //cout<<sum<<"asdas"<<endl;
        int  r=sum;
        int R=S[i];
        int c=C;
        unsigned long long Q=LONG_LONG_MAX;
        if(r!=1)
        while(r<=R)
        {
            r+=r-1;
            c++;
        }

//<<r<<"  "<<c<<endl;

        if(r!=1)
            Q=solve(S,i+1,r+S[i],c);

        return min(solve(S,i+1,sum,C+1) ,Q);
    }

}
int main()
{

    freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);


    int n;
    cin>>n;
    for (int i=1; i<=n; i++)
    {
        unsigned long long int ans=0;

        int B,N,k;
        cin>>B>>N;
        vector<int>S;
        for (int j=0; j<N; j++)
        {
            cin>>k;
            S.push_back(k);

        }
        sort(S.begin(),S.end());

        ans=solve(S,0,B,0);





        printf("Case #%d: %llu\n",i,ans);

    }

    return 0;


}
