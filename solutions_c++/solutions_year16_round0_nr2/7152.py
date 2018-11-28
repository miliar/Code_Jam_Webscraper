#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;
long n, t, seenCount, j = 1;
string s;
void flip(int left, int right){
    for(int i = left; i<=right; i++){
        if(s[i]=='-'){
            s[i]='+';
        }else{
            s[i]='-';
        }
    }
    while(left<right){
        swap(s[left], s[right]);
        left++;
        right--;
    }
}
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin>>t;
    int i = 1;
    while(t--){
        cin>>s;
        int ans=0, r = s.length()-1;
        bool direction = false;
        while(r>=0){

            if(direction){
                int l = 0;
                while(s[l]=='+'){
                    l++;
                }
                if(s[0]=='+') {
                    flip(0, l-1);
                    ans++;
                }
                //cout<<"before: "<<s<<endl;
                flip(0,r);
                //cout<<"after: "<<s<<endl;
                ans++;
                direction= false;
            }else{
                while(r>=0 && s[r]=='+'){
                    r--;
                }
                direction = true;
            }
        }
            cout<<"Case #"<<i++<<": "<<ans<<endl;
    }
    return 0;
}