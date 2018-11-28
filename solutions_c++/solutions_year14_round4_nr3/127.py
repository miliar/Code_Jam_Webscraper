#include<iostream>
#include<fstream>
#include<string>
#include<bitset>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
using namespace std;
typedef pair<int,int> pii;
typedef pair<pii, pii > building;

int DP[1000];
bool visited[1000];
building bs[1000];

int vdist(building a, building b){
    if (a.first.first < b.first.second && b.first.first < a.first.second) return 0;
    if (a.first.second <= b.first.first) return b.first.first - a.first.second;
    if (a.first.first >= b.first.second) return a.first.first - b.first.second;
}
int hdist(building a, building b){
    if (a.second.first < b.second.second && b.second.first < a.second.second) return 0;
    if (a.second.second <= b.second.first) return b.second.first - a.second.second;
    if (a.second.first >= b.second.second) return a.second.first - b.second.second;
}

int dist(building a, building b){
    return max(hdist(a,b), vdist(a,b));
}

int main(){
    ifstream in("C.in"); ofstream out("C.out");
    int T;
    in>>T;
    for (int t=0;t<T;t++){
        out<<"Case #"<<t+1<<": ";
        int W,H,B;
        in>>W>>H>>B;
        for (int i=0;i<B;i++){
            int a,b,c,d;
            in>>a>>b>>c>>d;
            bs[i] = make_pair(make_pair(a,c+1),make_pair(b,d+1));
            DP[i] = a;
            visited[i] = false;
            //cout<<"["<<bs[i].first.first<<","<<bs[i].first.second<<"]x["<<bs[i].second.first<<","<<bs[i].second.second<<"]\n";
        }/*
        for (int i=0;i<B;i++){
            for (int j=0;j<B;j++){
                cout<<dist(bs[i],bs[j])<<" ";
            }
            cout<<"\n";
        }*/

        for(int k  = 0; k<B;k++){
            int mindist = W+1;
            int minind = -1;
            for (int i=0;i<B;i++){
                if (DP[i]<mindist && !visited[i]){
                    mindist = DP[i];
                    minind = i;
                }
            }
            visited[minind] = true;
            for (int i=0;i<B;i++){
                DP[i] = min(DP[i],DP[minind]+dist(bs[i],bs[minind]));
            }
        }
        int ans = W;
        for (int i=0;i<B;i++){
            //cout<<DP[i]<<"\n";
            ans = min(ans,DP[i] + W - bs[i].first.second);
        }
        out<<ans<<"\n";
    }
}
