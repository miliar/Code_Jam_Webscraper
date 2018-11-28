//problem name
//url 
/*Analysis:
 */

#include  <bits/stdc++.h>//include all stl
#define LL long long
#define ULL unsigned LL
#define FOR(i,n) for(int i=0;i<n;i++)
#define ALL(v) begin(v),end(v)
#define UNIQUE(c) (c).resize(unique(ALL(c)) - (c).begin())
#define PRINT(v,sep) {copy(begin(v), end(v)-1, ostream_iterator<int>(cout, sep)); cout << *(end(v)-1)<<endl;}
#define MAX(v) accumulate(ALL(v),INT_MIN,[](int a,int b){return max(a,b);})
#define MIN(v) accumulate(ALL(v),INT_MAX,[](int a,int b){return min(a,b);})
using namespace std;
template<typename T>
inline T SUM(const vector<T>& v){
    return accumulate(ALL(v),T(0),[](T a,T b){return a+b;});
}

typedef vector<int>   VI;       typedef vector<bool> VB;
typedef vector<VI>   VVI;       typedef vector<double> VD;
typedef vector<VVI> VVVI;       typedef vector<VD> VDD;

typedef pair<int,int> PI;       typedef pair<double,double> PD;
typedef pair<PI,int> PII;

int main(){
    ios::sync_with_stdio(false);
    int T;
    cin>>T;
    FOR(t,T){
        int N;
        cin>>N;
        priority_queue<pair<int,char> > seq;
        int remaining = 0;
        FOR(i,N){
            int a;
            cin>>a;
            seq.push(PI{a,i+'A'});
            remaining+=a;
        }
        cout<<"Case #"<<t+1<<":";
        while(remaining){
            auto first = seq.top(); seq.pop();
            auto second = seq.top(); seq.pop();
            if(first.first>2){
                if(second.first==first.first){
                    cout<<" "<<first.second<<second.second;
                    first.first-=1;
                    second.first-=1;
                    seq.push(first);
                    seq.push(second);
                }else{
                    cout<<" "<<first.second<<first.second;
                    first.first-=2;
                    seq.push(first);
                    seq.push(second);
                }
                remaining-=2;
            } else if(first.first==2){
                if(second.first==first.first){
                    cout<<" "<<first.second<<second.second;
                    first.first-=1;
                    second.first-=1;
                    seq.push(first);
                    seq.push(second);
                    remaining-=2;
                }else if(remaining==3){
                    cout<<" "<<first.second;
                    first.first-=1;
                    seq.push(first);
                    seq.push(second);
                    remaining-=1;
                }else{
                    cout<<" "<<first.second<<first.second;
                    first.first-=2;
                    seq.push(first);
                    seq.push(second);
                    remaining-=2;
                }
            }else{
                if(remaining==2){
                    cout<<" "<<first.second<<second.second;
                    first.first-=1;
                    second.first-=1;
                    seq.push(first);
                    seq.push(second);
                    remaining-=2;
                }else{
                    cout<<" "<<first.second;
                    first.first-=1;
                    seq.push(first);
                    seq.push(second);
                    remaining-=1;
                }
            }
        }
        cout<<endl;

    }
    

    return 0;
}
