#include<bits/stdc++.h>

//#define fin cin
//#define fout cout
#define LL long long
#define pb push_back
#define pi acos(-1)
#define MOD 1000000007
#define MX 32622
using namespace std;

int main(){
    ofstream fout ("output.out");
    ifstream fin ("input.in");
    int test;
    fin>>test;
    for(int kase=1;kase<=test;kase++){
        vector<int>a,b;
        a.clear();
        b.clear();
        int r;
        fin>>r;
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                int val;
                fin>>val;
                if(i==r) a.pb(val);
            }
        }
        fin>>r;
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                int val;
                fin>>val;
                if(i==r) b.pb(val);
            }
        }
        int res,cnt=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(a[i]==b[j]){
                    cnt++;
                    res=a[i];
                }
            }
        }
        fout<<"Case #"<<kase<<": ";
        if(cnt==0) fout<<"Volunteer cheated!"<<endl;
        else if(cnt>1) fout<<"Bad magician!"<<endl;
        else fout<<res<<endl;
    }
    return 0;
}
