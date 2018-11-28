#include <iostream>
#include <stdio.h>
#include <queue>
#include <vector>
#include <set>
#include <iomanip>
#include <algorithm>
#include <string.h>
#include <ctype.h>
#include <math.h>
using namespace std;

#define pb push_back
#define X first
#define Y second
#define ll long long
#define MAX 1000000000
#define fi freopen("A-small-attempt0.in","r",stdin);

int t,n,m,a[5][5],b[5][5];

int main()
{
    fi;
    freopen("out.out","w",stdout);
    cin>>t;
    for(int cas=1;cas<=t;cas++) {
        cout<<"Case #"<<cas<<": ";
        cin>>n;
        n--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        cin>>m;
        m--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>b[i][j];
        int cnt=0,pos=0;
        for(int i=0;i<4;i++) {
            for(int j=0;j<4;j++) {
                if(a[n][i]==b[m][j]) {
                    cnt++;
                    pos=a[n][i];
                }
            }
        }
        if(cnt==0)
            cout<<"Volunteer cheated!\n";
        else if(cnt==1)
            cout<<pos<<"\n";
        else
            cout<<"Bad magician!\n";
    }
}
