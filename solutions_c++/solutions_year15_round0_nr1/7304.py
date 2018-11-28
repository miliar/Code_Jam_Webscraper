#include<iostream>

using namespace std;

int main(){
    int n_test, i, n_aud;
    char c;
    int case_n=1;
    cin>>n_test;
    while(n_test-->0){
        cin>>n_aud;
        int sz = n_aud + 1;
        int s[sz];
        for(i=0;i<sz;i++){
            cin>>c;
            s[i] = c - '0';
        }
        int curr=0, required=0;
        for(i=0;i<sz;i++){
            if(i<= (curr+required)){
                curr += s[i];
            }else{
                if(s[i] > 0){
                required += (i - (curr+required));
                curr += s[i];
                }
            }
        }
        cout<<"Case #"<<case_n++<<": "<<required<<endl;
   }
}
        
        
