#include<bits/stdc++.h>

using namespace std;

bool comp(const pair<long double, int> &i, const pair<long double, int> &j){
                        return i.first<j.first;
}

typedef pair<long double,int> point;

int main(){
        freopen("D-large.in","r",stdin);
        freopen("out6.txt","w",stdout);
        int tc,cas=0;
        cin>>tc;
        while(tc--){
                int n;
                cin>>n;
                point a[n];
                point b[n];
                for(int i=0;i<n;++i)
                        cin>>a[i].first, a[i].second=0;

                for(int i=0;i<n;++i)
                        cin>>b[i].first,b[i].second=0;

                 sort(a,a+n);
                 sort(b,b+n);

                 int j;
                 int cheat=0, fair=0;

                 int bstart=n-1, astart=n-1;
                 for(int k=astart; k>=0;--k){
                        if(a[k].second==0)
                        for(int l= bstart; l>=0;--l){
                                if(b[l]>a[k]&&b[l].second==0){
                                        fair++;
                                        bstart--;
                                        a[k].second=1;
                                        b[l].second=1;
                                        break;
                                }
                        }
                 }
                fair=n-fair;

                //Decptive game play begins

                for(int i=0;i<n;++i)
                        a[i].second=b[i].second=0;
                int pos_min=0,pos_max=n-1;
                for(int i=0;i<n;++i){
                        if(a[i]>b[pos_min]){
                                cheat++;
                                pos_min++;
                        }
                        else{
                                --pos_max;
                        }
                }

                 cout<<"Case #"<<++cas<<": ";
                 cout<<cheat<<" "<<fair<<endl;
        }
}
