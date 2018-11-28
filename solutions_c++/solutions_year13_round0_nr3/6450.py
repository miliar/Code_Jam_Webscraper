#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
using namespace std;

bool check(int n)
{
    vector<int>v;
    while(n>0)
    {
        v.push_back(n%10);
        n/=10;
    }
    for(int i=0;i<=v.size()/2;++i)
    {
        if(v[i]!=v[v.size()-i-1])return false;
    }
    return true;

}
int main()
{
    int t;
    ifstream fin("C-small-attempt0.in");
    ofstream fout("output.out");
    fin>>t;
    for(int i=1;i<=t;++i)
    {
        int a,b;
        fin>>a>>b;
        int c=0;
        for(int j=a;j<=b;++j)
        {
            int temp=j;
            if(sqrt(temp)*sqrt(temp)!=j)continue;
            if(check(j)&&check(sqrt(temp)))c++;
        }
        fout<<"Case #"<<i<<": "<<c<<endl;
    }
    return 0;
}
