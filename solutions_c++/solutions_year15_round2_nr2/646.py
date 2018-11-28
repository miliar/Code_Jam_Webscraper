#include <iostream>
#include <queue>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <set>
#include <sstream>
#include <ctime>
#include <map>
using namespace std;

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
        int N,R,C;
        cin>>R>>C>>N;

        vector<vector<bool> > lol(R,vector<bool>(C,false));

        int res = 10000000;

        for(int c=0;c<(1<<(R*C));c++)
        {
            int unhappy = 0;
            int truc=0;
            for(int x=0;x<R;x++)
            {
                for(int y=0;y<C;y++)
                {
                    if(c&(1<<(x*C+y)))
                    {
                        truc++;
                        lol[x][y]=true;
                    }
                    else
                    {
                        lol[x][y]=false;
                        continue;
                    }
                    if(x > 0 && lol[x-1][y]) unhappy++;
                    if(y > 0 && lol[x][y-1]) unhappy++;

                }
            }
            if(truc==N)
                res = min(unhappy,res);
        }
        cout<<res<<endl;
    }
}
