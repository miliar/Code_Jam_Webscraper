#include<iostream>
#include<cstdio>
#include<vector>
#include<fstream>
#include<iomanip>
#include<algorithm>
using namespace std;
main()
{
    ofstream ofile("output3.txt");
    ifstream ifile("D-small-attempt0.in");
    int t;
    ifile>>t;
    for(int z=1;z<=t;++z)
    {
        int n;
        ifile>>n;
        vector<double> v1(n);
        vector<double> v2(n);
        vector<double> v3(n);
        vector<double> v4(n);
        for(int i=0;i<n;++i)
        {
            ifile>>v1[i];
            v3[i]=v1[i];
        }
        for(int i=0;i<n;++i)
        {
            ifile>>v2[i];
            v4[i]=v2[i];
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        int e1=n-1,e2=n-1;
        int ans1=0;
        for(int i=0;i<n;++i)
        {
            if(v1[e1]>v2[e2])
            {
                int p=e1-1;
                while(v1[p]>v2[e2] && p>=0)
                {
                    --p;
                }
                ++p;
                v1.erase(v1.begin()+p);
                v2.erase(v2.begin()+e2);
                --e1;
                --e2;
                ++ans1;
            }
            else
            {
                v1.erase(v1.begin());
                v2.erase(v2.begin()+e2);
                --e1;
                --e2;
            }
        }
        sort(v3.begin(),v3.end());
        sort(v4.begin(),v4.end());
        int ans2=0;
        int s2=0;
        for(int i=0;i<n;++i)
        {
            if(s2==n)
            {
                break;
            }
            while(v4[s2]<v3[i] && s2<n)
            {
                ++ans2;
                ++s2;
            }
            ++s2;
        }
        ofile<<"Case #"<<z<<": "<<ans1<<" "<<ans2<<endl;
    }
}
