#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;
int main()
{
    int A,B,C;
    cin>>A>>B>>C;
    cout<<"Case #1:\n";
    vector<long long> v;
    v.push_back(2);
    v.push_back(3);
    for(long long i=5;i<=10000000;i+=2)
    {
        long long l=sqrt(i);
        int c=0;
        for(long long j=0;v[j]<=l;j++)
        {
            if(i%v[j]==0)
            {
                c=1;
                break;
            }
        }
        if(c==0)
        v.push_back(i);
    }
    int c=0;
    for(long i=32769;i<65526;i+=2)
    {
        int d=0;
        long i1=i;
        vector<long long> v1;
        vector<bool> str;
        while(i1>0)
        {
            str.push_back(i1%2);
            i1/=2;
        }
        for(int j=2;j<=10;j++)
        {
            long long s=0;
            int p;
            for(p=0;p!=str.size();p++)
            s+=(pow(j,p)*str[p]);
            p=0;
            for(long long k=0;k!=v.size() && v[k]<=sqrt(s);k++)
            {
                if(s%v[k]==0)
                {
                    p=1;
                    v1.push_back(v[k]);
                    break;
                }
            }
            if(p==0)
            {
                d=1;
                break;
            }
        }
        if(d==0)
        {
            for(int k=str.size()-1;k>=0;k--)
            cout<<str[k];
            for(int k=0;k!=v1.size();k++)
            cout<<" "<<v1[k];
            cout<<endl;
            c++;
        }
        if(c==50)
        break;
    }
    return 0;
}
