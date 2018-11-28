#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define UPPER 200
#define MAX 500
#define MAXIMUM 1000000

char s[MAX][MAX];
int len[MAX];
int group[MAX][MAX];
char which[MAX][MAX];
vector<vector <int> >v(MAX);
vector< vector<char> >vv(MAX);


void solve()
{

    int n;
    scanf("%d\n",&n);
    
    for (int i=0;i<=UPPER;i++) v[i].clear(), vv[i].clear();

    for ( int i=0;i<n;i++)
    {
        int c;
        int j = 0;
        while ((c=getchar()) != '\n' && c != EOF )
            s[i][j++] = c;
        len[i] = j;
    }


    for (int i=0;i<n;i++)
    {
        int j=0;
        char cur = s[i][0];
        group[0][i] = 0;
        which[0][i] = cur;
        int count = 0;
        for (int j=0;j<len[i];j++)
        {
            
            if ( s[i][j] == cur ) 
                group[count][i]++;
            else
            {
                v[count].push_back(group[count][i]);
                vv[count].push_back(which[count][i]);
                which[++count][i] = s[i][j];
                group[count][i] = 1;
                cur = s[i][j];
            }
        }

           v[count].push_back(group[count][i]);
           vv[count].push_back(which[count][i]);

    }
/*
    for (int i=0;i<=n;i++)
    {

        if ( v[i].empty() ) continue;
        for (int j =0; j <v[i].size();j++)
            printf("%d  ",v[i][j]);
        printf("<----\n");
    }
*/

//--------------------here for validity

    for (int i=0;i<= UPPER;i++)
    {

        bool flag = true;
        if ( vv[i].empty() ) continue;

        if ( vv[i].size() < n )
        {
            printf("Fegla won\n");
            return;
        }

        for (int j=1;j<vv[i].size();j++)
            if ( vv[i][j] != vv[i][0] ) 
                flag = false;

        if ( !flag )
        {
                 printf("Fegla won\n");
            return ;
        }
    }


//----------------here for optimality

    int ans = 0;
    for (int i=0;i<=UPPER;i++)
    {
        int help = MAXIMUM;
        for (int j=0;j<v[i].size();j++)
        {
            int marm = 0;
            for (int l=0;l<v[i].size();l++)
            {
                if ( v[i][l] > v[i][j] ) marm += v[i][l] - v[i][j];
                else marm += v[i][j] - v[i][l];
            }
            help = min(marm,help);
        }
        if ( help < MAXIMUM )
            ans = help+ ans;
    }
       
    printf("%d\n",ans);    
}


int main()
{

    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }

}
