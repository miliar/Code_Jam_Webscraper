#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

pair<long double, bool> naom[11150];
pair<long double, bool> ken[11150];

int main(){
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T;
    cin>>T;
    for(int i=1;i<=T;i++){
        cout<<"Case #"<<i<<": ";
        int N;
        pair<long double, bool> Npar;
        cin>>N;
        for(int j=0;j<N;j++){
            cin>>Npar.first;
            Npar.second=false;
            naom[j]=Npar;
        }
        for(int j=0;j<N;j++){
            cin>>Npar.first;
            Npar.second=false;
            ken[j]=Npar;
        }
        sort(naom, naom+N);
        sort(ken, ken+N);
        long double ln, lk;
        int solW=0,solDW=0;
        int nk=0;
        ///SOLW
        for(int j=0;j<N;j++){
            ln=naom[j].first;
            lk=-1;
            for(int k=nk;k<N;k++){
                if(!ken[k].second){
                    if(ken[k].first>ln){
                        ken[k].second=true;
                        lk=ken[k].first;
                        nk=k;
                        break;
                    }
                }
            }
            if(lk==-1){
                for(int k=0;k<N;k++){
                   if(!ken[k].second){
                        ken[k].second=true;
                        lk=ken[k].first;
                        solW++;
                        break;
                    }
                }
            }
        }
        for(int k=0;k<N;k++) ken[k].second=false;
        nk=0;
        ///SOLDW
        for(int j=0;j<N;j++){
            ln=naom[j].first;
            lk=-1;
            for(int k=nk;k<N;k++){
                if(!ken[k].second){
                    if(ken[k].first<ln){
                        ken[k].second=true;
                        lk=ken[k].first;
                        nk=k;
                        solDW++;
                    }
                    break;
                }
            }
            if(lk==-1){
                for(int k=N-1;k>=0;k++){
                    if(!ken[k].second){
                        ken[k].second=true;
                        lk=ken[k].first;
                        break;
                    }
                }
            }
        }
        cout<<solDW<<" "<<solW<<endl;
    }
    return 0;
}
