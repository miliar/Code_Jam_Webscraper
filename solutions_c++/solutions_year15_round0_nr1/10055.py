#include <iostream>

using namespace std;

#define lp(i,a,b) for(i=a;i<b;i++)

int main(){
    ios_base :: sync_with_stdio(0);
    int t;
    cin >> t;
    int m=0;
    while(t--){
        m++;
        string s;
        int n,i,req=0,people=0;
        cin >> n;
        cin >> s;
    //    cout << s << ":";
        people+=(s[0]-'0');
        lp(i,1,n+1){
            if(i>people){
                req = req+(i-people);
                people = i + (s[i]-'0');
            }else{
                people+=(s[i]-'0');
            }
        }
        cout << "Case #" << m << ": " << req << "\n";
    }

    return 0;
}
