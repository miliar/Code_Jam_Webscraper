#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    
    for(int i=1; i <= t; ++i)
    {
        int n;
        cin>>n;
        n += 2;
        string s;
        cin >> s;
        vector<int> psum(n);
        int sol = 0;
        for(int i1=1; i1 < n; ++i1)
        {
            int tp = 0;
            psum[i1] = psum[i1-1] + (s[i1-1]-'0'); 
            
            if( psum[i1] < i1)
                {
                sol += i1 - psum[i1];
                psum[i1] = i1; 
            }           
        }

        cout<<"Case #"<<i<<": "<<sol<<endl;
    }
    return 0;
}

