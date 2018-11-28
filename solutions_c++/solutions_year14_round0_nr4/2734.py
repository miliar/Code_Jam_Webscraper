#include<iostream>
#include<iomanip>
#include<vector>
#include<string>
#include<fstream>
#include<list>
#include<cctype>
#include<algorithm>
#include<queue>
#include<stack>
#include<cmath>
#include<sstream>
#include<map>
#define long long LL

using namespace std;
int War(vector<double>naomi,vector<double>ken)
{
    int W=0;
    while(naomi.size())
    {
            for(int j=0;j<ken.size();j++)
            {
                if(naomi.front()<ken[j])
                {
                    naomi.erase(naomi.begin());
                    ken.erase(ken.begin()+j);
                    break;
                }
                if(j==ken.size()-1)
                {
                    W+=naomi.size();
                    return W;
                }
            }
    }
    return W;
}
int WarD(vector<double>naomi,vector<double>ken)
{
    int WD=0;
    while(naomi.size())
    {
        if(naomi.front()<ken.front())
        {
            naomi.erase(naomi.begin());
            ken.pop_back();
        }
        else
        {
            WD++;
            naomi.erase(naomi.begin());
            ken.erase(ken.begin());
        }
    }
    return WD;
}
int main ()
{
    ifstream cin("D-large.in");
    ofstream cout("War.out");
    int cas;
    cin>>cas;
    for(int i=0;i<cas;i++)
    {
        vector<double> ken;
        vector<double> naomi;
        int num;
        cin>>num;
        double r;
        for(int j=0;j<num;j++)
        {
            cin>>r;
            naomi.push_back(r);
        }
        for(int j=0;j<num;j++)
        {
            cin>>r;
            ken.push_back(r);
        }
        sort(naomi.begin(),naomi.end());
        sort(ken.begin(),ken.end());
        /*for(int j=0;j<num;j++)
            cout<<naomi[j]<<" ";
        cout<<endl;
        for(int j=0;j<num;j++)
            cout<<ken[j]<<" ";
        cout<<endl;*/
        int W=0,WD=0;
        W=War(naomi,ken);
        WD=WarD(naomi,ken);
        cout<<"Case #"<<i+1<<": "<<WD<<" "<<W<<"\n";
    }

    return 0;
}

