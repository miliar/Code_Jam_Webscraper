#include <iostream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

//#define DEBUG

const char *infile = "A-large.in";
const char *outfile = "pa-large.out";

int getans(const string s[], int n) {
    int ans=0;
    int p[n];
    int a[n];
    for (int i=0; i<n; i++) p[i]=0;
    
    while (p[0] < s[0].size()) {
        fill_n(a, n, 0);
        char cur = s[0][p[0]];

#ifdef DEBUG
        cout << "cur=" << cur << endl;
        for (int i=0; i<n; i++)
            cout << p[i] << ' ';
        cout << endl;
#endif

        int i=p[0]+1;
        while (i<s[0].size() && s[0][i] == cur) 
            i++;
        a[0]=i-p[0];
        p[0]=i;
        
        for (int k=1; k<n; k++) {
            if (p[k] >= s[k].size() || s[k][p[k]] != cur) return -1;
            
            i=p[k]+1;
            while (i<s[k].size() && s[k][i] == cur) 
                i++;
            a[k]=i-p[k];
            p[k]=i;
        }
        
        sort(a, a+n);
        int mid = a[n/2];
        for (int k=0; k<n; k++)
            ans += abs(a[k] - mid);
    }
    
    for (int k=1; k<n; k++) {
        assert(p[k]<=s[k].size());
        if (p[k] != s[k].size()) return -1;
    }
    
    return ans;
}

int main() {
    ifstream fin(infile);
    assert(fin);
    ofstream fout(outfile);
    assert(fout);
    
    int test;
    fin >> test;
    for (int count=1; count<=test; count++) {
            
       // cout << "count = " << count << endl;  
            
        int n;
        fin >> n;
        string s[n];
        for (int i=0; i<n; i++)
            fin >> s[i];
    
      //  for (int  i=0; i<n; i++)
        //    cout << s[i] << endl;
        
        int ans=getans(s, n);
        fout << "Case #" << count << ": ";
        if (ans<0) fout << "Fegla Won" << endl;
        else fout << ans << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
