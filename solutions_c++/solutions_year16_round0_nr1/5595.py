#include<iostream>
#include<vector>
#include<stdio.h>
#include<algorithm>
using namespace std;

bool contains(vector<long long int> vec)
{
    if(vec.size()==10)
        return true;
    else
        return false;
}

int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("output5.txt","w",stdout);
    long long int t,n;
    cin>>t;
    long long int p=t;
    {
        while(t--)
        {
            vector <long long int> vec;
            cin>>n;
            long long int i=1;
            if(n==0)

            {
                cout<<"Case #"<<p-t<<": INSOMNIA"<<endl;
                continue;
            }
            long long int x,n1=n;
            while(1)
            {
                while(n!=0)
                {
                    if(find(vec.begin(),vec.end(),n%10)==vec.end())
                        vec.push_back(n%10);
                    sort(vec.begin(),vec.end());
                    n/=10;
                }
               // cout<<vec.size()<<endl;
                if(contains(vec))
                {
                    cout<<"Case #"<<p-t<<": "<<x<<endl;
                    break;
                }
                i++;
                n=n1*i;
               x=n;
            }
        }
    }
}
