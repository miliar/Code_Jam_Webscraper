#include <bits/stdc++.h>

using namespace std;

int main()
{ifstream cin("B-large.in") ;
    ofstream cout("out.txt");
    int t ;
    cin >> t ;
    int cp =1 ;

    while(t--){
        cout << "Case #" <<cp++ << ": ";
        int ans = 0;
        string s ;
        cin >> s;
        reverse(s.begin(),s.end());
        vector<bool> v ;
        for(int i = 0 ; i < s.size() ; i++) {
            if(s[i]=='+') v.push_back(true);
            else v.push_back(false);
        }
        //cout << v.size() << endl;
        int j = 0 ;
        while( j<s.size()){
            while(v[j]==1 && j<s.size()) j++ ;
            if(j==s.size()) break;
            if(v.back()==1) {
                    ans++ ;
                int k = s.size()-1 ;
                while(v[k]==1)  v[k--]=0 ;

            }
            ans++ ;
            reverse(v.begin()+j, v.end());
            for(int i=j ; i < s.size() ; i++ ) v[i]=!v[i];

        }
        cout << ans << endl;
    }
    return 0;
}
