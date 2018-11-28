#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath>
using namespace std;
int v[100];
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    cin>>T;
    for(int cas = 1; cas <= T; cas++){
        cout<<"Case #"<<cas<<": ";
        memset(v, 0 ,sizeof(v));
        int r1, i, j, r2, k;
        cin>>r1;
        for (i = 1; i <= 4; i++)
            for (j = 0; j < 4; j++){
                cin>>k;
                if (i == r1) v[k]++;
            }
        cin>>r2;
        int flag = 0, t;
        for (i = 1; i <= 4; i++)
            for (j = 0; j < 4; j++){
                cin>>k;
                if (i == r2)
                    if (v[k]) flag++, t = k;
            }
        if (flag == 0) cout<<"Volunteer cheated!"<<endl;
        else if (flag == 1) cout<<t<<endl;
        else cout<<"Bad magician!"<<endl;
    }
    return 0;
}


