#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <stack>
#define test int t; cin >> t;while(t--)
typedef unsigned long long ll;

using namespace std;

int MOD=1e9+7;

int main(){
	freopen("codejamrevengein.txt","r",stdin);
		freopen("codejamrevengeout.txt","w",stdout);

    int tt=1;
    test{
        cout << "Case #" << tt << ": ";
        tt++;
        char s[101];
        scanf("%s",s);
        int l=strlen(s);

        int in=-1;

        int ans=0;
        for(int i=0;i<l;i++){
            if(s[i]=='-')in=i;
        }

      //  cout << in << " ";
        if(in==0){
            cout << "1\n";
        }
        else if(in==-1)cout << "0\n";
        else{
            int aa=0; char prev=s[0];

            if(s[0]=='+')aa=1;

            for(int i=1;i<in;i++){
                if(s[i]=='+' && s[i]!=prev){
                    aa+=1;
                }
                prev=s[i];
            }

       //     cout << aa << " ";
            ans=2*aa + 1;
            if(s[0]=='+')ans-=1;
            cout << ans << "\n";
        }
    }
}
