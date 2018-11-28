#include <iostream>
#include <queue>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <set>
#include <sstream>
#include <iomanip>
using namespace std;



int dx[8]={-1,-1,-1,0,0,1,1,1};
int dy[8]={0,1,-1,1,-1,0,1,-1};

int xc;
int yc;

bool verify(vector<string> &v,vector<vector<int> > &voisins)
{
    vector<pair<int,int> > parcours;
    vector<vector<bool> > visites(voisins.size(),vector<bool>(voisins[0].size(),false));
    int xdep=-1,ydep;
    for(xdep=0;xdep<voisins.size();xdep++) for(ydep=0;ydep<voisins[xdep].size();ydep++) if(v[xdep][ydep]=='.'&&voisins[xdep][ydep]==0) goto found;
found:
    if(xdep==voisins.size()) return false;
    parcours.push_back(make_pair(xdep,ydep));
    visites[xdep][ydep]=true;
    while(parcours.size())
    {
        int xact = parcours.back().first;
        int yact = parcours.back().second;
        parcours.pop_back();
        for(int c=0;c<8;c++)
        {
            int x2 = xact+dx[c];
            int y2 = yact+dy[c];
            if(x2<0||y2<0||x2>=visites.size()||y2>=visites[0].size()||v[x2][y2]=='*') continue;
            if(x2>=0&&y2>=0&&x2<visites.size()&&y2<visites[0].size()&&visites[x2][y2]==false && voisins[x2][y2]==0)
            {
                parcours.push_back(make_pair(x2,y2));
            }
            visites[x2][y2]=true;
        }
    }
    for(int c=0;c<voisins.size();c++) for(int c2=0;c2<voisins[c].size();c2++) if(v[c][c2]!='*' && ! visites[c][c2]) return false;
     xc = xdep;
     yc = ydep;
    return true;

}


bool bourrin(vector<string> &act,vector<vector<int> > &voisins,int x,int y,int M)
{
    printf("%d %d\n",x,y);
    if(x==act.size())
    {
        if(M==0&&verify(act,voisins))
        {
            return true;
        }
        return false;
    }
    act[x][y]='.';
    if(bourrin(act,voisins,x+(y+1)/voisins[0].size(),(y+1)%voisins[0].size(),M))
        return true;
    if(M>0)
    {
        act[x][y]='*';
        for(int c=0;c<8;c++)
        {
            int x2 = x+dx[c];
            int y2 = y+dy[c];
            if(x2>=0&&y2>=0&&x2<voisins.size()&&y2<voisins[0].size()) voisins[x2][y2]++;
        }
        if(bourrin(act,voisins,x+(y+1)/voisins[0].size(),(y+1)%voisins[0].size(),M-1))
            return true;
        for(int c=0;c<8;c++)
        {
            int x2 = x+dx[c];
            int y2 = y+dy[c];
            if(x2>=0&&y2>=0&&x2<voisins.size()&&y2<voisins[0].size()) voisins[x2][y2]--;
        }
    }
    return false;

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
    for(int cas = 0; cas < nb_cas; cas++)
    {
        cout<<"Case #"<<cas+1<<":"<<endl;
        int R,C,M;
        cin>>R>>C>>M;
        // continue;
        vector<int> permutation(R*C,0);
        for(int c=0;c<M;c++) permutation[c]=1;
        reverse(permutation.begin(),permutation.end());
        bool ok = false;
        vector<string> act(R);
        for(int c=0;c<act.size();c++) act[c].resize(C);
        do
        {

            vector<vector<int> > voisins(R,vector<int>(C,0));
            for(int c=0;c<R;c++) act[c]=string(C,'.');
            for(int c=0;c<permutation.size();c++)
            {
                if(permutation[c]==1)
                {
                    int x = c/C;
                    int y = c%C;
                    act[x][y]='*';
                    for(int c=0;c<8;c++)
                    {
                        int x2 = x+dx[c];
                        int y2 = y+dy[c];
                        if(x2>=0&&y2>=0&&x2<voisins.size()&&y2<voisins[0].size()) voisins[x2][y2]++;
                    }
                }
            }

            if(R*C-M==1||verify(act,voisins)) {ok=true;break;}

        }while(next_permutation(permutation.begin(),permutation.end()));
        if(!ok)
        {
            cout<<"Impossible"<<endl;
        }
        else
        {
            if(R*C-M==1) {xc=0;yc=0;}
            act[xc][yc]='c';
            for(int c=0;c<act.size();c++) cout<<act[c]<<endl;
        }
    }
}
