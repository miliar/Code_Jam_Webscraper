#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <string>

using namespace std;

int T,t;
int n,m;
const long long MM = 1000002013;

struct point{
    int code,mode,num;
};

long long cal(long long x)
{
    return x*n-x*(x-1)/2;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>T;
    while (t<T){
        t++;
        cin>>n>>m;
        int o[1100],e[1100],p[1100],cnt = 0;
        point z[3000],s[3000];
        long long sum = 0;
        for (int i = 1; i<=m; i++){
            cin>>o[i]>>e[i]>>p[i];
            sum = (sum+p[i]*cal(e[i]-o[i]))%MM;
            cnt++;
            z[cnt].code = o[i];
            z[cnt].mode = 0;
            z[cnt].num = p[i];
            cnt++;
            z[cnt].code = e[i];
            z[cnt].mode = 1;
            z[cnt].num = p[i];
        }
        for (int i = 1; i<=cnt; i++)
            for (int j = i+1; j<=cnt; j++){
                if (z[i].code>z[j].code||z[i].code==z[j].code&&z[i].mode>z[j].mode){
                    point tmp;
                    tmp = z[i]; z[i] = z[j]; z[j] = tmp;
                }
            }
        long long ans = 0;
        int top = 0;
        for (int i = 1; i<=cnt; i++){
            if (top==0){
                top++;
                s[top] = z[i];
            }
            else{
                
                    if (z[i].mode==1){
start:                  int delta = min(z[i].num,s[top].num);
                        ans = (ans+cal(z[i].code-s[top].code)*delta)%MM;
                        z[i].num-=delta;
                        s[top].num-=delta;
                        if (s[top].num==0) top--;
                        if (z[i].num>0&&top>0) goto start;
                    }
                    else{
                        top++;
                        s[top] = z[i];
                    }
            }
        }
        //cout<<sum<<"  "<<ans<<endl;
        ans = (sum-ans)%MM;
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
