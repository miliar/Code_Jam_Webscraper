#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("fileName.in","r",stdin);
    freopen("fileName.out","w",stdout);
    int t , n , people=0 , cnt=0;
    string s ;
    cin >> t ;
    for(int j=0 ; j < t ; j++)
    {
        cin >> n >> s ;
        people += s[0]-48;
        for(int i=1 ;i < s.size() ; i++){
            if(people < i)
                cnt++ , people++ ;
            people += s[i]-48 ;
        }
        cout << "Case #" << j+1 << ": " << cnt << endl ;
        people = 0 , cnt=0;
    }
    return 0;
}
