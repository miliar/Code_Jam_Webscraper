#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int T,sol,n,s1,s2;
vector<double> v1,v2;
bool viz1[1001],viz2[1001];

inline void setviz()
{
    for(int i=0;i<n;i++)
        viz1[i]=viz2[i]=false;
}

int main()
{
    double x;
    ifstream f1("1.in");
    ofstream f2("1.out");
    f1>>T;
    for(int ct=1;ct<=T;ct++)
    {
        v1.clear();
        v2.clear();
        f1>>n;
        for(int i=0;i<n;i++)
        {
            f1>>x;
            v1.push_back(x);
        }
        for(int i=0;i<n;i++)
        {
            f1>>x;
            v2.push_back(x);
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        //cerinta 1
        setviz();
        s1=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if(v1[j]>v2[i]&&!viz1[j])
                {
                    viz1[j]=true;
                    s1++;
                    break;
                }
        //cerinta 2
        setviz();
        s2=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if(v2[j]>v1[i]&&!viz2[j])
                {
                    viz2[j]=true;
                    s2++;
                    break;
                }
        f2<<"Case #"<<ct<<": "<<s1<<" "<<n-s2<<"\n";
    }
    return 0;
}
