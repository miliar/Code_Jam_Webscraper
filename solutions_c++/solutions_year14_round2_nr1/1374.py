/*
ID: amr.f.eldfrawy
LANG: C++
*/
#include <fstream>
#include <string>
#include<iostream>
#include<stdio.h>
#include<vector>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<math.h>
#define INF 1000000
#define MOD  1000000007
#define MAX 100000
using namespace std;
string arr[101];

int n ;
int g;
class node
{
public :
    char c ;
    int m ;
    node()
    {

    }
};
vector<vector<node> >G;

int solve()
{
    int cost = 0 ;
    for(int i = 0 ; i< n ; i++)
    {

        string str1 = arr[i];

        vector<node>A;
        stack<node>S;
        for (int j=0; j<str1.size(); j++)
        {
            char top = str1[j];

            if(S.size()>0)
            {
                if(top==S.top().c)
                    S.top().m++;
                else
                {
                    A.push_back(S.top());
                    S.pop();
                    node y ;
                    y.c = top;
                    y.m = 1;
                    S.push(y);
                }


            }
            else
            {
                node y ;
                y.c = top;
                y.m = 1;
                S.push(y);
            }
        }
        while(!S.empty()){
            A.push_back(S.top());S.pop();
        }

        G.push_back(A);



    }
    vector<node>STR;
    int o =G[0].size();
    //cout << G.size() << " sss \n" ;
    for (int i=0; i<G.size(); i++)
    {
        //cout << o << " " << G[i].size()<<endl;
        if(G[i].size()!=o)
            return INF;
    }
   // cout << " here \n";

    STR=G[0];
    for (int i=0; i<STR.size(); i++)
    {
        char s = STR[i].c;
        for (int j=0; j<G.size(); j++)
        {
            if(G[j][i].c!=s)
                return INF;
        }
        int SSS=INF;
        for (int j=0; j<G.size(); j++)
        {
            int mid  = G[j][i].m;

            int sum = 0 ;
            for (int k=0; k<G.size(); k++)
            {
                sum+=abs(G[k][i].m-mid);

            }
            SSS= min(SSS,sum);

        }

        cost+=SSS;


    }




    return cost;
}
int main()
{
    freopen("S.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin >> t;
    for (int q=0; q<t; q++)
    {

        cin  >> n ;
        for (int i=0; i<n; i++)
        {
            cin >>arr[i];
        }
        int ans =  INF ;


        ans = min(ans , solve());



        printf("Case #%d: ",q+1);
        if(ans==INF)
            printf("Fegla Won\n");
        else
            printf("%d\n",ans);

            G.clear();
    }

    return 0;

}
