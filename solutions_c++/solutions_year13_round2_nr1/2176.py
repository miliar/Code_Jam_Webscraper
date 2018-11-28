#include<iostream>
#include<fstream>
#include<algorithm>
#include<stdlib.h>
#include<vector>
using namespace std;
int calc(int a,int b)
{
    int count=0;
    while(a<=b)
    {
        a=a+a-1;
        count++;
    }
    return count;
}
int final(int a,int b)
{

    while(a<b)
    {
        a=a+a-1;

    }
    return (a+b);
}
int func(int x,vector<int> vec)
{

    if(vec.size()==0)
    return 0;

    int d= calc(x,vec[0]);
    int val=final(x,vec[0]);
    vec.erase(vec.begin());
    int x1=d+func(val,vec);
    int x2=1+func(x,vec);
    if(x1>x2)
    return x2;
    else
    return x1;
}
int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.txt");
    vector<int> vec;
    int t,a,n,p,i,q=0;
    fin>>t;
    while(t--)
    {
        vec.clear();
        fin>>a>>n;
        for(i=0;i<n;i++)
        {
            fin>>p;
            vec.push_back(p);
        }
        int ans;
        sort(vec.begin(),vec.end());
        if(a!=1)
        ans=func(a,vec);
        else
        ans=n;
        q++;
        fout<<"Case #"<<q<<": "<<ans<<endl;
        //cout<<ans<<endl;
    }

    return 0;
}
