#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <iomanip>
#include <fstream>
#include <iomanip>

using namespace std;

string trm(string t)
{
    string ans="";
    for(int i=0;i<t.size();){
        char s=t[i];
        ans+=t[i];
        while (i<t.size()&&s==t[i]){
            i++;
        }
    }
    return ans;
}
string s[200];

int main()
{
    ofstream myfile;;
    myfile.open("vats.txt");
    int test;
    cin>>test;
    int cc=1;
    while (test--){
        int n;
        cin>>n;
        for (int i=0;i<n;i++){
            cin>>s[i];
        }
        string t=trm(s[0]);
        int c=0;
        for (int i=0;i<n;i++){
            if (t==trm(s[i])){

            } else {
                myfile<<"Case #"<< cc <<": ";
                cc++;
                myfile<<"Fegla Won\n";
                c=1;
            }
        }
        if (c==1){
            continue;;
        }
        //cout<<t<<"\n";
        vector<int> h[300];
        for (int i=0;i<n;i++){
            int l=0;
            int prev=0;
            for (int j=0;j<t.size();j++){
                prev=l;
                while (l<s[i].size() && t[j]==s[i][l]){
                    l++;
                }
               // cout<<l<<" "<<prev<<"\n";
                h[i].push_back(l-prev);
            }
        }
        int ans=0;
        int sz=t.size();
        for (int j=0;j<t.size();j++){
            vector<int> temp;
            for (int i=0;i<n;i++){
                temp.push_back(h[i][j]);
            }
            sort (temp.begin(), temp.end());
            int g=temp[n/2];
            int an=0;
            for (int i=0;i<n;i++){
                an+=abs(g-temp[i]);
            }
            ans+=an;
        }
        //cout<<"Case #"<< cc <<": ";
        myfile<<"Case #"<< cc <<": ";
        cc++;
        //cout<<ans<<"\n";
        myfile<<ans<<"\n";
    }
    return 0;
}
