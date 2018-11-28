#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int c = 1;
    while(t--){
        string s;
        cin>>s;
        int n = s.length();
        vector<int>v;
        int i;
        int freq[26];
        for(i = 0; i < 26; i++){
            freq[i] = 0;
        }
        for(i = 0; i < n; i++){
            freq[s[i]-'A']++;
        }
        if(freq['Z' - 'A'] > 0){
            while(freq['Z' - 'A'] > 0){
                freq['Z' - 'A']--;
                freq['E' - 'A']--;
                freq['R' - 'A']--;
                freq['O' - 'A']--;
                v.push_back(0);
            }
        }
        if(freq['W' - 'A'] > 0){
            while(freq['W' - 'A'] > 0){
                freq['T' - 'A']--;
                freq['W' - 'A']--;
                //freq['R' - 'A']--;
                freq['O' - 'A']--;
                v.push_back(2);
            }
        }
        if(freq['U' - 'A'] > 0){
            while(freq['U' - 'A'] > 0){
                freq['F' - 'A']--;
                freq['O' - 'A']--;
                freq['U' - 'A']--;
                freq['R' - 'A']--;
                v.push_back(4);
            }
        }
        if(freq['X' - 'A'] > 0){
            while(freq['X' - 'A'] > 0){
                freq['S' - 'A']--;
                freq['I' - 'A']--;
                //freq['R' - 'A']--;
                freq['X' - 'A']--;
                v.push_back(6);
            }
        }
        if(freq['S' - 'A'] > 0){
            while(freq['S' - 'A'] > 0){
                freq['S' - 'A']--;
                freq['E' - 'A']--;
                freq['V' - 'A']--;
                freq['E' - 'A']--;
                freq['N' - 'A']--;
                v.push_back(7);
            }
        }
        if(freq['F' - 'A'] > 0){
            while(freq['F' - 'A'] > 0){
                freq['F' - 'A']--;
                freq['I' - 'A']--;
                freq['V' - 'A']--;
                freq['E' - 'A']--;
                //freq['N' - 'A']--;
                v.push_back(5);
            }
        }
        if(freq['G' - 'A'] > 0){
            while(freq['G' - 'A'] > 0){
                freq['E' - 'A']--;
                freq['I' - 'A']--;
                freq['G' - 'A']--;
                freq['H' - 'A']--;
                freq['T' - 'A']--;
                v.push_back(8);
            }
        }
        if(freq['O' - 'A'] > 0){
            while(freq['O' - 'A'] > 0){
                freq['O' - 'A']--;
                freq['N' - 'A']--;
                freq['E' - 'A']--;
                //freq['E' - 'A']--;
                //freq['N' - 'A']--;
                v.push_back(1);
            }
        }
        if(freq['H' - 'A'] > 0){
            while(freq['H' - 'A'] > 0){
                freq['T' - 'A']--;
                freq['H' - 'A']--;
                freq['R' - 'A']--;
                freq['E' - 'A']--;
                freq['E' - 'A']--;
                v.push_back(3);
            }
        }
        if(freq['I' - 'A'] > 0){
            while(freq['I' - 'A'] > 0){
                freq['N' - 'A']--;
                freq['I' - 'A']--;
                freq['N' - 'A']--;
                freq['E' - 'A']--;
                //freq['N' - 'A']--;
                v.push_back(9);
            }
        }

        sort(v.begin(),v.end());
        cout<<"Case #"<<c<<": ";
        for(i = 0; i < v.size(); i++){
            cout<<v[i];
        }
        cout<<"\n";
        c++;
    }
    return 0;
}
