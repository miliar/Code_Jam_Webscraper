#include<iostream>
#include<map>
#include<fstream>
#include<iomanip>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main() {

    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for (int cas=1;cas<=t;cas++) {

        int n;
        string s;
        cin>>n>>s;
        int total[n+1];
        int num[n+1];
        memset(num,0,sizeof(num));
        memset(total,0,sizeof(total));
        int answer=0;
        for (int i=0;i<s.length();i++) {
            num[i]=s[i]-'0';
            if (i>0) total[i]=total[i-1]+num[i-1];else total[i]=0;
            if (i-total[i]>answer) answer=i-total[i];
        }
        cout<<"Case #"<<cas<<": "<<answer<<endl;
    }
    return 0;
}
