#include<iostream>
#include<algorithm>
#define MAXM 1e18
using namespace std;

long long pw[105][105];

void calc_pw() {
    long long i,j;
    for(i=1;i<=100;i++) pw[i][0]=1,pw[1][i]=1;
    for(i=2;i<=100;i++) {
        for(j=1;pw[i][j-1]*i<=MAXM;j++) pw[i][j]=pw[i][j-1]*i;
    }
}

int main()
{
    freopen("gcj_16_qua_4_in.txt","r",stdin);
    freopen("gcj_16_qua_4_out.txt","w",stdout);
    int t;
    cin>>t;
    calc_pw();
    for(int qq=1;qq<=t;qq++) {
        cout<<"Case #"<<qq<<": ";
        long long i,j,k,c,s;
        cin>>k>>c>>s;
        for(i=0;i<s;i++) {
            cout<<i*pw[k][c-1]+1<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
