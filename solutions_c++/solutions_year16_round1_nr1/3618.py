#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long int t;
    cin>>t;
    long long int cc = 1;
    while(t--){
        //break;
        string s;
        cin>>s;
        //fscanf(myFile, "%s", s);
        //cin>>s;
        string ans1 = "";
        string ans2 = "";
        string curr_ans = "";
        long long int i;
        for(i = 0; i < s.length(); i++){
            ans1 = curr_ans + s[i];
            ans2 = s[i] + curr_ans;
            if(ans1 > ans2){
                curr_ans = ans1;
            }
            else{
                curr_ans = ans2;
            }
        }
        cout<<"Case #"<<cc++<<": "<<curr_ans<<"\n";
    }
    return 0;
}
