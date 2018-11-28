#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("outputL.out","w",stdout);

    int T,runn;
    int n;
    int i,dmx,p[1001];
    int aa,ab;


    cin >> T;
    for(runn=1;runn<=T;runn++){
        dmx=0; aa=0; ab=0;
        cin >> n;
        for(i=0;i<n;i++){
            cin >> p[i];
            if(i>0) dmx=max(dmx,p[i-1]-p[i]);
        }
        for(i=0;i<n;i++){
            if(p[i-1]>p[i]&&i!=0){
                aa+=p[i-1]-p[i];
            }
            if(i!=n-1) ab+=min(dmx,p[i]);
        }
        printf("Case #%d: %d %d\n",runn,aa,ab);
    }
}
