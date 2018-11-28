#include <iostream>
#include <queue>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <set>
#include <sstream>
#include <map>
using namespace std;

int truchash(vector<int> &v)
{
    int res = 0;
    for(int c=0;c<v.size();c++)
    {
        res*=10;
        res+=max(0,v[c]);
    }
    return res;
}
map<int,int> memo;
int brute(vector<int> &v)
{
    for(int c=0;c<v.size();c++) cout<<v[c]<<" ";
    cout<<endl<<endl;
    int bla = truchash(v);
    if(memo.find(bla)!=memo.end()) return memo[bla];

    if(*max_element(v.begin(),v.end())<0) return 0;
    memo[bla]=10000000;



    int res = 1000000;

    for(int c=0;c<v.size();c++)
    {
        for(int c2=0;c2<v.size();c2++)
        {
            if(c==c2 || v[c] <= 0) continue;
            int tmp = v[c];
            int subZero = (v[c2]<0?-v[c2]:0);
            v[c2]+=subZero;
            for(int c3=0;c3<tmp;c3++)
            {
                v[c]--;
                v[c2]++;
                res=min(res,brute(v)+1);
            }
            v[c2]-=subZero;
            v[c]+=tmp;
            v[c2]-=tmp;
        }
    }
    for(int c=0;c<v.size();c++)
    {
        v[c]=v[c]-1;
    }

    res = min(res,brute(v)+1);
    for(int c=0;c<v.size();c++)
    {
        v[c]=v[c]+1;
    }
    for(int c=0;c<v.size();c++) cout<<v[c]<<" ";
    cout<<endl<<res<<endl<<endl;
    memo[bla]=res;
    return res;
}


int main()
{
    ios_base::sync_with_stdio(false);
    ifstream in("input.txt");
    ofstream out("output.txt");
    #define cin in
    #define cout out
    int nb_cas;
    cin>>nb_cas;
    for(int cas=1;cas<=nb_cas;cas++)
    {
        cout<<"Case #"<<cas<<": ";
        int D;
        cin>>D;

        vector<int> v(D);
        for(int c=0;c<D;c++)
        {
            cin>>v[c];
        }
        int res = (*max_element(v.begin(),v.end()));
        for(int c=1000;c>=1;c--)
        {
            int act = 0;
            for(int c2=0;c2<D;c2++)
            {
                if(v[c2]>c)
                {
                    act+=(v[c2]-1)/c;
                }
            }

            res=min(res,act+c);

            nop:;
        }
        cout<<res<<endl;
    }
}
