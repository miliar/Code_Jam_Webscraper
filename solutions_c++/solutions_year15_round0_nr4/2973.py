
//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

//typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

//defines-general
#define to(a) __typeof(a)
#define all(vec)  vec.begin(),vec.end()
#define fill(a,val)  memset(a,val,sizeof(a))

//defines-iteration
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)
#define repii(i,a,b) for(__typeof(b) i = a;i<=b;i++)
#define repr(i,b,a) for(__typeof(b) i = b;i>a;i--)
#define repri(i,b,a) for(__typeof(b) i = b;i>=a;i--)
#define tr(vec,it)  for(__typeof(vec.begin())  it = vec.begin();it!=vec.end();++it)



//defines-pair
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

// my own
#define sl(a) scanf("%lld",&a)
#define sll(a,b) scanf("%lld%lld",&a,&b)
#define slll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define sllll(a,b,c,d) scanf("%lld%lld%lld%lld",&a,&b,&c,&d)
#define fastio   std::ios_base::sync_with_stdio(false)

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,X,R,C;
    int ctr=1;
    cin>>T;
    while(T--)
    {
        cin>>X>>R>>C;
        if(X>=7)
            cout<<"Case #"<<ctr<<": RICHARD"<<endl;
        else
        {
            if((R*C)%X!=0)
                cout<<"Case #"<<ctr<<": RICHARD"<<endl;
            else
            {
                int row=min(R,C);
                int col=max(R,C);
                switch(row)
                {
                case 1:
                    if(X>=3)
                        cout<<"Case #"<<ctr<<": RICHARD"<<endl;
                    else
                        cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    break;
                case 2:
                    if(X==5 || X==6)
                        cout<<"Case #"<<ctr<<": RICHARD"<<endl;
                    else if(col==2)
                    {
                       if(X==4)
                            cout<<"Case #"<<ctr<<": RICHARD"<<endl;
                       else
                            cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    }
                    else if(col==3)
                    {
                        if(X==6)
                            cout<<"Case #"<<ctr<<": RICHARD"<<endl;
                        else
                            cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    }
                    else if(col==4)
                    {
                         if(X==4)
                            cout<<"Case #"<<ctr<<": RICHARD"<<endl;
                        else
                            cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    }
                    else if(col==5)
                    {
                         if(X==5)
                            cout<<"Case #"<<ctr<<": RICHARD"<<endl;
                        else
                            cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    }
                    else
                        cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    break;
                case 3:
                    if(col==3)
                    {
                        if(X==6)
                            cout<<"Case #"<<ctr<<": RICHARD"<<endl;
                        else
                            cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    }
                    else if(col==4)
                    {
                         if(X==6)
                            cout<<"Case #"<<ctr<<": RICHARD"<<endl;
                        else
                            cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    }
                    else if(col==5)
                    {
                         if(X==6)
                            cout<<"Case #"<<ctr<<": RICHARD"<<endl;
                        else
                            cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    }
                    else
                        cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    break;
                case 4:
                        cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    break;
                case 5:
                        cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    break;
                default:
                    cout<<"Case #"<<ctr<<": GABRIEL"<<endl;
                    break;
                }
            }
        }
        ctr++;
    }
}
