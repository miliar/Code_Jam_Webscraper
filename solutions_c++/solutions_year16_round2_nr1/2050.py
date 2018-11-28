#include <bits/stdc++.h>

using namespace std;
int arr[200];
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    string x;
    int t;
    cin>>t;
    int cases=0;
    while(t--){
        cases++;
        cin>>x;
        memset(arr,0,sizeof arr);
        for(int i=0;i<x.size();i++)
            arr[x[i]]++;
        vector<int> ans;
        string cur="ZERO";
        int zeros=arr['Z'];
        for(int i=0;i<zeros;i++){
            ans.push_back(0);
            for(int j=0;j<cur.size();j++)
                arr[cur[j]]--;
        }
         cur="SIX";
         zeros=arr['X'];
        for(int i=0;i<zeros;i++){
            ans.push_back(6);
            for(int j=0;j<cur.size();j++)
                arr[cur[j]]--;
        }
         cur="TWO";
         zeros=arr['W'];
        for(int i=0;i<zeros;i++){
            ans.push_back(2);
            for(int j=0;j<cur.size();j++)
                arr[cur[j]]--;
        }
         cur="EIGHT";
         zeros=arr['G'];
        for(int i=0;i<zeros;i++){
            ans.push_back(8);
            for(int j=0;j<cur.size();j++)
                arr[cur[j]]--;
        }
        cur="THREE";
         zeros=arr['H'];
        for(int i=0;i<zeros;i++){
            ans.push_back(3);
            for(int j=0;j<cur.size();j++)
                arr[cur[j]]--;
        }
        cur="FOUR";
        zeros=arr['U'];
        for(int i=0;i<zeros;i++){
            ans.push_back(4);
            for(int j=0;j<cur.size();j++)
                arr[cur[j]]--;
        }
        cur="FIVE";
         zeros=arr['F'];
        for(int i=0;i<zeros;i++){
            ans.push_back(5);
            for(int j=0;j<cur.size();j++)
                arr[cur[j]]--;
        }

        cur="SEVEN";
         zeros=arr['V'];
        for(int i=0;i<zeros;i++){
            ans.push_back(7);
            for(int j=0;j<cur.size();j++)
                arr[cur[j]]--;
        }
        cur="ONE";
         zeros=arr['O'];
        for(int i=0;i<zeros;i++){
            ans.push_back(1);
            for(int j=0;j<cur.size();j++)
                arr[cur[j]]--;
        }
        cur="NINE";
         zeros=arr['I'];
        for(int i=0;i<zeros;i++){
            ans.push_back(9);
            for(int j=0;j<cur.size();j++)
                arr[cur[j]]--;
        }
        sort(ans.begin(),ans.end());
        cout<<"Case #"<<cases<<": ";
        for(int i=0;i<ans.size();i++)cout<<ans[i];
        cout<<endl;
    }
    return 0;
}
