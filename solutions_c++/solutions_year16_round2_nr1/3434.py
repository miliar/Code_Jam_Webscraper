#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<ll,ll>
#define f first
#define s second
#define we1(i,n) for(int i=0;i<n;i++)
bool we1234[2011][10];
int main(){
    //freopen("A-small-attempt0.in.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    we1(i,T){
        string s;
        cin >> s;
        int ws[26]={0};
        for(auto x:s){
            ws[x-'A']++;
        }
        int we123[10]={0};
        string we12="";
        while(ws[25]) we12+='0' , we123[0]++ , ws['Z'-'A']-- , ws['E'-'A']-- , ws['R'-'A']-- , ws['O'-'A']--;
        while(ws['U'-'A']) we12+='4' , we123[4]++ , ws['F'-'A']-- , ws['O'-'A']-- , ws['U'-'A']-- , ws['R'-'A']--;
        while(ws['W'-'A']) we12+='2' , we123[2]++ , ws['T'-'A']-- , ws['W'-'A']-- , ws['O'-'A']--;
        while(ws['X'-'A']) we12+='6' , we123[6]++ , ws['S'-'A']-- , ws['I'-'A']-- , ws['X'-'A']--;
        while(ws['G'-'A']) we12+='8' , we123[8]++ , ws['E'-'A']-- , ws['I'-'A']-- , ws['G'-'A']-- , ws['H'-'A']-- , ws['T'-'A']--;
        while(ws['O'-'A']) we12+='1' , ws['O'-'A']-- , ws['N'-'A']-- , ws['E'-'A']--;
        while(ws['T'-'A']) we12+='3' , ws['T'-'A']-- , ws['H'-'A']-- , ws['R'-'A']-- , ws['E'-'A']-=2;
        while(ws['F'-'A']) we12+='5' , ws['F'-'A']-- , ws['I'-'A']-- , ws['V'-'A']-- , ws['E'-'A']--;
        while(ws['I'-'A']) we12+='9' , ws['N'-'A']-- , ws['I'-'A']-- , ws['N'-'A']-- , ws['E'-'A']--;
        while(ws['S'-'A']) we12+='7', ws['S'-'A']-- , ws['E'-'A']-- , ws['V'-'A']-- , ws['E'-'A']-- , ws['N'-'A']--;
 
        sort(we12.begin(),we12.end());
        cout<<"Case #"<<i+1<<": "<<we12<<"\n";
    }
}
