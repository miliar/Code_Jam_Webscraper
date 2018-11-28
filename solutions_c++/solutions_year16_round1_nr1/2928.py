#include<bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,t1=1; scanf("%d",&t);
    while(t--){
        string s,temp; cin >> s;
        int i,n = s.length();
        string p = "";
        p+= s[0]; int j,m;
        for(i=1;i<n;i++){
            if(s[i]>=p[0]){
                temp = "";
                temp+= s[i];
                m = p.length();
                for(j=0;j<m;j++)
                    temp+= p[j];
                p = temp;
            }
            else
                p+= s[i];
        }
        cout << "Case #" << t1 << ": " << p << endl;
        t1++;
    }
    return 0;
}
