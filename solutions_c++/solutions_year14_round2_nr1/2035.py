#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <ctype.h>
#include <stack>
#include <queue>
#include <limits.h>
#include <fstream>
#include <map>
#include <set>

#define rep(i, a) for(int i = 0; i < a; i++)
#define rep1(i, a) for(int i = 1; i <= a; i++)
#define fo(i, a, b) for(int i = a; i < b; i++)
#define defo(i, a, b) for(int i = a; i >= b; i--)
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a.size()))
#define x first
#define y second
#define SET(x, a) memset(x, a, sizeof(x));
using namespace std;

typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
int abs(int a){
    if(a<0){
        return -1*a;
    }
    return a;
}
int main(){
    freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
    int test,l=0;
    cin>>test;
    while(test--){
        int ans = 0;
        l++;
        string s1[105],s3[105];
        vector<int> v1[105];
        int n;
        cin>>n;
        int i,j;
        for(i=0;i<n;i++){
            cin>>s1[i];
            s3[i] = "";
        }
        for(j=0;j<n;j++){
            int x = 1;
            char c = s1[j][0];
            for(i=1;i<s1[j].size();i++){
                if(s1[j][i]==c){
                    x++;
                }
                else{
                    v1[j].push_back(x);
                    x = 1;
                    s3[j]=s3[j]+c;
                    c = s1[j][i];
                }
            }
            v1[j].push_back(x);
            x = 1;
            s3[j]=s3[j]+c;
            //cout<<s3[j]<<"\n";
        }
        string coo = s3[0];
        int f = 0;
        for(i=0;i<n;i++){
            if(s3[i]!=coo){
                f = 1;
                break;
            }
        }
        if(f==1){
            cout<<"Case #"<<l<<": "<<"Fegla Won\n";
        }
        else{
            for(i=0;i<s3[0].size();i++){
                vector<int> arr;
                for(j=0;j<n;j++){
                    arr.push_back(v1[j][i]);
                }
                sort(arr.begin(),arr.end());
                int in = (arr.size()+1)/2;
                in--;
                /*for(j=0;j<arr.size();j++){
                    cout<<arr[j]<<" ";
                }*/
               // cout<<"\n";
               // cout<<in<<"\n";
                int k = 0;
                for(j=0;j<in;j++){
                    k+=arr[j+1] - arr[j];
                    ans+=k;
                }
                k = 0;
                for(j=n-2;j>=in;j--){
                    k+=arr[j+1] - arr[j];
                    ans+=k;
                }
            }
            cout<<"Case #"<<l<<": "<<ans<<"\n";
        }
    }
    return 0;
}
