#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    ifstream cin("input.in");
    ofstream cout("output.out");
    int t;
    cin >> t;
    for(int a = 0;a<t;a++){
        int n;
        string s;
        cin >> n >> s;
        int sum = 0;
        int ans = 0;
        for(int i = 0;i<=n;i++){
            int num = s[i]-'0';
            if(sum<i){
                ans += i-sum;
                sum = i;
            }
            sum += num;
        }
        cout << "Case #"<< a+1 << ": "<< ans << "\n";
    }
    return 0;
}
