#include<iostream>
#include<string>
#include<bits/stdc++.h>

using namespace std;

char a[8][8] = {
                        {0, 1, 2, 3, 4, 5, 6, 7},
                        {1, 4, 3, 6, 5, 0, 7, 2},
                        {2, 7, 4, 1, 6, 3, 0, 5},
                        {3, 2, 5, 4, 7, 6, 1, 0},
                        {4, 5, 6, 7, 0, 1, 2, 3},
                        {5, 0, 7, 2, 1, 4, 3, 6},
                        {6, 3, 0, 5, 2, 7, 4, 1},
                        {7, 6, 1, 0, 3, 2, 5, 4}
};

int main(){
   freopen("input.txt", "r" , stdin );
   freopen("output.txt", "w" , stdout );
    int t;
    cin>>t;
    int r = 0;
    while(t--){
        int l, x, flag1 = 0 ,flag2 =0, flag3 =0;
        string s , s2;
        cin>>l>>x>>s;
        int i, j = 0;
        r++;
        for( i = 0; i < l; i++){
            if( s[i] == 'i')
                s[i] = 1;
            else if(s[i] == 'j')
                s[i] = 2;
            else
                s[i] = 3;
        }
        for( i = 0; i < x; i++)
            s2 = s2 + s;
        int v = 0;
        for( i = 0 ; i < (l*x) - 2 ; i++){
            v = a[v][s2[i]];
            if( v == 1 ){
                flag1 = 1;
                break;
            }
        }
        v = 0;
        for( i = i + 1 ; i < (l*x) - 1 ; i++){
            v = a[v][s2[i]];
            if( v == 2){
                flag2 = 1;
                break;
            }
        }
        v = 0;
        for( i = i + 1 ; i < (l*x) ; i++){
            v = a[v][s2[i]];
        }
        if( v == 3)
        {
            flag3 = 1;
        }
        if(flag1 == 1 && flag2 == 1 && flag3 == 1)
            cout<<"Case #"<<r<<": "<<"YES\n";
        else
            cout<<"Case #"<<r<<": "<<"NO\n";
    }
    return 0;
}
