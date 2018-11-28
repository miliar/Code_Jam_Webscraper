#include<stdio.h>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<iostream>

#define MN 1000010
#define INF 100000001
#define pb push_back
#define mp make_pair
#define fr first
#define se second
#define sc scanf
#define pr printf

using namespace std;
int t;
string a, b;
string square(string x){
    string y;
    reverse(x.begin(), x.end());
    for(int i=0; i<x.length(); i++){
        for(int j=0; j<x.length(); j++){
            if(i+j==y.length()){
                y.pb(0);
            }
            y[i+j] += x[i]*x[j];
        }
    }
    int carry = 0;
    for(int i=0; i<y.length() || carry; i++){
        if(i == y.length())y.pb(0);
        y[i] += carry;
        carry = y[i]/10;
        y[i] = y[i]%10;
    }
    return y;
}
bool palindrome(string x){
    string y = x;
    reverse(x.begin(), x.end());
    return (x == y);
}
bool cmp(string x, string y){
        /*cout<<"x, y -> ";
        for(int i=0; i<x.length(); i++){
            cout<<int(x[i]);
        }
        cout<<" ";
        for(int i=0; i<y.length(); i++){
            cout<<int(y[i]);
        }
        cout<<endl;*/
    if(x.length() == y.length())return (x<=y);
    return (x.length() < y.length());
}
char S(int x){
    char s;
    return s;
}
int Ans(int len, string s){
    /*cout<<len<<" ";
    for(int i=0; i<s.length(); i++){
        cout<<int(s[i]);
    }
    cout<<endl;*/
    if(len == 0){
        while(s.length()>0 && s[0] == 0){
            s = s.substr(1, s.length()-1);
        }
        if(s.length() == 0)return 0;
        string s1 = s;
        reverse(s1.begin(), s1.end());
        /*cout<<"s, s1 -> ";
        for(int i=0; i<s.length(); i++){
            cout<<int(s[i]);
        }
        cout<<" ";
        for(int i=0; i<s1.length(); i++){
            cout<<int(s1[i]);
        }
        cout<<endl;*/
        string sq1 = square(s+s1);
        string sq2 = square(s+s1.substr(1, s1.length()-1));
        /*
        for(int i=0; i<sq1.length(); i++){
            cout<<int(sq1[i]);
        }
        cout<<endl;

        for(int i=0; i<sq2.length(); i++){
            cout<<int(sq2[i]);
        }
        cout<<endl;
        cout<<palindrome(sq1)<<endl;
        cout<<palindrome(sq2)<<endl;
        cout<<( palindrome( sq1 )&cmp(a, sq1)&cmp(sq1, b) )<<endl;
        cout<<( palindrome( sq2 )&cmp(a, sq2)&cmp(sq2, b) )<<endl;
        return 0;
        */
        return ( palindrome( sq1 )&cmp(a, sq1)&cmp(sq1, b) ) + ( palindrome( sq2 )&cmp(a, sq2)&cmp(sq2, b) );
    }
    int ans = 0;
    for(char i=0; i<3; i++){
        //pr("%d\n", i);
        ans += Ans(len-1, s+i);
    }
    //cout<<"ans->"<<ans<<endl;
    return ans;
}
void Init(){
    sc("%d", &t);
    for(int k=1; k<=t; k++){
        cin>>a>>b;
        cout<<"Case #"<<k<<": ";
        //cout<<a<<" "<<b<<endl;
        for(int i=0; i<a.length(); i++){
            a[i] -= 48;
        }
        for(int i=0; i<b.length(); i++){
            b[i] -= 48;
        }
        char tmp = 9;
        string tmp1;
        tmp1 += tmp;
        pr("%d\n", (cmp(a, tmp1)&cmp(tmp1, b)) + Ans(((b.length()+1)/2+1)/2, ""));
    }
    /*
    for(int i=1; i<=MN; i++){
        if(palindrome(i) && palindrome(1LL*i*i)){
            pr("%d %lld\n", i, 1LL*i*i);
        }
    }*/
}
main(){
    freopen("input.txt", "r", stdin);    freopen("output.txt", "w", stdout);
    //freopen("C.dat", "r", stdin);    freopen("C.sol", "w", stdout);
    Init();
    //cout<<cmp("113", "212")<<endl;
    return 0;
}
