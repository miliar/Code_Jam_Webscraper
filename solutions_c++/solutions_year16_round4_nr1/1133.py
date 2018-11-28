#include<bits/stdc++.h>
using namespace std;

int T,n;
int P,R,S;
int z[3];//R,R,S
int main(){
    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    fscanf(in,"%d",&T);
    for(int t=1;t<=T;t++){
        fscanf(in,"%d%d%d%d",&n,&z[1],&z[0],&z[2]);
        int cd[3];
        int nn=1;
        for(int o=0;o<n;o++) nn*=2;
        cd[0] = cd[1] = cd[2] = nn/3;
        cd[2]++;
        if(n%2==1) cd[1]++;
        bool ok = true;
        pair<int,int> v[3];
        for(int i=0;i<3;i++) {v[i].first=z[i];v[i].second=i;}
        sort(v,v+3);
        for(int i=0;i<3;i++){
            if(v[i].first!=cd[i]) ok=false;
        }
        if(!ok) fprintf(out,"Case #%d: IMPOSSIBLE\n",t);
        else{
            string now[3]={"PR","PS","RS"};
            string tmp[3];
            int _n=1;
            while(_n<n){
                _n++;
                for(int i=0;i<3;i++) {
                    tmp[i] = now[i];
                    now[i] = "";
                }
                for(int i=0;i<3;i++){
                    int k=tmp[i].length();
                    for(int j=0;j<k;j++){
                        if(tmp[i][j]=='P') now[i]+="PR";
                        if(tmp[i][j]=='R') now[i]+="RS";
                        if(tmp[i][j]=='S') now[i]+="PS";
                    }
                }
            }
            int idx=0;
            for(;idx<3;idx++){
                int _p=0,_r=0,_s=0;
                for(int i=0;i<now[idx].length();i++){
                    if(now[idx][i]=='P') _p++;
                    if(now[idx][i]=='R') _r++;
                    if(now[idx][i]=='S') _s++;
                }   
                if(z[0]==_p&&z[1]==_r&&z[2]==_s) break;
            }
            int unit=2;
            string ans="";
            string tt=now[idx];
            int len = now[idx].length();
            for(int _=1;_<n;_++){
                unit*=2;
                for(int i=0;i<(len/unit);i++){
                    string t1= tt.substr(i*unit,unit/2);
                    string t2= tt.substr(i*unit+unit/2,unit/2);
                    if(t1>t2) ans+=(t2+t1);
                    else ans+=(t1+t2);
                }
                tt=ans;
                ans="";
            }
            fprintf(out,"Case #%d: %s\n",t,tt.c_str());
        }
    }
}
