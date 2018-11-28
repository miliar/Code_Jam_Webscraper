#include <bits/stdc++.h>
using namespace std;

int main() {

    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    string s;
    int count,ss;
    for(int j=1;j<=t;j++)
    {
        cin>>s;
        count=0;
        ss=s.size();
        for(int i=0;i<ss;i++){
            if(count==0&&s[i]=='-'){
                count++;
            }
            else if(s[i]=='+'&&((i+1)<ss)&&(s[i+1]=='-')){
                count+=2;
            }
        }
        cout<<"Case #"<<j<<": "<<count<<endl;
        
    }
    
	return 0;
}
