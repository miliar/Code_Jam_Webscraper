#include <bits/stdc++.h>
using namespace std;

void getDir(int &dx,int &dy, char d)
{
    dx = dy = 0;
    if(d == 'v') dx = 1;
    if(d == '^') dx = -1;
    if(d == '>') dy = 1;
    if(d == '<') dy = -1;
}

int getNextChar(char d)
{
    if(d == 'v') return '^';
    if(d == '^') return '>';
    if(d == '>') return '<';
    if(d == '<') return 'v';
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
        int R,C;
        cin>>R>>C;
        vector<vector<bool> > visites(R,vector<bool>(C,false));
        vector<string> lab(R);


        for(int c=0;c<R;c++)
        {
            cin>>lab[c];
        }


        int res = 0;

        for(int c=0;c<lab.size();c++)
        {
            for(int c2=0;c2<lab[c].size();c2++)
            {
                if(lab[c][c2] != '.' && !visites[c][c2])
                {
                    int dx,dy;
                    getDir(dx,dy,lab[c][c2]);
                    int x = c;
                    int y = c2;

                    for(int change=0;change<4;change++)
                    {
                        getDir(dx,dy,lab[c][c2]);
                        int x = c;
                        int y = c2;
                        bool found = false;
                        visites[x][y] = true;
                        while(x >= 0 && y >= 0 && x < lab.size() && y < lab[x].size())
                        {
                            x += dx;
                            y += dy;
                            if(x < 0 || y < 0 || x >= lab.size() || y >= lab[x].size()) break;
                            if(visites[x][y])
                            {
                                res += min(1,change);
                                goto noProblem;
                            }
                            else
                            {
                                if(lab[x][y] != '.')
                                {
                                    found = true;
                                    getDir(dx,dy,lab[x][y]);
                                    visites[x][y] = true;
                                }
                            }
                        }
                        if(found)
                        {
                            res += min(1,change)+1;
                            goto noProblem;
                        }
                        visites[c][c2]=false;
                        lab[c][c2] = getNextChar(lab[c][c2]);
                    }
                    cout<<"IMPOSSIBLE"<<endl;
                    goto nop;
                    noProblem:;
                }
            }
        }
        cout<<res<<endl;
        nop:;
    }
}
