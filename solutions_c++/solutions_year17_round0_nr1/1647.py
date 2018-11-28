#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream cin("A-large (3).in");
    ofstream cout("out.txt");
    int t ;
    cin >> t ;
    for(int tc=1 ;  tc<=t; tc++){
        string s;
        int n ;
        cin >> s >> n ;
        int ans = 0 ;
        for(int i = 0 ; i<= s.size()-n ; i++){
            if(s[i]=='-'){
                ans++;
                for(int j = i ; j <i+n ; j++){
                    if(s[j]=='+')s[j]='-';
                    else s[j]='+';
                }
            }
        }

        bool ansexist=1;
        for(int i = s.size()-n ; i<s.size() ; i++)
            if(s[i]=='-')ansexist=0;
        cout << "Case #" << tc << ": ";
        if(!ansexist)cout<<"IMPOSSIBLE\n";
        else cout <<ans<<endl;
    }
}
