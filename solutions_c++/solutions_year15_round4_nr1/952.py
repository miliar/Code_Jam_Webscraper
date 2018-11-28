#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include<iomanip>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define pb push_back
#define sz size()
#define ln length()
#define fore(i,a,b) for(int i=a;i<b;i++)
#define fores(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%d",&a)
#define md 1000000007

int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
		printf("Case #%d: ",z+1);
		int r,c;
		cin>>r>>c;
		vector<string> mat;
		fore(i,0,r)
		{
		    string s;
		    cin>>s;
		    mat.pb(s);
		}
		int fa = 0;
		bool mfound = false;
		fore(i,0,r)
		{
		    fore(j,0,c)
		    {
		        if(mat[i][j]=='.')
                    continue;
                int dx = 0,dy = 0;
                if(mat[i][j]=='^')
                    dx = -1;
                else if(mat[i][j]=='v')
                    dx = 1;
                else if(mat[i][j]=='>')
                    dy = 1;
                else if(mat[i][j]=='<')
                    dy = -1;
                int x = i,y = j;
                bool found = false;
                x+=dx;
                y+=dy;
                while(x>=0 && x<r && y>=0 && y<c)
                {
                    if(mat[x][y]!='.')
                    {
                        found = true;
                        break;
                    }
                    x+=dx;
                    y+=dy;
                }
                if(found)
                    continue;
                x = i,y = j;
                dx = -1;dy = 0;
                found = false;
                x+=dx;
                y+=dy;
                while(x>=0 && x<r && y>=0 && y<c)
                {
                    if(mat[x][y]!='.')
                    {
                        found = true;
                        break;
                    }
                    x+=dx;
                    y+=dy;
                }
                if(found)
                {
                    fa++;
                    continue;
                }
                x = i,y = j;
                dx = 1;dy = 0;
                found = false;
                x+=dx;
                y+=dy;
                while(x>=0 && x<r && y>=0 && y<c)
                {
                    if(mat[x][y]!='.')
                    {
                        found = true;
                        break;
                    }
                    x+=dx;
                    y+=dy;
                }
                if(found)
                {
                    fa++;
                    continue;
                }
                x = i,y = j;
                dx = 0;dy = -1;
                found = false;
                x+=dx;
                y+=dy;
                while(x>=0 && x<r && y>=0 && y<c)
                {
                    if(mat[x][y]!='.')
                    {
                        found = true;
                        break;
                    }
                    x+=dx;
                    y+=dy;
                }
                if(found)
                {
                    fa++;
                    continue;
                }
                x = i,y = j;
                dx = 0;dy = 1;
                found = false;
                x+=dx;
                y+=dy;
                while(x>=0 && x<r && y>=0 && y<c)
                {
                    if(mat[x][y]!='.')
                    {
                        found = true;
                        break;
                    }
                    x+=dx;
                    y+=dy;
                }
                if(found)
                {
                    fa++;
                    continue;
                }
                else
                {
                    mfound = true;
                    break;
                }
		    }
		    if(mfound)
                break;
		}
		if(mfound)
        {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        cout<<fa<<endl;
	}
	return 0;
}
