#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#define loop(v) for(int i=0;i<v.size();i++)
#define loopb(v) for(int i=v.size()-1;i>=0;i--)

using namespace std;

bool isOk(vector<vector<int> > lawn,int N,int M)
{
    for(int j=0;j<N;j++)
        {
            for(int k=0;k<M;k++)
            {
                if(lawn[j][k]==1)
                    return false;
            }
        }
    return true;
}

int main() {

    int T;
    int M,N;
    int get;
    ofstream OUT ("small.out");
    ifstream IN ("small.in");
    IN >> T;
    //cout << T<<endl;
    for(int i=0;i<T;i++)
    {
        IN>>N;
        IN>>M;
        vector<vector<int> > lawn;
        for(int j=0;j<N;j++)
        {
            vector<int> ligne;
            for(int k=0;k<M;k++)
            {
                IN>>get;
                ligne.push_back(get);
            }
            lawn.push_back(ligne);
        }

        vector<int> supprimer;
        for(int j=0;j<N;j++)
        {
            int compteur=0;
            for(int k=0;k<M;k++)
            {
                if(lawn[j][0]==1)
                {
                    if(lawn[j][k]==lawn[j][0])
                        compteur++;
                }
            }
            if(compteur==M)
                supprimer.push_back(j);

        }

        for(int j=0;j<supprimer.size();j++)
        {
            lawn.erase(lawn.begin()+supprimer[j]-j);
        }
        N-=supprimer.size();


         for(int j=0;j<M;j++)
        {
            int compteur=0;
            if(lawn[0][j]==1)
            {
                for(int k=0;k<N;k++)
                {
                    if(lawn[k][j]==lawn[0][j])
                        compteur++;
                }
            }
            if(compteur==N)
            {
                for(int k=0;k<N;k++)
                    lawn[k][j]=0;
            }

        }

        OUT <<"Case #"<<i+1<<": ";
        if(isOk(lawn,N,M))
            OUT<<"YES"<<endl;
        else
            OUT<<"NO"<<endl;

        lawn.clear();
        supprimer.clear();
    }
    return 0;
}
