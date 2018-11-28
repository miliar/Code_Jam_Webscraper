#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <list>
#include <sstream>
#include <ctime>
#include <queue>
#include <iomanip>
#include <map>
#define DEBUG2

using namespace std;



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
        int N;
        cin>>N;
        vector<pair<int,int> > v(N);
        for(int c=0;c<v.size();c++)
        {
            cin>>v[c].first;
            v[c].second = c;
        }
        sort(v.begin(),v.end());
        int gauche = 0, droite = v.size()-1;
        int res = 0;
        for(int c=0;c<v.size();c++)
        {
            int pos = min(droite,max(gauche,v[c].second));
            if(abs(pos-gauche) < abs(pos-droite))
            {
                res+=abs(pos-gauche);
                for(int c2=0;c2<v.size();c2++) if(v[c2].second<v[c].second) v[c2].second++;
                gauche++;
            }
            else
            {
                res+=abs(pos-droite);
                for(int c2=0;c2<v.size();c2++) if(v[c2].second>v[c].second) v[c2].second--;
                droite--;
            }
        }
        cout<<res<<endl;
    }


}
