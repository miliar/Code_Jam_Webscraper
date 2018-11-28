#include<bits/stdc++.h>

using namespace std;

long long getDec(){
    int a,b;
    scanf("%d.%d",&a,&b);
    return a*10000+b;
}

void solve_small2(){
    int n;
    long long V,X;
    cin >> n;
    V=getDec();
    X=getDec();
    vector<pair<long long,long long > > v;
    for(int i = 0 ; i < n ; ++ i ){
        long long T,R;

        R=getDec();
        T=getDec();
        v.push_back({T,R});
    }
    if(n==1){
        if(v[0].first!=X){
            cout <<"IMPOSSIBLE"<<endl;
            return ;
        }
        else{
            cout << V*1.0/v[0].second << endl;
            return ;
        }
    }
    else{
        sort(v.begin(),v.end());
        if(v[1].first<X||v[0].first>X){
            cout <<"IMPOSSIBLE"<<endl;
            return ;
        }
        if(v[0].first==X&&v[1].first==X){
            cout << V*1.0/(v[0].second+v[1].second) << endl;
            return ;
        }
        if(v[0].first==X){
            cout << V*1.0/(v[0].second) << endl;
            return ;
        }
        if(v[1].first==X){
            cout << V*1.0/(v[1].second) << endl;
            return ;
        }

        double SUMHEAT= V*X;
        double s1=0,e1=V;
            for(int t = 0 ; t < 200 ; ++ t ){

                double mid = s1+ (e1-s1)/2;
                double heat = mid*v[0].first+ (V-mid)*v[1].first;
                //cout << mid  << " "<< heat << " " << SUMT << endl;

                if(SUMHEAT>heat){
                    e1=mid;
                }
                else{
                    s1=mid;
                }
            }

            cout << max(s1/v[0].second,(V-s1)/v[1].second) << endl;
    }
}

void solve_small(){
    int n;
    double V,X;
    cin >> n >> V >> X;

    vector<pair<double,double> > pipe;
    for(int i = 0 ; i < n ; ++ i ){
        double R,T;
        cin >> R >> T;
        pipe.push_back({T,R});
    }
    if(n==1){
        if(fabs( pipe[0].first- X ) <1e-6){
            cout << V/pipe[0].second << endl;
        }
        else {
            cout <<"IMPOSSIBLE"<<endl;
        }
    }
    else{
        sort(pipe.begin(),pipe.end());
        if(pipe[0].first-X>2e-4||X-pipe[0].first<-2e-4){
            cout <<"IMPOSSIBLE"<<endl;

        }
        else{
            double SUMT=V*X;
            double s1=0,e1=V;
            while( (e1-s1)>1e-18){
                double mid = s1+ (e1-s1)/2;
                double heat = mid*pipe[0].first+ (V-mid)*pipe[1].first;
                //cout << mid  << " "<< heat << " " << SUMT << endl;
                if(fabs( (SUMT)/V- heat/V)<1e-8){
                    cout << max(mid/pipe[0].second,(V-mid)/pipe[1].second) << endl;
                    return ;
                }
                if(SUMT>heat){
                    e1=mid;
                }
                else{
                    s1=mid;
                }
            }
            cout <<"IMPOSSIBLE"<<endl;
        }
    }
}

int main(){
    //freopen("Bsample.txt","r",stdin);
    freopen("B-small-attempt3"".in","r",stdin);
    freopen("B-small-attempt3"".out","w",stdout);
    cout << setprecision(10) << fixed ;
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; ++ i ){
        printf("Case #%d: ",i);
        solve_small2();
    }
}
