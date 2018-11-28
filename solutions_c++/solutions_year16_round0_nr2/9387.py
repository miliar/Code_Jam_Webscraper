#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
int n;
string s;
int ans;
int main(){
    ifstream fin("B.in");
    ofstream fout("B.out");
    int i,j,t;
    cin>>t;
//    fin>>t;
    for(j=1;j<=t;j++){
        cin>>s;
//        fin>>s;
        n=s.size();
        for(i=n-1;i>=0;i--){
            if(s[i]=='-'){
                ans++;
                i--;
                for(;i>=0;i--){
                    if(s[i]!=s[i+1])ans++;
                }
            }
        }
        cout<<"Case #"<<j<<": ";
        cout<<ans<<endl;
//        fout<<"Case #"<<j<<": ";
//        fout<<ans<<endl;
        ans=0;
    }
	return 0;
}
