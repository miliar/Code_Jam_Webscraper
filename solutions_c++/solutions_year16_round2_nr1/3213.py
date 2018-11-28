#include<bits/stdc++.h>
using namespace std;

int main(){
    int T;cin>>T;
    for(int t=1;t<=T;t++){
        int A[26];
        for(int i=0;i<26;i++)
            A[i]=0;
        string str;
        cin>>str;
        int n=str.length();
        for(int i=0;i<n;i++)
            A[str[i]-65]++;
        vector<int> ans;
        for(int i=0;i<A[25];i++){
            A[4]--;
            A[17]--;
            A[14]--;
            ans.push_back(0);
        }
        A[25]=0;
        for(int i=0;i<A[23];i++){
            A[8]--;
            A[18]--;
            ans.push_back(6);
        }
        A[23]=0;
        
        for(int i=0;i<A[6];i++){
            A[4]--;
            A[8]--;
            A[7]--;
            A[19]--;
            ans.push_back(8);
        }
        A[6]=0;
        
        for(int i=0;i<A[22];i++){
            A[14]--;
            A[19]--;
            ans.push_back(2);
        }
        A[22]=0;
        
        for(int i=0;i<A[20];i++){
            A[5]--;
            A[14]--;
            A[17]--;
            ans.push_back(4);
        }
        A[20]=0;
        
        for(int i=0;i<A[19];i++){
            A[7]--;
            A[17]--;
            A[4]--;
            A[4]--;
            ans.push_back(3);
        }
        A[19]=0;
        
        for(int i=0;i<A[14];i++){
            A[13]--;
            A[4]--;
            ans.push_back(1);
        }
        A[14]=0;
        
        for(int i=0;i<A[5];i++){
            A[8]--;
            A[22]--;
            A[4]--;
            ans.push_back(5);
        }
        A[5]=0;
        
        for(int i=0;i<A[18];i++){
            A[4]--;
            A[21]--;
            A[4]--;
            A[13]--;
            ans.push_back(7);
        }
        A[18]=0;
        
        for(int i=0;i<A[4];i++){
            A[13]--;
            A[8]--;
            A[13]--;
            ans.push_back(9);
        }
        A[4]=0;
        
        sort(ans.begin(),ans.end());
        cout<<"Case #"<<t<<": ";
        
        for(int i=0;i<ans.size();i++)
            cout<<ans[i];
        cout<<endl;
    }
}