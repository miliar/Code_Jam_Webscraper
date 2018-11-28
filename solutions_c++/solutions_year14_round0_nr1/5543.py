#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>

#define forn(i,n) for(int i=0;i<n;i++)
#define all(v) v.begin(),v.end()

using namespace std;

int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int casos;
	cin >> casos;
	forn(casito,casos)
	{
        int a, b;
        vector<vector<int> > vec1(4),vec2(4);
        cin >> a;
        a--;
        forn(i,4)
        {
            vec1[i].resize(4);
            forn(j,4)
                cin >> vec1[i][j];
        }
        cin >> b;
        b--;
        forn(i,4)
        {
            vec2[i].resize(4);
            forn(j,4)
                cin >> vec2[i][j];
        }
        set<int> setint;
        forn(i,4)
        forn(j,4)
        if(vec1[a][i] == vec2[b][j])
            setint.insert(vec1[a][i]);
        cout << "Case #" << casito+1 <<": ";
        if(setint.size()==1)
            cout << *setint.begin();
        else if(setint.size()==0)
            cout << "Volunteer cheated!";
        else
            cout << "Bad magician!";
        cout << endl;
	}
}
