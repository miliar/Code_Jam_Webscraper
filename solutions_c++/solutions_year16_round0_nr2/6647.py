#include<bits/stdc++.h>
#define MAX 10000
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define ellapse printf("Time : %0.3lf\n",clock()*1.0/CLOCKS_PER_SEC);
using namespace std;
/*
//E,SE,S,SW,W,NW,N,NE
int dr[8]={0,1,1,1,0,-1,-1,-1};
int dc[8]={1,1,0,-1,-1,-1,0,1};
*/
typedef long long l64d;
typedef unsigned long int ud;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
int res = 100000000;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);

    //std::ios::sync_with_stdio(false);
    int t;
    char arr[105];
    l64d n;
    scanf("%d",&t);
    for(int i=0;i<t;i++) {
        res = 0;
        vector<int> pancake;
        queue<pair<bool, pair<int, vector<int> > > > bfs;
        scanf("%s", &arr);
        int len = strlen(arr);
        for(int j=0;j<len;j++) {
            if(arr[j] == '+') pancake.pb(1);
            else pancake.pb(0);
        }
        bfs.push(mp(1, mp(0, pancake)));
        while(!bfs.empty()) {
            pair<bool, pair<int, vector<int> > >  fr = bfs.front();
            bfs.pop();
            //checking front
            bool ok = 1;
            for(int i=0;i<fr.sc.sc.size();i++) {
                if(!fr.sc.sc[i]) ok = 0;
            }
            if(!ok) {
                if(!fr.fi) {
                    int ind = 0;
                    //flip partially
                    for(int i=1;i<fr.sc.sc.size();i++) {
                        fr.sc.sc[i-1] ^= 1;
                        if(fr.sc.sc[i-1] != fr.sc.sc[i]) {
                            ind = i;
                            break;
                        }
                    }
                    reverse(fr.sc.sc.begin(), fr.sc.sc.begin() + ind);
                    bfs.push(mp(1,mp(fr.sc.fi+1, fr.sc.sc)));
                }
                else {
                    //flip entirely
                    for(int i=0;i<fr.sc.sc.size();i++) {
                        fr.sc.sc[i] ^= 1;
                    }
                    reverse(fr.sc.sc.begin(), fr.sc.sc.end());
                    bfs.push(mp(0,mp(fr.sc.fi+1, fr.sc.sc)));
                    //normally
                    for(int i=0;i<fr.sc.sc.size();i++) {
                        fr.sc.sc[i] ^= 1;
                    }
                    reverse(fr.sc.sc.begin(), fr.sc.sc.end());
                    int ind = 0;
                    //flip partially
                    for(int i=1;i<fr.sc.sc.size();i++) {
                        fr.sc.sc[i-1] ^= 1;
                        if(fr.sc.sc[i-1] == fr.sc.sc[i]) {
                            ind = i;
                            break;
                        }
                    }
                    reverse(fr.sc.sc.begin(), fr.sc.sc.begin() + ind);
                    bfs.push(mp(1,mp(fr.sc.fi+1, fr.sc.sc)));
                }
            }
            else {
                res = fr.sc.fi;
                break;
            }
        }
        printf("Case #%d: %d\n", i+1, res);
    }

    #ifdef Xanxiver
    ellapse;
    #endif // Xanxiver
}
