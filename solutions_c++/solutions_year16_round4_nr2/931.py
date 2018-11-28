#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
#include<string>
#define pb push_back
using namespace std;

int T,N,K,viz[210];
double p[210];
vector<vector<int> > combi;

int main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        printf("Case #%d: ",t);
        scanf("%d%d",&N,&K);
        double maP = 0;
        for(int i=1;i<=N;++i) {
            scanf("%lf",&p[i]);
        }
        combi.clear();
        for(int l=0;l<(1<<K);++l) {
            int x = l;
            int k = 0;
            for(int i=1;i<=K;++i) {
                if(x%2) {
                    viz[i] = 1;
                    ++k;
                } else {
                    viz[i] = 0;
                }
                x/=2;
            }
            if(k==K/2) {
                vector<int> v;
                for(int i=1;i<=N;++i) {
                    v.pb(viz[i]);
                }
                combi.pb(v);
            }
        }
        for(int l=0;l<(1<<N);++l) {
            int x = l;
            int k = 0;
            for(int i=1;i<=N;++i) {
                if(x%2) {
                    viz[i] = 1;
                    ++k;
                } else {
                    viz[i] = 0;
                }
                x/=2;
            }
            if(k==K) {
                double P = 0.0;
                for(auto c:combi) {
                    int curr = 0;
                    double pipi = 1.0;
                    for(int i=1;i<=N;++i) {
                        if(viz[i]) {
                            if(c[curr]) {
                                pipi *= p[i];
                            } else {
                                pipi *= (1-p[i]);
                            }
                            ++curr;
                        }
                    }
                    P += pipi;
                }
                maP = max(maP,P);
            }
        }
        
        printf("%.10lf\n",maP);
    }
    return 0;
}

