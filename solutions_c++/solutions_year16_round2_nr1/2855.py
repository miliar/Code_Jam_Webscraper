#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("INP.txt","r+",stdin);
    freopen("ANS.txt","w+",stdout);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++){
        string s;
        cin>>s;
        vector<int>v;
        int a[26];
        memset(a,0,sizeof(a));
        for(int i=0;i<s.length();i++)    a[s[i]-'A']++;
        int num=s.length();

            while(a[25]){
                v.push_back(0);
                a[25]--;
                a['E'-'A']--;
                a['R'-'A']--;
                a['O'-'A']--;
            }
            while(a['W'-'A']){
                v.push_back(2);
                a['W'-'A']--;
                a['T'-'A']--;
                a['O'-'A']--;
            }
            while(a['U'-'A']){
                v.push_back(4);
                a['F'-'A']--;
                a['O'-'A']--;
                a['U'-'A']--;
                a['R'-'A']--;
            }
            while(a['X'-'A']){
                v.push_back(6);
                a['S'-'A']--;
                a['I'-'A']--;
                a['X'-'A']--;
            }
            while(a['R'-'A']){
                v.push_back(3);
                a['T'-'A']--;
                a['H'-'A']--;
                a['R'-'A']--;
                a['E'-'A']-=2;
            }
            while(a['T'-'A']){
                v.push_back(8);
                a['E'-'A']--;
                a['I'-'A']--;
                a['G'-'A']--;
                a['H'-'A']--;
                a['T'-'A']--;
            }
            while(a['S'-'A']){
                v.push_back(7);
                a['S'-'A']--;
                a['E'-'A']-=2;
                a['V'-'A']--;
                a['N'-'A']--;
            }
            while(a['O'-'A']){
                v.push_back(1);
                a['O'-'A']--;
                a['N'-'A']--;
                a['E'-'A']--;
            }
            while(a['N'-'A']){
                v.push_back(9);
                a['N'-'A']-=2;
                a['I'-'A']--;
                a['E'-'A']--;
            }
            while(a['V'-'A']){
                v.push_back(5);
                a['F'-'A']--;
                a['I'-'A']--;
                a['V'-'A']--;
                a['E'-'A']--;
            }
        sort(v.begin(),v.end());
        cout<<"Case #"<<j<<": ";
        for(int i=0;i<v.size();i++)cout<<v[i];cout<<endl;

    }
    return 0;
}
