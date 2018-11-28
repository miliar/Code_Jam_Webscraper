#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    long long t;
    cin>>t;
    long long k = 1;
    while(t--)
    {
        cout<<"Case #"<<k<<": ";
        k++;
        long long n;
        cin>>n;
        vector<long long> v;
        for(long long i=0;i<n;i++)
        {
            long long temp;
            cin>>temp;
            v.push_back(temp);
        }
        long long diff = 0;
        long long ans1  = 0;
        for(long long i=1;i<v.size();i++)
        {
            long long temp = v[i-1] - v[i];
            if(temp > diff)
            {
                diff = temp;

            }
            if(temp > 0)
            {
                ans1 += temp;
            }
            //cout<<temp<<" "<<ans1<<endl;
        }
        //cout<<endl;
        long long ans2 = 0;
        for(long long i=0;i<v.size()-1;i++)
        {
            if(v[i] >= diff)
            {
                ans2 += diff;
            }
            else
            {
                ans2 += v[i];
            }
        }
        cout<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}
