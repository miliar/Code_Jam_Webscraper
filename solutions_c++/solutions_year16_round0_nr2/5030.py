#include<iostream>
using namespace std;
void flip(int pancakes[], int i){
    int j;
    for(j = 0; j <= i; j++)
        if(pancakes[j])
            pancakes[j] = 0;
        else
            pancakes[j] = 1;
    for(j = 0; j <= i / 2; j++)
        swap(pancakes[i - j], pancakes[j]);
}

int main(){
    int T, N, i, j, cases, ans;
    string S;
    cin>>T;
    cases = 1;
    while(cases <= T){
        ans = 0;
        cin>>S;
        N = S.length();
        int pancakes[N];
        for(i = 0; i < N; i++)
            if(S[i] == '+')
                pancakes[i] = 1;
            else
                pancakes[i] = 0;
        for(i = N - 1; i >= 0; i--)
            if(!pancakes[i]){
                for(j = 0; j < i; j++)
                    if(!pancakes[j])
                        break;
                if(j > 0){
                    flip(pancakes, j - 1);
                    ans++;
                }
                flip(pancakes, i);
                ans++;
            }
        cout<<"Case #"<<cases++<<": "<<ans<<endl;
    }
    return 0;
}
