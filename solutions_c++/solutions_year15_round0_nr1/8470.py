#include<iostream>
using namespace std;
int main()
{
    int t,cnt,j,all;
    string s;
    cin>>t;
    for (int i=1; i<=t; i++) {
        cin>>j>>s;
        cnt=j=all=0;
        while (j<s.length()) {
            if (all<j) {
                cnt++;
                all++;
            }
            all+=(int)s[j]-48;
            j++;
        }
        cout<<"Case #"<<i<<": "<<cnt<<endl;
    }
}