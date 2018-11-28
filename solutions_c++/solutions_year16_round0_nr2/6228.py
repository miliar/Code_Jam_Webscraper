#include <bits/stdc++.h>

using namespace std;

void solvre(){
    bool flag[1100];
    int n;
    bool ant;
    char ch;
    int ans;

    n = 0;

    while(scanf("%c", &ch)!=EOF && ch!='\n'){
        flag[n++] = ch == '+';
    }

    ant = true;
    ans = 0;
    for(int i = n-1; i>=0; i--){
        if(ant!=flag[i]){
            ant = flag[i];
            ans++;
        }
    }
    printf("%d\n", ans);

}

int main(){
    int x;
    int n;
    char ch;

    cin>>n;
    while(scanf("%c", &ch)!=EOF && ch!='\n');
    for(int i = 1; i<=n; i++){
        cout<<"Case #"<<i<<": ";
        solvre();
    }


}
