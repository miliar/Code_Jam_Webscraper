#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath>
using namespace std;
double a[2000],b[2000];
int v[2000];
int main()
{
    freopen("D2.in","r",stdin);
    freopen("D2.out","w",stdout);
    int T;
    cin>>T;
    for(int cas = 1; cas <= T; cas++){
        cout<<"Case #"<<cas<<": ";
        int n, i, j;
        cin>>n;
        for (i = 0; i < n; i++) cin>>a[i];
        for (i = 0; i < n; i++) cin>>b[i];
        sort(a,a+n);
        //for (i = 0; i < n; i++) cout<<a[i]<<' ';cout<<endl;
        sort(b,b+n);

        //for (i = 0; i < n; i++) cout<<b[i]<<' ';cout<<endl;
        int y = 0, z = 0;
        memset(v,0,sizeof(v));
        for (i = 0; i < n; i++){
            int flag = 0;
            for (j = 0; j < n; j++)
                if (!v[j] && a[i]<b[j]) {
                    flag = 1;
                    v[j] = 1;
                    break;
                }
            if (flag) ;
            else {for (j = 0; j < n; j++)
                    if (!v[j]) {
                        v[j] = 1;
                        break;
                    }
                z++;
            }
        }
        for (i = 0; i < n; i++){
            double t = a[i];
            a[i] = b[i];
            b[i] = t;
        }
        memset(v,0,sizeof(v));
        for (i = 0; i < n; i++){
            int flag = 0;
            for (j = 0; j < n; j++)
                if (!v[j] && a[i]<b[j]) {
                    flag = 1;
                    v[j] = 1;
                    y++;
                    break;
                }
            if (flag) ;
            else {for (j = 0; j < n; j++)
                    if (!v[j]) {
                        //cout<<j<<' '<<b[j]<<endl;
                        v[j] = 1;
                        break;
                    }
            }
        }
        cout<<y<<' '<<z<<endl;
    }
    return 0;
}


