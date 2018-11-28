#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long ull;
typedef long long int ll;
typedef vector<long long int> vi;
int main()
{
    ios_base::sync_with_stdio(0);
    ll sum=0,count=0,t;
    ifstream f("A-large (1).in");
    ofstream o("Aout.out");
    f>>t;
    int z=t;
    while(t--)
    {
        char a[10000];
        //cout<<"hi";
        f>>a;
        //cout<<"hi1";
        vector<char > v;
        ll n;
        n=strlen(a);
        for(int i=0;i<n;i++)
        {
            if(i!=0)
            {
                if(v[0]>a[i])
                {
                    v.push_back(a[i]);
                }
                else
                    v.insert(v.begin(),a[i]);
            }

            else
                v.push_back(a[i]);
        }
        o<<"Case #"<<z-t<<": ";
        for(int i=0;i<n;i++)
        {
            o<<v[i];
            //cout<<v[i];
        }
        //cout<<endl;
        o<<endl;
    }
	return 0;
}



