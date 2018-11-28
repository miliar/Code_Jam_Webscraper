#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
enum{i=2,j=3,k=4};
int multLUT[5][5]={
    {0,0,0,0,0},
    {0,1,i,j,k},
    {0,i,-1,k,-j},
    {0,j,-k,-1,i},
    {0,k,j,-i,-1}
};
inline int mult(int arg1,int arg2)
{
    if(arg1<0)
    {
        if(arg2<0)return multLUT[-arg1][-arg2];
        else return -multLUT[-arg1][arg2];
    }
    else if(arg2<0)return -multLUT[arg1][-arg2];
    return multLUT[arg1][arg2];
}
string t;
int cases,repetitions,asdf;
bool findWay3(int w)
{
    int curval=1;
    while(w<t.size())
    {
        curval=mult(curval,t[w]-103);
        w++;
    }
    if(curval==k)return 1;
    return 0;
}
bool findWay2(int w)
{
    int curval=1;
    while(w<t.size())
    {
        curval=mult(curval,t[w]-103);
        if(curval==j&&findWay3(w+1))return 1;
        w++;
    }
    return 0;
}
bool findWay1()
{
    int curval=1;
    for(int w=0;w<t.size();w++)
    {
        curval=mult(curval,t[w]-103);
        if(curval==i&&findWay2(w+1))return 1;
    }
    return 0;
}
int main()
{
    ifstream fin("dijkstra.in");
    ofstream fout("dijkstra.out");
    fin >> cases;
    for(int f=0;f<cases;f++)
    {
        fin >> asdf >> repetitions;
        getline(fin,t);
        getline(fin,t);
        string x(t);
        for(int i=1;i<repetitions;i++)t+=x;
        cout << f << "\n";
        if(findWay1())fout << "Case #" << f+1 << ": YES\n";
        else fout << "Case #" << f+1 << ": NO\n";
    }
    return 0;
}
