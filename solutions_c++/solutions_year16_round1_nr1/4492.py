#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>


using namespace std;

#define all(x) x.begin(),x.end()
// sort(all(vec))
#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container),element) != container.end())
#define tr(container, it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
// tr(set,it)
// total+=it->second;
set<vector<int>> se;




int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    int kase=0;
    while(t--){
        
        string s;
        cin >> s;
        cout << "Case #" << ++kase << ": ";
        vector<string> vec{};
        vector<string> tmp{};
        vec.push_back(s.substr(0,1));
        for(int i=1;i<s.length();i++){
            int sz=vec.size();
            for(int j=0;j<sz;j++){
                string t=vec[j];
                tmp.push_back(t+s[i]);
                tmp.push_back(s[i]+t);
            }
            vec=tmp;
            tmp.clear();
            //for(int i=0;i<vec.size();i++)
            //    cout << vec[i] << " " ;
            //cout << endl;
        }
        sort(vec.begin(),vec.end());
        cout << vec[vec.size()-1] << endl;
        
    }
}
