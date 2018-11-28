#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <limits>
#include <iomanip>

using namespace std;

int func1(vector<double> naomi, vector<double> ken, int N)
{
    int ans = 0;
    for(int i=0,j=0;i<N;++i)
    {
        if (naomi[i]<ken[j])
        {
            ;
        }
        else
        {
            ++j;
            ans++;
        }
    }
    return ans;
}

int func2(vector<double> naomi, vector<double> ken, int N)
{
    int ans = 0;
    for(int i=0,j=0;j<N;++j)
    {
        if (naomi[i]<ken[j])
        {
            ++i;
        }
        else
        {
            ans++;
        }
    }
    return ans;
}

int main()
{
    int i,j,k,l,m,n;
    int T,M,N,K,t1,t2,t3,t4,t5;
    long long ans,out;
    freopen("D-large.in","r",stdin);
    freopen("D_output.txt","w",stdout);
    double x,y,z;
    cin>>T;
    for(t1=1;t1<=T;++t1)
    {
        cin>>N;
        vector<double> naomi, ken;
        for(i=0;i<N;++i)
        {
            cin>>x;
            naomi.push_back(x);
        }
        for(i=0;i<N;++i)
        {
            cin>>x;
            ken.push_back(x);
        }
        sort(naomi.begin(),naomi.end());
        sort(ken.begin(),ken.end());
        /*for(i=0;i<N;++i)
            cout<<naomi[i]<<"\t";
        cout<<endl;
        for(i=0;i<N;++i)
            cout<<ken[i]<<"\t";
        cout<<endl;*/
        printf("Case #%d: %d %d\n",t1, func1(naomi,ken,N), func2(naomi,ken,N));
    }

    return 0;
}
