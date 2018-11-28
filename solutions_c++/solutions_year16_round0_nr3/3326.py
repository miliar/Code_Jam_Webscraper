#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
using namespace std;

vector< unsigned long long >p,dv;
//vector< pair<unsigned long long,unsigned long long > >dv;
long long pw[20][20];

void calc_pw() {
    unsigned long long i,j;
    for(i=0;i<=16;i++) pw[i][0]=1;
    for(i=2;i<=10;i++) {
        for(j=1;j<=16;j++) {
            pw[i][j]=pw[i][j-1]*i;
        }
    }
}

void print(unsigned long long num,unsigned long long n) {
    unsigned i;
    for(i=16;i>=1;i--) {
        if(num&pw[2][i-1]) cout<<"1";
        else cout<<"0";
    }
}

int main()
{
    freopen("gcj_16_qua_3_in.txt","r",stdin);
    freopen("gcj_16_qua_3_out.txt","w",stdout);
    int t;
    t=1;
    while(t--) {
        calc_pw();
        cout<<"Case #1:\n";
        unsigned long long i,j=50,n,m,temp,x,y;
        for(i=1;i<=5761455;i++) cin>>temp,p.push_back(temp);
        for(i=0;i<(1<<16);i++) {
            if(j<=0) break;
            if(i&1 && (i&(1<<15))) {
                for(x=2;x<=10;x++) {
                    temp=0;
                    for(y=0;y<16;y++) {
                        if(i&(1<<y)) temp+=pw[x][y];
                    }
                    for(y=0;y<p.size();y++) {
                        if(temp%p[y]==0 && temp!=p[y]) { break; }
                    }
                    if(y==p.size()) break;
                    else dv.push_back(p[y]);
                }
                if(x>10) {
                    print(i,16); cout<<" ";
                    for(y=0;y<dv.size();y++) cout<<dv[y]<<" ";
                    cout<<"\n"; j--;
                }
                dv.clear();
            }
        }
    }
    return 0;
}
