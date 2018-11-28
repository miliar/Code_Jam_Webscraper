#include <iostream>
#include <ctype.h>
#include <stack>
#include <queue>
#include <limits.h>
#include <fstream>
#include <map>
#include <cmath>
#include <ctime>
#include <cstring>
#include <ctime>
#include <set>

#define rep(i, a) for(int i = 0; i < a; i++)
#define rep1(i, a) for(int i = 1; i <= a; i++)
#define fo(i, a, b) for(int i = a; i < b; i++)
#define defo(i, a, b) for(int i = a; i >= b; i--)
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a.size()))
#define x first
#define y second
#define SET(x, a) memset(x, a, sizeof(x));
using namespace std;

int main(){
     ofstream f;
     f.open("e1.txt");
    int test;
    cin>>test;
    int l = 0;
    while(test--){
        l++;
        int arr[5][5];
        int x[17]={0};
        int i,j,r1,r2,ans,no=0;
        cin>>r1;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>arr[i][j];
            }
        }
        for(j=0;j<4;j++){
            x[arr[r1-1][j]] = 1;
        }
        cin>>r2;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>arr[i][j];
            }
        }
        for(j=0;j<4;j++){
            if(x[arr[r2-1][j]]==1){
                ans = arr[r2-1][j];
                no++;
            }
        }
        f<<"Case #"<<l<<": ";
        if(no==1){
            f<<ans<<"\n";
        }
        else if(no==0){
            f<<"Volunteer cheated!\n";
        }
        else{
            f<<"Bad magician!\n";
        }
    }
    return 0;
}
