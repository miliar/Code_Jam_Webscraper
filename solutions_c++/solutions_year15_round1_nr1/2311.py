#include <vector>
#include <iostream>
#include <fstream>

using namespace std;


int main()
{
    freopen("in.txt","r",stdin);
    freopen("outlarge.txt","w",stdout);
    long t;
    cin>>t;
    for(long i=1;i<=t;i++)
    {
        long n;
        cin>>n;
        vector<long> vec;
        for(long j=0;j<n;j++)
        {
            long temp;
            cin>>temp;
            vec.push_back(temp);
        }

        long ans1=0;
        for(long j=0;j<vec.size()-1;j++)
        {
            if(vec[j]>vec[j+1])
                {
                    ans1+=(vec[j]-vec[j+1]);
                }
        }

        long ans2=0;
        long diff=0;
        for(long j=0;j<vec.size()-1;j++)
        {
            if(vec[j]>vec[j+1])
            {
                if(diff<(vec[j]-vec[j+1]))
                    diff=(vec[j]-vec[j+1]);
            }

        }

        for(long j=0;j<vec.size()-1;j++)
        {
            if(vec[j]<=diff)
            {
                ans2+=vec[j];
            }
            else
            {
                ans2+=diff;
            }

        }
        cout<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<endl;

    }
    return 0;
}
