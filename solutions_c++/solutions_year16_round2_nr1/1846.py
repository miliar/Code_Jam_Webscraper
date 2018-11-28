#include<iostream>
#include<queue>
#include<vector>
#include<stack>
#include<string>
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<map>
#include<fstream>

using namespace std;

#define pb   push_back
#define mp   make_pair
#define s    second
#define ll   long long
#define For(i,j,n)  for(int (i) = (j); i < n; i++)
#define MAX(a, b)     ((a) > (b) ? (a) : (b))
#define MIN(a, b)     ((a) < (b) ? (a) : (b))
#define Max INT_MAX
#define Min INT_MIN
#define mod 1000000007

void printArray(int *a,int n){
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
}

void generateRandomArray(int *a,int n){
    for(int i=0;i<n;i++){
        a[i] = rand()%100;
    }
}

void generateSortedArray(int *a,int n){
    for(int i=0;i<n;i++){
        a[i] = rand()%100;
    }
    sort(a,a+n);
}
void generateLinearArray(int *a,int n){
    For(i,1,n+1){
        a[i-1]=i*2;
    }
    return;
}

void swapNo(int *a,int *b){
    int temp = *a;
    *a=*b;
    *b=temp;
    return;
}

ll power(ll base, ll exp) {
    ll r=1;
    while(exp>0) {
       if(exp%2==1) r=(r*base)%mod;
       base=(base*base)%mod;
       exp/=2;
    }
    return r%mod;
}

bool isPossible(int *a){
    for(int i=0;i<26;i++){
        if(a[i]>0){
            return true;
        }
    }
    return false;
}

int main(){
    ifstream in;
    ofstream out;
    in.open("test.txt");
    out.open("result.txt");
    int cases,ca=1;
    in>>cases;
    while(ca<=cases){
        int a[26]={0};
        string s;
        in>>s;
        for(int i=0;i<s.length();i++){
            a[(int)s[i]-'A']++;
        }
        vector<int> ans;
        while(isPossible(a)){
            if(a['Z'-'A']>0){
                a['Z'-'A']--;
                a['E'-'A']--;
                a['R'-'A']--;
                a['O'-'A']--;
                ans.push_back(0);
                continue;
            }else if(a['X'-'A']>0){
                a['S'-'A']--;
                a['I'-'A']--;
                a['X'-'A']--;
                ans.push_back(6);
                continue;
            }else if(a['G'-'A']>0){
                a['E'-'A']--;
                a['I'-'A']--;
                a['G'-'A']--;
                a['H'-'A']--;
                a['T'-'A']--;
                ans.push_back(8);
                continue;
            }else if(a['S'-'A']>0){
                a['S'-'A']--;
                a['E'-'A']--;
                a['V'-'A']--;
                a['E'-'A']--;
                a['N'-'A']--;
                ans.push_back(7);
                continue;
            }else if(a['V'-'A']>0){
                a['F'-'A']--;
                a['I'-'A']--;
                a['V'-'A']--;
                a['E'-'A']--;
                ans.push_back(5);
                continue;
            }else if(a['F'-'A']>0){
                a['F'-'A']--;
                a['O'-'A']--;
                a['U'-'A']--;
                a['R'-'A']--;
                ans.push_back(4);
                continue;
            }else if(a['W'-'A']>0){
                a['T'-'A']--;
                a['W'-'A']--;
                a['O'-'A']--;
                ans.push_back(2);
                continue;
            }else if(a['O'-'A']>0){
                a['O'-'A']--;
                a['N'-'A']--;
                a['E'-'A']--;
                ans.push_back(1);
                continue;
            }else if(a['N'-'A']>0){
                a['N'-'A']--;
                a['I'-'A']--;
                a['N'-'A']--;
                a['E'-'A']--;
                ans.push_back(9);
                continue;
            }else if(a['H'-'A']>0){
                a['T'-'A']--;
                a['H'-'A']--;
                a['R'-'A']--;
                a['E'-'A']--;
                a['E'-'A']--;
                ans.push_back(3);
                continue;
            }
        }
        sort(ans.begin(),ans.end());
        out<<"Case #"<<ca<<": ";
        for(int i=0;i<ans.size();i++){
            out<<ans[i];
        }
        out<<endl;
        ca++;
    }
    return 0;
}
