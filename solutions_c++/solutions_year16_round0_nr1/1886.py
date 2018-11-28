#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int T;
    cin >> T;
    int t = 1;
    while(T--){
        int counter = 0;
        int vis[10] = {0};
        long long n;
        cin >> n;
        long long temp = n;
        int acc = 0;
        while(counter < 10 && acc < 1000){
            acc++;
            long long tmp = temp;
            while(tmp){
                if(!vis[tmp%10])vis[tmp%10] = 1 , counter++;
                tmp /= 10;
            }
            temp+=n;
        }
        cout << "Case #"<<t++<<": ";
        if(counter != 10)cout << "INSOMNIA"<<endl;
        else cout << temp-n<<endl;
    }
    return 0;
}
