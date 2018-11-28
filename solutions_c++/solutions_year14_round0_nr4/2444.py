#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include "fstream"

#define sz(X) ((int)X.size())
#define FOR(i,x,y) for(int i=x; i<y; ++i)
#define FORE(i,x,y) for(int i=x; i<=y; ++i)
char buf[50]; std::string itos(int x) {sprintf(buf,"%d",x); return buf;}

using namespace std;

bool war_won_by_naomi(vector<double> &naomi, vector<double> &ken)
{
    if(naomi[0] < ken[0])
    {
        naomi.erase(naomi.begin()); ken.erase(ken.begin());
        return false;
    }
    else
    {
        bool found = 0;

        int N = sz(ken);
        int i = 0;
        while (i<N)
        {
            if(naomi[0] > ken[i])
                i++;
            else
            {
                found = true;
                break;
            }
        }

        if(found)
        {
            ken.erase(ken.begin()+i);
            naomi.erase(naomi.begin());
            return false;
        }
        else
        {
            ken.erase(ken.begin());
            naomi.erase(naomi.begin());
            return true;
        }
    }
}

bool deceitful_war_won_by_naomi(vector<double> &naomi, vector<double> &ken)
{
    if(naomi[0]<ken[0]) //if naomi is loosing give the lowest value telling it as the highest
    {
        naomi.erase(naomi.end()-1); //give min
        ken.erase  (ken.begin());   //take max
        return false;
    }
    else
    {
        //naomi will optimally give the max to get the max of ken 
        int N = sz(naomi);
        int i = 0;
        while (i<N && naomi[i] > ken[0]) i++;

        naomi.erase(naomi.begin() + i - 1);
        ken.erase(ken.begin());
        return true;
    }
}
int main()
{
    ofstream cout ("output.txt");
    ifstream cin ("input.txt");

    int T;
    cin>>T;

    FOR(i,1,T+1)
    {
        int N; cin>>N;
        vector<double> naomi(N), ken(N);
        FOR(i,0,N)cin>>naomi[i];
        FOR(i,0,N)cin>>ken[i];


        //Playing War
        int war_ans = 0;
        sort(naomi.begin(), naomi.end());
        sort(ken.begin()  , ken.end());

        vector<double> d_naomi(naomi), d_ken(ken);

        int j = 0;
        FOR(i,0,N)
            if(war_won_by_naomi(naomi, ken)) war_ans++;

        //Playing Deceitful War
        int d_war_ans = 0;
        sort(d_naomi.rbegin(), d_naomi.rend());
        sort(d_ken.rbegin()  , d_ken.rend());

        j = 0;
        FOR(i,0,N)
        {
            if(deceitful_war_won_by_naomi(d_naomi,d_ken)) d_war_ans++;
        }

        cout<<"Case #"<<i<<": "<<d_war_ans<<" "<<war_ans<<endl;
    }

    return 0;
}