#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<deque>
#include<cmath>
#include<cstdio>
#include<utility>
#include<set>
#include<cmath>
#include<queue>
#define MAX_N 21
using namespace std;

int T, n, result;
string cars[21];
string scalony;
bool bylo[121];

void perm(int k)
{
    if(k==1)
    {
        //cout << "jestem" << endl;
        //for(int i=1; i<=n; ++i) cout << cars[i] << " ";
        bool dasie=true;
        scalony="";
        for(int i=40; i<=121; ++i) bylo[i]=false;
        for(int i=1; i<=n; ++i) scalony+=cars[i];
        //cout << scalony << endl;
        for(int i=0; i<scalony.length(); ++i)
        {
            //cout << scalony[i]-'0' << " " << endl;
            //cout << "i2: " << i << endl;
            if(bylo[scalony[i]-'0']) {dasie=false;}//cout << scalony[i]-'0' << "!" << endl;}
            char temp=scalony[i];
            while(scalony[i]==temp) i++;
            i--;
            //cout << "i: " << i << endl;
            bylo[scalony[i]-'0']=true;
        }
        if(dasie) result++;
    }
    else
    {
        for(int i=1; i<=k; ++i)
        {
            swap(cars[i], cars[k]);
            perm(k-1);
            swap(cars[i], cars[k]);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin >> T;
    for(int lzd=1; lzd<=T; ++lzd)
    {
        cin >> n;
        result=0;
        for(int i=1; i<=n; ++i) cin >> cars[i];
        //for(int i=1; i<=n; ++i) cout << cars[i] << " ";
        perm(n);
        cout << "Case #" << lzd << ": " << result << endl;
    }
    return 0;
}
