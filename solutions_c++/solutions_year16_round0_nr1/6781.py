/*
    Author: 0Alien0
    School: NCTU
*/
#include<bits/stdc++.h>

#define FI freopen("in.txt", "r", stdin)
#define IOS ios_base::sync_with_stdio(0);cin.tie(0)
#define PB push_back
#define MP make_pair
#define MT make_tuple
#define ff first
#define ss second
#define EPS 1E-7
#define INF 0x7FFFFFFF
#define PI 3.1415926535897932384626433832795

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef vector<int> VII;
typedef vector<LL> VLL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;

//int dx[]={1,0,-1,0};              int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};    int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};   int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={2,1,-1,-2,-1,1};        int dy[]={0,1,1,0,-1,-1}; //Hexagonal Direction

int main(){
    IOS;
    FI;
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        int N;
        cin >> N;
        cout << "Case #" << i << ": ";
        if(N == 0){cout << "INSOMNIA" << endl;continue;}
        bool number[10]={};
        int done=0,Ans;
        for(int i=1;;i++){
            int sheep=i*N;
            while(sheep > 0){
                if(number[sheep%10] == false){number[sheep%10]=true;done++;}
                sheep/=10;
            }
            if(done == 10){Ans=i*N;break;}
        }
        cout << Ans << endl;
    }
    return 0;
}
