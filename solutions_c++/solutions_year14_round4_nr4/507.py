#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <list>
#include <sstream>
#include <ctime>
#include <queue>
#include <iomanip>
#include <set>
#include <map>
#define DEBUG2

using namespace std;



int nbServeurs = 0;
map<int,int> m;
int bourrin(vector<int> &att,vector<string> &S,int i)
{
    if(i == att.size())
    {
        vector<set<string> > v(nbServeurs);
        int nonVides = 0;
        for(int c=0;c<att.size();c++)
        {
            if(v[att[c]].size()==0)
            {
                nonVides ++;
            }
            for(int c2=0;c2<=S[c].size();c2++)
            {
                v[att[c]].insert(S[c].substr(0,c2));
            }
        }
        if(nonVides != nbServeurs) return 0;

        int res = 0;
        for(int c=0;c<v.size();c++) res+=v[c].size();
        m[res]++;
        return res;
    }
    int res = 0;
    for(int c=0;c<nbServeurs;c++)
    {
        att[i] = c;
        res = max(res,bourrin(att,S,i+1));
    }
    return res;
}



int main()
{
#define cin in
#define cout out
    ifstream in("input.txt");
    ofstream out("output.txt");
    int nb_cas;
    cin>>nb_cas;

    for(int cas = 0;cas<nb_cas;cas++)
    {
        cout<<"Case #"<<cas+1<<": ";
        m.clear();
        int M;
        cin>>M>>nbServeurs;
        printf("%d",nbServeurs);
        vector<string> S(M);
        for(int c=0;c<M;c++) cin>>S[c];
        vector<int> att(M,0);
        int res = bourrin(att,S,0);
        cout<<res<<" ";
        cout<<m[res]<<endl;

    }


}
