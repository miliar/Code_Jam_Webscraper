#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<map>
#include<set>
#include<vector>

using namespace std;

typedef pair<int,int> pii;
typedef vector<pii> vii;
typedef vector<int> vi;

#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define DFOR(i,a,b) for(int i=a;i>=b;i--)
#define mp(x,y) make_pair((int)x,(int)y)
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(x,a,b) {cout << #x << " = "; FOR(i,a,b) cout << x[i] << ' '; cout << endl;}
#define ll long long
#define DEBUG 1
int test;
int ans1;
int ans2;
int a[5][5];
int b[5][5];
int main(){
    if (DEBUG==1){
        freopen("A-small-attempt0.in","r",stdin);
        freopen("output.txt","w",stdout);
    }
    cin>>test;
    FOR(cstest,1,test){
        cin>>ans1;
        //cout<<ans1<<endl;
        FOR(i,1,4)FOR(j,1,4){
            int number;
            cin>>number;
            a[i][j]=number;
        }
        cin>>ans2;
        //cout<<ans2<<endl;
        FOR(i,1,4)FOR(j,1,4){
            int number;
            cin>>number;
            b[i][j]=number;
        }
        int dem=0;
        int value=0;
        FOR(j1,1,4){
            int tmp= a[ans1][j1];
            //cout<<tmp<<endl;
            FOR(j2,1,4){
                //cout<<"___"<<b[ans2][j2]<<endl;
                if (tmp==b[ans2][j2]){
                dem++;
                value= tmp;
                break;
                }
            }
        }
        cout<<"Case #"<<cstest<<": ";
        if (dem==1) cout<<value<<endl;
        else if (dem>1) cout<<"Bad magician!"<<endl;
        else cout<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
