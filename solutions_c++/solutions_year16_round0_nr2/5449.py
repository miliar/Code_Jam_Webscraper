#include<bits/stdc++.h>
using namespace std;
long long x,cnt,ans[101];
string s[101];
bool y;
int main(){
  /*ifstream m;
  m.open ("B-small-attempt0.in");
  ofstream f;
  f.open("output.txt")*/
 cin>>x;
// m>>x;
 for(int i=0;i<x;i++){
    cin>>s[i];
   // m>>s[i];
 }
 for(int i=0;i<x;i++){
        cnt=0;
        y=0;
    for(int j=s[i].size()-1;j>=0;j--){
        if((s[i][j]=='-'&&y==0)||(s[i][j]=='+'&&y==1)){
            cnt++;
            y^=1;
        }
    }
    ans[i]=cnt;
 }
 for(int i=0;i<x;i++)cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
}
