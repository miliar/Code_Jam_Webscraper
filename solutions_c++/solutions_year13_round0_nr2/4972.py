#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>
#include<cstring>


using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf


int dest[105][105];

int row,col;

struct node
{
    int val;
    int r,c;
};
vector<node> nodes;
bool operator<(const node &a, const node & b)
{
    if ( a.val !=  b.val)
        return a.val > b.val;
    if ( a.r != b.r)
        return a.r<b.r;
    return a.c < b.c;
}
int src[105][105];

bool flagrow[105];
bool flagcol[105];

string Match()
{
    //cout<<src[0][1]<< " "<<src[0][1]<< "  "<<src[0][2]<<endl;
    int i,j;
    for(i=0;i<row;i++)
        for(j=0;j<col;j++)
            if ( src[i][j] != dest[i][j] )
                return "NO";
    return "YES";
}

int main()
{

    //freopen("sample.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("answer.txt","w",stdout);
    int t;
    int kase=1;
    sf("%d",&t);
    while(t--)
    {
        nodes.clear();
        pf("Case #%d: ",kase++);
        sf("%d %d",&row,&col);
        int i,j;
        for(i=0;i<row;i++)
            for(j=0;j<col;j++)
            {
                sf("%d",&dest[i][j]), src[i][j] = 100;
                //cout<<dest[i][j]<<endl;
                node temp;
                temp.val = dest[i][j];
                temp.r = i;
                temp.c = j;
                nodes.pb(temp);
            }
        sort(nodes.begin(), nodes.end());
        fill(flagrow,flagrow+103,false);
        fill(flagcol, flagcol+103,false);

        for(i=0;i<nodes.sz();i++)
        {
            node temp = nodes[i];
            //cout<<temp.val<<endl;
            int k;
            if ( flagrow[temp.r] == false)
            {
                // flag this row and cut it
                //cout<<temp.r<<endl;
                for(k=0;k<col;k++)
                    src[temp.r][k] = temp.val;
                flagrow[temp.r] = true;
            }
            //flag this  col and cut it
            if ( flagcol[temp.c] == false )
            {
                for(k=0;k<row;k++)
                    src[k][temp.c] = temp.val;
                flagcol[temp.c] = true;
            }
        }
        // now match src and dst;

        cout<<Match()<<endl;

    }
    return 0;
}
