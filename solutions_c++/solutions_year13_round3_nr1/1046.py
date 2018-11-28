#include <iostream>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

bool f(char c){
    if ((c == 'a')||(c == 'e')||(c == 'i')
    || (c == 'o')||(c == 'u'))return true;
    else
        return false;
};

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    int n;
    for (int o_O=0;o_O<t;o_O++){
        cout << "Case #" << o_O+1 << ": ";
        string s;
        cin >> s;
        cin >> n;
        long long ans = 0;
        vector <int> a,b;
        a.assign(s.length(),0);
        b.assign(s.length(),-1);
        if (!(f(s[0])))
            a[0]=1;
        for (int i=0;i<s.length();i++){
            if ((!(f(s[i]))) &&(i!=0))
                a[i]=a[i-1]+1;
            if (a[i] >= n){
                for (int j=i-n+1;j>=0;j--){
                    if (b[j] == -1)
                        b[j] = i;
                    else
                        break;
                }
            }
        }
        for (int i=0;i<s.length();i++){
            if (b[i] != -1)
                ans += s.length()-b[i];
        }
        cout << ans << endl;
    }
    return 0;
}
