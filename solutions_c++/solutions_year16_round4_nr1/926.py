#include <iostream>
#include <cstring>
#include <queue>
#include <cstdio>
using namespace std;

int main(){
    
    freopen("/Users/clsrn1581/Desktop/xcode/practice/practice/input.txt","r",stdin);
    freopen("/Users/clsrn1581/Desktop/xcode/practice/practice/output.txt","w",stdout);
    
    int testcase;
    scanf("%d",&testcase);
    
    int R,P,S,N;
    for(int t=1;t<=testcase;t++){
        
        scanf("%d%d%d%d",&N,&R,&P,&S);
        pair<string, int> p[2][3];
        
        p[0][0].first = "P";
        p[0][0].second = P;
        p[0][1].first = "R";
        p[0][1].second = R;
        p[0][2].first = "S";
        p[0][2].second = S;
        
        int q = 0;
        
        bool cc = 0;
        
        while(1){
            p[!q][0].first = p[q][0].first + p[q][1].first;
            p[!q][1].first = p[q][0].first + p[q][2].first;
            p[!q][2].first = p[q][1].first + p[q][2].first;
            
            int k = p[q][0].second + p[q][1].second - p[q][2].second;
            if(p[q][0].second < k/2 || p[q][1].second < k/2 || k < 0){
                cc = 1;
                break;
            }
            p[!q][0].second = k/2;
            p[!q][1].second = p[q][0].second - (k/2);
            p[!q][2].second = p[q][2].second -  p[!q][1].second;
            
            q = !q;
            if(p[q][0].second + p[q][1].second + p[q][2].second == 1) break;
        }
        string ans;
        if(cc){
            ans = "IMPOSSIBLE";
        } else {
            for(int i=0;i<3;i++){
                if(p[q][i].second == 1) {
                    ans = p[q][i].first;
                    break;
                }
            }
        }
        
        printf("Case #%d: %s\n",t,ans.c_str());
        
    }
    
    return 0;
}