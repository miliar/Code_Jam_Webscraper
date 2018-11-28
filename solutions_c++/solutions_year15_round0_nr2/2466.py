#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> p(1010);
long long int maxi,mini,sum;
long double temp;

int main()
{
    int t;
    int d;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>t;
    for(int ti=1;ti<=t;ti++)
    {
        cin>>d;
        for(int i=0;i<d;i++)
            cin>>p[i];
        maxi=*max_element(p.begin(),p.end());
        mini=100000000;
        for(int i=1;i<=maxi;i++)
        {
            sum=0;
            for(int j=0;j<d;j++)
            {
                if(p[j]>i)
                {
                    temp=(double)(p[j]-i)/(double)i;
                    sum+=ceil(temp);
                    
                }
            }
            sum+=i;
            if(sum<mini)
                mini=sum;
        }
        cout<<"Case #"<<ti<<": "<<mini<<endl;
    }
    return 0;
}