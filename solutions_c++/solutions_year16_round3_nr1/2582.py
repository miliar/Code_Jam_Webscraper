#include <bits/stdc++.h>

using namespace std;
priority_queue<pair<int, int> > q;
bool check(){
    pair<int, int> h = q.top();
    q.pop();
    if(q.size()>0 && q.top().first == 1){
        q.push(h);
        return false;
    }
    q.push(h);
    return true;

}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cases = 1;
    cin>>t;
    while(t--){
        while(!q.empty())q.pop();
        int n, x, temp, sum = 0;
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>temp;
            sum+=temp;
            q.push({temp, i});
        }
        printf("Case #%d: ", cases++);
        while(!q.empty()) {
            pair<int, int> a = q.top();
            q.pop();
            if(a.first>=2){
                if((q.top().first+0.0) / (sum-2.0) <= 0.5){
                    printf("%c%c ", 'A' + a.second, 'A' + a.second);
                    if(a.first-2>0)
                        q.push({a.first - 2, a.second});
                    sum-=2;
                }
                else if(sum==2 ||((q.top().first-1.0) / (sum-2.0) <= 0.5 && (a.first-1.0) / (sum-2.0) <= 0.5  && check())){
                    pair<int, int> hamada = q.top();
                    printf("%c%c ", 'A' + a.second, 'A' + hamada.second);
                    q.pop();
                    if(hamada.first>1)q.push({hamada.first-1, hamada.second});
                    if(a.first>1)q.push({a.first-1, a.second});
                    sum-=2;
                }
                else {
                    printf("%c ", 'A' + a.second);
                    if(a.first>1)q.push({a.first-1, a.second});
                    sum--;
                }
            }
            else {
                if(sum==2 || ((q.top().first-1.0) / (sum-2.0) <= 0.5 && (a.first-1.0) / (sum-2.0) <= 0.5  && check())){
                    pair<int, int> hamada = q.top();
                    printf("%c%c ", 'A' + a.second, 'A' + hamada.second);
                    q.pop();
                    if(hamada.first>1)q.push({hamada.first-1, hamada.second});
                    if(a.first>1)q.push({a.first-1, a.second});
                    sum-=2;
                }
                else {
                    printf("%c ", 'A' + a.second);
                    if(a.first>1)q.push({a.first-1, a.second});
                    sum--;
                }
            }
        }
        printf("\n");
    }
    return 0;
}
