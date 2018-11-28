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
vector<int> ok;
bool seen[15] = {};
int main()
{
    freopen("A-large(1).in","r",stdin);
    freopen("A-large(1).out","w",stdout);

    //std::ios::sync_with_stdio(false);
    int t;
    string s,hsl = "",tmp;
    cin>>t;
    for(int i=0;i<t;i++) {
        hsl = "";
        cin>>s;
        hsl += s[0];
        for(int j=1;j<s.size();j++) {
            if(s[j] < hsl[0]) hsl += s[j];
            else {
                tmp = s[j];
                tmp += hsl;
                hsl = tmp;
            }
        }
        cout<<"Case #"<<(i+1)<<": "<<hsl<<endl;
    }

    #ifdef Xanxiver
    ellapse;
    #endif // Xanxiver
}
