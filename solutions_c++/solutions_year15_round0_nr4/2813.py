#include<bits/stdc++.h>

using namespace std;

int main()
{
    int casos;

    vector < set <pair<int,int> > > tabla(4);
    tabla[0].insert(make_pair(1,1));
    tabla[0].insert(make_pair(1,2));
    tabla[0].insert(make_pair(1,3));
    tabla[0].insert(make_pair(1,4));
    tabla[0].insert(make_pair(2,2));
    tabla[0].insert(make_pair(2,3));
    tabla[0].insert(make_pair(2,4));
    tabla[0].insert(make_pair(3,3));
    tabla[0].insert(make_pair(3,4));
    tabla[0].insert(make_pair(4,4));
    tabla[1].insert(make_pair(1,2));
    tabla[1].insert(make_pair(1,4));
    tabla[1].insert(make_pair(2,2));
    tabla[1].insert(make_pair(2,3));
    tabla[1].insert(make_pair(2,4));
    tabla[1].insert(make_pair(3,4));
    tabla[1].insert(make_pair(4,4));
    tabla[2].insert(make_pair(2,3));
    tabla[2].insert(make_pair(3,3));
    tabla[2].insert(make_pair(3,4));
    tabla[3].insert(make_pair(4,3));
    tabla[3].insert(make_pair(4,4));

    cin >> casos;
    for(int i = 0 ; i < casos ; i++)
    {
        int X,R,C;
        cin >> X >> R >> C;
        if(tabla[X-1].find(make_pair(R,C))!=tabla[X-1].end()||tabla[X-1].find(make_pair(C,R))!=tabla[X-1].end())
            printf("Case #%d: GABRIEL\n",i+1);
        else
            printf("Case #%d: RICHARD\n",i+1);
    }

    return 0;
}
