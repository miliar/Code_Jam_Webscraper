#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long ll;

double eps = 1e-7;

int main(){
    int T;
    cin >> T;
    
    cout << setprecision(18);
    
    for(int t=1;t<=T;t++){
        int N;
        double V, X;
        cin >> N >> V >> X;
        
        vector<pair<double, double> > sources(N);
        for(int i=0;i<N;i++){
            double R, C;
            cin >> R >> C;
            sources[i] = make_pair(C, R);
        }
        
        sort(sources.begin(), sources.end());
        
        double totalR = 0.;
        double totalC = 0.;
        for(int i=0;i<N;i++) totalR += sources[i].second;
        for(int i=0;i<N;i++) totalC += sources[i].first*sources[i].second;
        
        double minC = sources[0].first;
        double maxC = sources[N-1].first;
        
        if(X < minC-eps || X > maxC+eps){
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        }else if(abs(X-minC) <= eps || abs(X-maxC) <=eps){
            double curR = 0.;
            for(int i=0;i<N;i++){
                double C = sources[i].first;
                double R = sources[i].second;
                
                if(abs(C - X) <= eps) curR += R;
            }
            
            cout << "Case #" << t << ": " << (V/curR) << endl;
        }else{
        
        
        double allC = totalC/totalR;
        double ans = 0.;
        double cumx = 0.;
        double cumy = 0.;
        if(X < allC){
            for(int i=0;i<N;i++){
                double C = sources[i].first;
                double R = sources[i].second;
                
                cumx += R;
                cumy += C*R;
                
                if(X < cumy/cumx + eps){
                    if(abs(X-C) < eps){
                        ans = V/R;
                        break;
                    }else{
                        double t = (X*cumx - cumy)/((X-C)*R);
                        ans = V/(cumx - R*t);
                        break;
                    }
                }
            }
        }else{
            for(int i=N-1;i>=0;i--){
                double C = sources[i].first;
                double R = sources[i].second;
                
                cumx += R;
                cumy += C*R;
                
                if(X > cumy/cumx - eps){
                    if(abs(X-C) < eps){
                        ans = V/R;
                        break;
                    }else{
                        double t = (X*cumx - cumy)/((X-C)*R);
                        ans = V/(cumx - R*t);
                        break;
                    }
                }
            }
        }
        
        /*
        double low = V/totalR;
        double high = 1e10;
        double tarX = V;
        double tarY = X*V;
        
        while(high - low > max(1e-7, high*1e-7)){
      //      cout << high << " " << low << endl;
            double mid = (high+low)/2;
            
            bool good = true;
            
            //lower envelope
            double cumx = 0.;
            double cumy = 0.;
            for(int i=0;i<N;i++){
                double C = sources[i].first;
                double R = sources[i].second;
                
                double cx = R*mid;
                double cy = C*R*mid;
                
                if((tarY-cumy)*cx + eps < (tarX - cumx)*cy){
                    good = false;
                }
                
                cumx += cx;
                cumy += cy;
            }
            
            // upper envelope
            cumx = 0.;
            cumy = 0.;
            
            for(int i=N-1;i>=0;i--){
                double C = sources[i].first;
                double R = sources[i].second;
                
                double cx = R*mid;
                double cy = C*R*mid;
                
                if((tarY-cumy)*cx - eps > (tarX - cumx)*cy){
                    good = false;
                }
                
                cumx += cx;
                cumy += cy;
            }
            
            if(good) high = mid;
            else low = mid;
        }*/
        
        cout << "Case #" << t << ": " << ans << endl;

        }
    }
    
    return 0;
}