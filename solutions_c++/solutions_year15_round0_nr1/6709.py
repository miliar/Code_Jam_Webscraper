#include <bits/stdc++.h>
using namespace std;
int n , cnt , mini ;
string str;
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t , k=1;
    cin >> t;
    while(t--){
        cin >> n ;
        cin >> str;
        cnt = 0;
        mini = 0;
        for(int i=0;i<(int)str.length();i++){
            int x = str[i]-'0';
            if(cnt>=i){
                cnt+=x;
            }else{
                mini+=(abs(i-cnt));
                cnt+=(abs(i-cnt));
                cnt+=x;
            }
        }
        cout << "Case #" << k<< ": " <<mini << endl;
        k++;
    }
    return 0;
}
