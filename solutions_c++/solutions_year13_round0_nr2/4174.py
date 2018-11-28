#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>

#define ull unsigned long long
//#define DEBUG

#define HORIZ 0
#define VERT 1

using namespace std;

int n, m;
int h[100][100];
bool acc [100][100]; //has this height been accounted for?


void init(){

    for(int i =0;i<100;i++){
        for(int j =0;j<100;j++){
            h[i][j] = acc[i][j] = 0;
        }

    }
}

int largest(int p, int flag){
    int answer = 0;
    if(flag==HORIZ){
        for(int q = 0;q<m;q++){
            answer = max(answer,h[p][q]);
        }
    }
    else
        for(int q = 0;q<n;q++){
            answer = max(answer,h[q][p]);
        }

    return answer;
}

bool yes(){

    for(int i = 0;i<n;i++){
        for(int j =0;j<m;j++){
            if(acc[i][j]==0) return false;
        }
    }
    return true;
}

int main ()
{
    #ifndef DEBUG
        freopen ("B-large.in","r",stdin);
        freopen ("B-large.out","w",stdout);
    #endif
    int t; cin>>t;
    for (int _t=0;_t<t;_t++){
        init();
        cin>>n>>m;
        for(int i =0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>h[i][j];

            }

        }

        for(int i = 0;i<n;i++){
            int maxi = largest(i,HORIZ);
            for(int j = 0;j<m;j++){
                if(h[i][j]==maxi) acc[i][j] = true;
            }

        }

        for(int j = 0;j<m;j++){
            int maxi = largest(j,VERT);
            for(int i=0;i<n;i++){
                if(h[i][j]==maxi) acc[i][j] = true;
            }

        }

        cout<<"Case #"<<_t+1<<": ";

        if(yes())
            cout<<"YES";
        else
            cout<<"NO";

        cout<<endl;

    }

    return 0;
}

