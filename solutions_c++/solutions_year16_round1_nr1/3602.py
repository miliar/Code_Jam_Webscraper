#include<iostream>
#include<vector>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int x=1;x<=t;x++)
    {
        string s;
        cin>>s;
        int len = s.size();
        vector<char>left;
        vector<char>right;
        char curr=s[0];
        for (int i=1;i<len;i++){
            if (s[i]>=curr){
                left.push_back(s[i]);
                curr=s[i];
            }
            else{
                right.push_back(s[i]);
            }
        }
        cout<<"Case #"<<x<<": ";
        for (int i=left.size()-1;i>=0;i--){
            cout<<left[i];
        }
        cout<<s[0];
        for(int i=0;i<right.size();i++){
            cout<<right[i];
        }
        cout<<"\n";
    }
}
