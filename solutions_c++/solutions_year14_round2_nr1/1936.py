#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

#define forn(i,n) for(int i = 0; i<(int) n; i++)
#define forns(i,n,s) for(int i = s; i<n; i++)
#define forn1(i,n) for(int i = 1; i<=(int) n; i++)

#define dforn(i,n) for(int i = n; i>=0; i--)
#define dforn2(i,n,s) for(int i = n; i>=s; i--)

#define MAX 1048576
#define pb push_back
#define mp make_pair

using namespace std;
int cases,n;
string s[2];

int cada [100][2];
int main()
{
   	freopen("input.txt", "r", stdin);
   	freopen("output.txt", "w", stdout);
    cin>>cases;
    forn(i,cases)
    {
        cout<<"Case #"<<i+1<<": ";
        forn(j,100)
          forn(k,2)
           cada[j][k]=0;
        int resp=0;
        cin>>n;
        forn(j,n)
            cin>>s[j];
        int cont = 0;
        string resp1[2];
        forn(a,2)
        {
            cont =0;
            resp1[a][0]=s[a][0];
            forn(j,s[a].size())
            if(s[a][j]==s[a][j+1])
                cada[cont][a]++;
            else
            {
                resp1[a]+=s[a][j];
                cont++;
            }
        }
        if(!(resp1[0]==resp1[1]))
            cout<<"Fegla Won"<<endl;
        else
        {
            forn(i,cont)
            {
                resp+=abs(cada[i][0]-cada[i][1]);
            }
              cout<<resp<<endl;
        }
    }
    return 0;
}
