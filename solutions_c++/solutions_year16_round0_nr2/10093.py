#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <queue>
#include <math.h>
using namespace std;
char temp[101],enter;
bool ck[1025];
int depth[1025];
int T=0;
queue<string> Q;

int strtoi(string a){
    int num=0;
    int len = (int)a.length();
    for (int i=0; i<len; i++) {
        if (a[i] == '+') {
            num += (int)pow(2, len-1-i);
        }
    }
    return num;
}
bool isPlus(string a){
    int len = (int)a.length();
    for (int i = 0; i<len; i++) {
        if (a[i] == '-') {
            return false;
        }
    }
    return true;
}

int main(){
    
    FILE * ifp = fopen("/Users/KHJ/Desktop/codejam/B/B-small-attempt0.in", "r");
    FILE * ofp = fopen("/Users/KHJ/Desktop/codejam/B/B-small-attempt0.out", "w");

    
    int t;fscanf(ifp,"%d",&t);
    
    while (t--) {
        
        fscanf(ifp,"%s",temp);
        //fscanf(ifp,"%c", &enter);
        fprintf(ofp, "Case #%d: ", ++T);
        
        string cake = (string)temp;
        int cake_num = strtoi(cake);
        
        ck[cake_num] = true;
        Q.push(cake);
        
        int ans=0;
        
        while (!Q.empty()) {
            string now = Q.front();Q.pop();
            int now_num = strtoi(now);
            if (isPlus(now)) {
                ans = depth[now_num];
                break;
            }
            
            int len = (int)now.length();
            for (int i=0; i<len; i++) {
                string sub;
                for (int j=0; j<=i; j++) {
                    if (now[i-j] == '+') {
                        sub += '-';
                    }else{
                        sub += '+';
                    }
                    
                }
                for (int j=i+1; j<len;j++ ) {
                    sub += now[j];
                }
                int sub_num = strtoi(sub);
                
                //printf("sub_num : %d  sub_len : %d\n",sub_num,(int)sub.length());
                
                if (!ck[sub_num]) {
                    ck[sub_num] = true;
                    depth[sub_num] = depth[now_num] + 1;
                    Q.push(sub);
                }
                
            }
            
            
        }
        fprintf(ofp,"%d\n",ans);
        while (!Q.empty()) {
            Q.pop();
        }
        for (int i=0; i<1025; i++) {
            ck[i] = false;
            depth[i] = 0;
        }
        
        
    }
    
    return 0;
}