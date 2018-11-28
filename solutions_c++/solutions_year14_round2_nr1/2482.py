#include<cstdio>
#include<cstring>
#include<map>
#include<set>
using namespace std;

class en{
public:
    int time;
    char c;
    en(char ch, int t){
        c = ch;
        time = t;
    }
    en(){
        c = 0;
        time = 0;
    }
};
int n, ct[105];
map<int, en> str[105];
int T(set<int> tt){
    int l = (tt.size()-1)/2, k=0, ans = 0;
    set<int>::iterator it2 = tt.begin(), it = it2;
    advance(it2, l);
    k = *it2;
    for(; it!=tt.end(); it++){
        ans += (*it>k)? *it-k: k-*it;
    }
    return ans;
}
int main(){

    int t, ca=1, time, ans, num;
    char c, lastc;
    scanf("%d", &t);

    for(; t>0; t--){
        printf("Case #%d: ", ca++);
        scanf("%d%*c", &n);
        bool can = true;
        memset(ct, 0, sizeof(ct));
        for(int i=0; i<n; i++)
            str[i].clear();
        for(int i=0; i<n; i++){
            lastc = time = 0;
            while((c=getchar())!='\n'){
                if(lastc!=c){
                    ct[i]++;
                    if(lastc!=0)
                        str[i].insert(pair<int, en>(ct[i]-1, en(lastc, time)));
                    time = 0;
                }
                time++;
                lastc = c;
            }str[i].insert(pair<int, en>(ct[i], en(lastc, time)));
        }
        num = ct[0];
        for(int i=1; i<n; i++){
            if(ct[i]!=num){
                can = false;
                break;
            }
        }
        ans = 0;
        if(can){
            for(int i=1; i<=num&&can; i++){
                c = (str[0])[i].c;
                set<int> ti;
                ti.insert((str[0])[i].time);
                for(int j=1; j<n; j++){
                    if(c!=(str[j])[i].c){
                        can = false;
                        break;
                    }
                    ti.insert((str[j])[i].time);
                }
                ans += T(ti);
            }
        }
        if(can)
            printf("%d\n", ans);
        else
            puts("Fegla Won");
    }
    return 0;
}
