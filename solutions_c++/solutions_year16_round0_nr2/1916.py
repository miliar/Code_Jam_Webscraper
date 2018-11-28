#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main(){
    int T; scanf("%d", &T);
    for(int ti=1;ti<=T;ti++){
        fprintf(stderr, "start processing testcase %d\n", ti);
        printf("Case #%d: ", ti);
        string s; cin >> s;
        char c = s[0];
        int cnt = 0;
        for(int i=0;i<s.size();i++){
            if(s[i] != c){
                cnt ++;
                c = s[i];
            }
        }
        printf("%d\n", cnt + (s[s.size()-1]=='-'));
        fprintf(stderr, "completed processing testcase %d\n", ti);
    }
}
