#include<stdio.h>
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string a,b;
int T,N;
bool viza[26], vizb[26];

void reset_viz() {
    for(int i=0;i<26;++i) {
        viza[i]=0;
        vizb[i]=0;
    }
}


int main() {
    freopen("input.txt","r",stdin);
    freopen("output2.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        printf("Case #%d: ",t);
        scanf("%d",&N);
        cin>>a>>b;
        if(a[0]!=b[0]) {
            printf("Fegla Won\n");
            continue;
        }
        bool ok =1;
        int ret=0;
        int x=0, y=0;
        while(x<a.size() && y<b.size()) {
            //printf("%d %c,  %d %c\n",x,a[x],y,b[y]);
            viza[a[x]-'a']=1;
            vizb[b[y]-'a']=1;
            if(a[x]==b[y]) {
                ++x;
                ++y;
            } else if(a[x]!=b[y]) {
                if(a[x]==a[x-1]) {
                    ++x;
                    ++ret;
                } else if(b[y]==b[y-1]) {
                    ++y;
                    ++ret;
                } else {
                    ok=0;
                    break;
                }
            }
        }
        if(x<a.size()) {
            //`cout<<"hallo";
            for(int i=x;i<a.size();++i) {
          
                if(a[x-1]==a[i]) {
                    ++ret;
                } else {
                    ok=0;
                    break;
                }
            }
        } else if(y<b.size()) {
            for(int i=y;i<b.size();++i) {
                if(b[y-1]==b[i]) {
                    ++ret;
                } else {
                    ok=0;
                    break;
                }
            }
        }
        if(ok) {
            printf("%d\n",ret);
        } else {
            printf("Fegla Won\n");
        }
    }
    return 0;
}
