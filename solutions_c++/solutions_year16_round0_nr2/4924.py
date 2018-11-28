#include<iostream>
#include<string>

using namespace std;

int main(){
    int c_n, t;
    cin>>t;
    c_n = 1;
    int i;
    while(t--){
        string s;
        cin>>s;
        cout<<"Case #"<<c_n<<":";
        c_n++;
        int cnt=0;
        if(s[s.size()-1] == '-')
            cnt++;
        char curr = s[0];
        for(i=1; i< s.size();i++){
            if(curr != s[i]){
                cnt++;
                curr = s[i];
            }
        }
        cout<<" "<<cnt<<endl;
    }
}

