#include<iostream>
#include<string>
#include<vector>
using namespace std;

//if Z, get all zeroes first
//if W, get all twos
//if X, get all six
//if G, get all eight
//if U, get all four

//now ONE, THREE, FIVE, SEVEN, NINE

//if S, get all seven
//if R, get all three

//now ONE, FIVE, NINE

//if V, get all five
//if O, get all one
//if N, get all nine


int main(){
    int t; cin>>t;
    for(int T=0;T<t;T++){
        string s; cin>>s;
        int a[26]={0};
        int ans[10] = {0};

        for(int i=0;i<s.size();i++){
            a[s[i]-65]++;
        }

        if(a['Z'-65]>0){
            int diff=a['Z'-65];
            a['Z'-65]-=diff;
            a['E'-65]-=diff;
            a['R'-65]-=diff;
            a['O'-65]-=diff;
            ans[0]+=diff;
        }

        if(a['W'-65]>0){
            int diff=a['W'-65];
            a['T'-65]-=diff;
            a['W'-65]-=diff;
            a['O'-65]-=diff;
            ans[2]+=diff;
        }

        if(a['X'-65]>0){
            int diff=a['X'-65];
            a['S'-65]-=diff;
            a['I'-65]-=diff;
            a['X'-65]-=diff;
            ans[6]+=diff;
        }

        if(a['G'-65]>0){
            int diff=a['G'-65];
            a['E'-65]-=diff;
            a['I'-65]-=diff;
            a['G'-65]-=diff;
            a['H'-65]-=diff;
            a['T'-65]-=diff;
            ans[8]+=diff;
        }
        
        if(a['U'-65]>0){
            int diff=a['U'-65];
            a['F'-65]-=diff;
            a['O'-65]-=diff;
            a['U'-65]-=diff;
            a['R'-65]-=diff;
            ans[4]+=diff;
        }

        if(a['S'-65]>0){
            int diff=a['S'-65];
            a['S'-65]-=diff;
            a['E'-65]-=diff;
            a['V'-65]-=diff;
            a['E'-65]-=diff;
            a['N'-65]-=diff;
            ans[7]+=diff;
        }

        if(a['R'-65]>0){
            int diff=a['R'-65];
            a['T'-65]-=diff;
            a['H'-65]-=diff;
            a['R'-65]-=diff;
            a['E'-65]-=diff;
            a['E'-65]-=diff;
            ans[3]+=diff;
        }

        if(a['V'-65]>0){
            int diff=a['V'-65];
            a['F'-65]-=diff;
            a['I'-65]-=diff;
            a['V'-65]-=diff;
            a['E'-65]-=diff;
            ans[5]+=diff;
        }
        
        if(a['O'-65]>0){
            int diff=a['O'-65];
            a['O'-65]-=diff;
            a['N'-65]-=diff;
            a['E'-65]-=diff;
            ans[1]+=diff;
        }

        if(a['I'-65]>0){
            int diff=a['I'-65];
            a['N'-65]-=diff;
            a['I'-65]-=diff;
            a['N'-65]-=diff;
            a['E'-65]-=diff;
            ans[9]+=diff;
        }

        cout << "Case #" << T+1 << ": ";

        for(int i=0;i<10;i++){
            for(int j=0;j<ans[i];j++){
                cout << i;
            }
        }

        cout << endl;
    }
}
