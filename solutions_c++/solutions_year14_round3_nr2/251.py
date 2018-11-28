#include <iostream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

//#define Debug

typedef long long bigint;

const bigint mod = 1000000007;

bigint jiechen(int n) {
    if (n==0) return 1;
    
    bigint res=1;
    for (int i=1; i<=n; i++)
        res = res * i % mod;
    return res;
}

bigint getAns(int n, string s[]) {
    vector<int> g[26];
    for (int i=0; i<26; i++)
        g[i].assign(26, 0);
        
    vector<int> midcount(26, 0);
    assert(midcount.size() == 26);
    
    for (int i=0; i<n; i++) {
        char c1=s[i][0];
        
        assert(c1-'a' < 26);
        
        //if (midcount[c1-'a']>0) return 0;
        
        int j=0;
        while (j<s[i].size() && s[i][j]==c1) j++;
        
        if (j==s[i].size()) {
            g[c1-'a'][c1-'a']++;
            continue;
        }
        
        char c2=s[i][s[i].size()-1];
        if (c1==c2) return 0;
        
        int k=s[i].size()-1;
        while (k>0 && s[i][k]==c2) k--;
        
        for (int r=j; r<=k; r++) {
            if (r>0 && s[i][r-1]!=s[i][r]) {
                int index=s[i][r]-'a';
                midcount[index]++;
                if (midcount[index]>1) return 0;
                
                for (int p=0; p<n; p++) 
                    if (s[p][0]==s[i][r] || s[p][s[p].size()-1]==s[i][r]) return 0;
            }
        }
        
        g[c1-'a'][c2-'a']++;
    
    }
    vector<int> outcount(26, 0);
    vector<int> incount(26, 0);
    for (int i=0; i<26; i++) {
        for (int j=0; j<26; j++) {
            if (i!=j) {
                outcount[i]+=g[i][j];
                incount[j]+=g[i][j];
            }
        }
    }
    
    for (int i=0; i<26; i++)
        if (incount[i]>1 || outcount[i]>1) return 0;
    
    bigint ans=1;
    int compoent=0;
    vector<bool> vis(26, false);
    
    for (int i=0; i<26; i++)
        if (incount[i]==0 &&  outcount[i]==0 && g[i][i]==0)
            vis[i]=true;
    
    for (int i=0; i<26; i++) {
        if (!vis[i] && incount[i]==0) {
            //vis[i]=true;
            compoent++;
            int j=i;
            do {
                vis[j]=true;
                ans = ans * jiechen(g[j][j]) % mod;
                
                if (outcount[j]==0) break;
                
                int k=0;
                while (k<26 && (k==j || !g[j][k])) 
                    k++;
                
                assert(k<26);
                
                j=k;    
                
            } while (true);
        }
    }
    
    for (int i=0; i<26; i++) 
        if (!vis[i]) return 0;
    
    ans = ans * jiechen(compoent) % mod;
    
    return ans;
}

int main() {
    ifstream fin("B-large.in");
    assert(fin);
    ofstream fout("pb-large.out");
    assert(fout);
    
    int test;
    fin >> test;
    for (int count=1; count<=test; count++) {
        int n;
        fin >> n;
        string s[n];
        for (int i=0; i<n; i++) 
            fin >> s[i];
            
    #ifdef Debug
        for (int i=0; i<n; i++)
            cout << s[i] << " ";
        cout << endl;
    #endif
        
        fout << "Case #" << count << ": " << getAns(n, s) << endl;
    }
    
    fin.close();
    fout.close();
    return 0;
}

