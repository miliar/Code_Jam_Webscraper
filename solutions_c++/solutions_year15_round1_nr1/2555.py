#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int i,x,y=0,t_cases,N,m[10000],sum1,sum2,max_diff=0;
    cin>>t_cases;
    while(t_cases--)
    {
        y+=1;
        sum1=sum2=max_diff=0;
        cin>>N;
        for(i=0;i<N;i++)
            cin>>m[i];
        for(i=0;i<N-1;i++)
            {
                x = m[i] - m[i+1];
                if(x>0)
                    sum1+=x;
                max_diff = max(x,max_diff);
            }
            //cout<<"Sum1 = "<<sum1;
        for(i=0;i<N-1;i++)
            {
                 //cout<<";  Sum2 = "<<sum2<<endl;
                 sum2+= min(max_diff,m[i]);
            }
            cout<<"Case #"<<y<<": "<<sum1<<" "<<sum2<<endl;

    }

}
