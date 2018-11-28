#include<bits/stdc++.h>
using namespace std;
int arr[10][26],acnt[26];
int main(){
    int t;
    cin>>t;
    string num[10]={"ZERO", "TWO","SIX","EIGHT", "SEVEN","FIVE","THREE", "FOUR", "ONE","NINE"};
    char ord[10]={'Z','W','X','G','S','V','T','F','O','I'};
    int abc[10]={0,2,6,8,7,5,3,4,1,9};
    for(int i=0;i<10;i++){
        for(int j=0;j<num[i].size();j++){
            arr[i][num[i][j]-'A']++;
        }
    }
    vector<int> ans;
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<": ";
        string s;
        int n;
        cin>>s;
        n=s.size();
        int cnt[10];
        for(int i=0;i<26;i++)
            acnt[i]=0;
        for(int i=0;i<n;i++){
            acnt[s[i]-'A']++;
        }
        ans.clear();
        for(int i=0;i<10;i++){
            cnt[i]=0;
            if(acnt[ord[i]-'A']>0){
                int mn=acnt[ord[i]-'A'];///arr[i][ord[i]-'A'];
                //for(int j=0;j<num[i].size();j++){
                //    if(arr[i][num[i][j]-'A']!=0)
                //    mn=min(mn,acnt[num[i][j]-'A']/arr[i][num[i][j]-'A']);
                //}
                cnt[i]=mn;
                for(int j=0;j<num[i].size();j++){
                    acnt[num[i][j]-'A']-=(mn*arr[i][num[i][j]-'A']);
                }
            }

        }
        for(int i=0;i<10;i++){
            for(int j=0;j<cnt[i];j++){
                ans.push_back(abc[i]);
            }
        }
        sort(ans.begin(),ans.end());
        for(int i=0;i<ans.size();i++){
            cout<<ans[i];
        }
        cout<<endl;
    }
}
