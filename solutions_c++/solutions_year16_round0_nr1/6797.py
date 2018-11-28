#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<map>
#include<set>
#include<vector>
#include<queue>
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

int main(){
    if (DEBUG==1){
        freopen("A-large.in","r",stdin);
        freopen("output.txt","w",stdout);
    }
    int t;
    cin>>t;
    bool c[20];
    int n;
    FOR(i,1,t){
        cin>>n;
        if (n==0){
            cout<<"Case #"<<i<<": INSOMNIA";
            if(i<t) cout<<endl;
            continue;
        }
        for(int j=0;j<=9;j++) c[j]=false;
        int m=1;
        while (n%10==0){
            c[0]=true;
            n=n/10;
            m=m*10;
        }
        int value=n;
        int res=-1;
        for(int counter=1;counter<=2000; counter++){
            int tmp=value;
            while (tmp!=0){
                c[tmp%10]=true;
                tmp=tmp/10;
            }
            bool fin= true;
            for(int j=0;j<=9;j++) if (c[j]==false) {
                fin=false;
                break;
            }
            if (fin){
                res= counter;
                break;
            }else{
                value+=n;
            }
        }
        cout<<"Case #"<<i<<": ";
        if(res<0) cout<<"INSOMNIA";else cout<<(value*m);
        if (i<t) cout<<endl;
    }
    return 0;
}
