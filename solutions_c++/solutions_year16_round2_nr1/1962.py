#include <iostream>
#include <map>
#include <cstring>
using namespace std;

map<char,int> A;
int ans[10];
int main(){
    freopen("readable.txt","w",stdout);
    int t; cin>>t;
    for (int ca=1;ca<=t;ca++){
        memset(ans,0,sizeof ans);
        A.clear();
        string s; cin>>s;
        for (int i=0;i<s.size();i++) A[s[i]]++;
        //zero=z, two=w, six=x, eight=g, three=h, seven=s, five=v, four= f, one=o, nine=e
        ans[0]+=A['Z']; A['E']-=A['Z']; A['R']-=A['Z']; A['O']-=A['Z']; A['Z']=0;
        ans[2]+=A['W']; A['T']-=A['W']; A['O']-=A['W']; A['W']=0;
        ans[6]+=A['X']; A['S']-=A['X']; A['I']-=A['X']; A['X']=0;
        ans[8]+=A['G']; A['E']-=A['G']; A['I']-=A['G']; A['H']-=A['G']; A['T']-=A['G']; A['G']=0;
        ans[3]+=A['H']; A['T']-=A['H']; A['R']-=A['H']; A['E']-=A['H']; A['E']-=A['H']; A['H']=0;
        ans[7]+=A['S']; A['V']-=A['S']; A['E']-=A['S']; A['E']-=A['S']; A['S']=0;
        ans[5]+=A['V']; A['F']-=A['V']; A['I']-=A['V']; A['E']-=A['V']; A['V']=0;
        ans[4]+=A['F']; A['O']-=A['F']; A['U']-=A['F']; A['R']-=A['F']; A['F']=0;
        ans[1]+=A['O']; A['N']-=A['O']; A['E']-=A['O']; A['O']=0;
        ans[9]+=A['E'];
        cout<<"Case #"<<ca<<": ";
        for (int i=0;i<=9;i++){
            for (int j=0;j<ans[i];j++) cout<<i;
        }
        cout<<endl;
    }
}