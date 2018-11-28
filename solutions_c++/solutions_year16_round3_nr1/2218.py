#include <bits/stdc++.h>
using namespace std;
const int MAX = 30;
int a[MAX];
mycomp(const pair<int, char> &a, const pair<int, char> &b){
    return a.first > b.first;
}
void solve(int tc){
    vector<pair<int, char> >v;
    int n;
    scanf("%d", &n);
    int total = 0;
    for(int i = 0; i < n; i++){
        scanf("%d", a+i);
        total+=a[i];
        v.push_back(make_pair(a[i], 'A'+i));
    }
    
    printf("Case #%d:", tc);
    while(total){
        sort(v.begin(), v.end(), mycomp);
        if(v[0].first + v[1].first  == total){
            while(total){
                printf(" %c%c", v[0].second, v[1].second);
                total-=2;
            }
        }else if(v[0].first == 1 && v[1].first == 1 && v[2].first == 1){
            printf(" %c", v[0].second);
            v[0].first = 0;
            total--;
        }else{
            printf(" %c%c", v[0].second, v[1].second);
            total-=2;
            v[0].first--;
            v[1].first--;
        }
    }
    printf("\n");
}

int main(){
    int tt;
    scanf("%d", &tt);
    for(int i = 1; i <= tt; i++)solve(i);
    return 0;
}