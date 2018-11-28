//
//  pb.cpp
//  
//
//  Created by 宋元堯 on 2016/4/9.
//
//

#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;
    for(int i = 1; i <= n; ++i){
        int ans = 0;
        string s;
        cin >> s;
        char tmp = s[0];
        if(s[0] == '-') ans += 1;
        for(int j = 1; j < s.size(); ++j){
            if(tmp != '-' && s[j] == '-'){
                ans += 2;
            }
            tmp = s[j];
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
