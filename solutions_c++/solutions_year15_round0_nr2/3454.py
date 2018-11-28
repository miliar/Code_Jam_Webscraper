#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;
/*
int solve(vector <int>  p, int time){
    bool flag = false;
    bool flag1 = false;
    int max = 0;
    int maxi=-1;
    for(int i=0; i<p.size(); i++){
        if(p[i] > max){
            max = p[i];
            maxi = i;
        }
        if(p[i]!=0)
            flag=true;
        if(p[i]>1)
            flag1 = true;
    }
    if(flag == false){
        return time;
    } else if(flag1==false){
        for(int i=0; i<p.size(); i++){
            if(p[i] > 0){
                p[i]--;
            }
        }
        return solve(p,time+1);

    } else {
        vector <int> p1 = p;
        vector <int> p2 = p;
        //cout << maxi;
        p1[maxi] = (max+2-1)/2;
        p1.push_back(max/2);
        for(int i=0; i<p2.size(); i++){
            if(p2[i] > 0){
                p2[i]--;
            }
        }
        return min(solve(p1,time+1), solve(p2, time+1));

    }

}
*/

int main(){
    int T;
    cin >>T;
    for(int I=0; I<T; I++){
        int D;
        cin >> D;
        vector<int> P;
        int max=-1;
        int maxi;
        for(int J=0; J<D; J++){
            int p;
            cin >> p;
            P.push_back(p);
            if(p>max){
                max=p;
                maxi = J;
            }
        }
        //int time = solve(P,0);
        vector<int> costs;
        costs.push_back(0);
        costs.push_back(1);
        vector <int> pp = P;
        long long int ans = max;
        for(int i=2; i<ans; i++){
            long long int x;
            for(int j=0; j<P.size(); j++){
                x = (P[j]-1)/i;
            }
            
            long long int sum=0;
            for(int j=0; j<P.size(); j++){
                sum+=(P[j]-1)/i;
            }
            P.push_back(i);
            sum+=i;
            ans = min(ans,sum);
        }
        long long int time = ans;
        cout << "Case #" << I+1<<": "<< time << endl;
    }
    
}