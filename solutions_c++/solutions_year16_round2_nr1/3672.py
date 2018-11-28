#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<math.h>
#include<fstream>
using namespace std;
typedef long long ll;
#define      pii               std::pair<int,int>
#define      vi                std::vector<int>
#define      mp(a,b)           make_pair(a,b)
#define      pb(a)             push_back(a)
#define      each(it,s)        for(auto it = s.begin(); it != s.end(); ++it)
#define      rep(i, n)         for(int i = 0; i < (n); ++i)
#define      fill(a)           memset(a, 0, sizeof (a))
#define      sortA(v)          sort(v.begin(), v.end())
#define      sortD(v)          sort(v.begin(), v.end(), greater<auto>())
#define      X                 first
#define      Y                 second
ll MOD = 1000000007;
// First remove zero, right, six,two, four , five
string solve(int c) {
    string ss[10]= {"ZERO","ONE","TWO","THREE","FOUR", "FIVE","SIX", "SEVEN","EIGHT","NINE"};
    return ss[c];

}
int main() {
    freopen("in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    int t;
    cin>>t;
    for(int tt=1; tt<=t; tt++) {
        string ss;
        cin>>ss;
        int arr[40];
        for(int i=0; i<34; i++)
            arr[i]=0;
        int aa[11];
        for(int i=0; i<10; i++)
            aa[i]=0;
        //  sort(ss.begin(),ss.end());
        string temp;
        for(int i=0; i<ss.size(); i++) {
            arr[ss[i]-'A']++;
        }

        while(arr['Z'-'A']>0) {
            if(arr['Z'-'A']>0&&arr['E'-'A']>0 &&arr['R'-'A']>0 &&arr['O'-'A']>0) {
                arr['Z'-'A']--;
                arr['E'-'A']--;
                arr['R'-'A']--;
                arr['O'-'A']--;
                aa[0]++;
            }
              else
                break;

        }

        while (arr['G'-'A']>0) {
            if(arr['E'-'A']>0&&arr['I'-'A']>0 &&arr['G'-'A']>0 &&arr['H'-'A']>0&&arr['T'-'A']>0) {
                arr['E'-'A']--;
                arr['I'-'A']--;
                arr['G'-'A']--;
                arr['H'-'A']--;
                arr['T'-'A']--;
                aa[8]++;
            }
              else
                break;
        }
        while (arr['X'-'A']>0) {
            if(arr['S'-'A']>0&&arr['I'-'A']>0 &&arr['X'-'A']>0 ) {
                arr['S'-'A']--;
                arr['I'-'A']--;
                arr['X'-'A']--;
                aa[6]++;
            }
              else
                break;
        }
        while (arr['W'-'A']) {
            if(arr['T'-'A']>0&&arr['W'-'A']>0 &&arr['O'-'A']>0 ) {
                arr['T'-'A']--;
                arr['W'-'A']--;
                arr['O'-'A']--;
                aa[2]++;
            }
              else
                break;
        }

        while (arr['U'-'A']>0) {
            if(arr['F'-'A']>0&&arr['O'-'A']>0 &&arr['U'-'A']>0 &&arr['R'-'A']>0) {
                arr['F'-'A']--;
                arr['O'-'A']--;
                arr['U'-'A']--;
                arr['R'-'A']--;
                aa[4]++;
            }
              else
                break;
        }
        while (arr['V'-'A']>0) {
            if(arr['F'-'A']>0&&arr['I'-'A']>0 &&arr['V'-'A']>0 &&arr['E'-'A']>0) {
                arr['F'-'A']--;
                arr['I'-'A']--;
                arr['V'-'A']--;
                arr['E'-'A']--;
                aa[5]++;
            }
            else
                break;
        }

        while (arr['R'-'A']>0) {
            if(arr['T'-'A']>0&&arr['H'-'A']>0 &&arr['R'-'A']>0 &&arr['E'-'A']>1) {
                arr['T'-'A']--;
                arr['H'-'A']--;
                arr['R'-'A']--;
                arr['E'-'A']--;
                arr['E'-'A']--;
                aa[3]++;
            }
              else
                break;
        }
        while (arr['V'-'A']>0) {
            if(arr['S'-'A']>0&&arr['E'-'A']>1 &&arr['V'-'A']>0 &&arr['N'-'A']>0) {
                arr['S'-'A']--;
                arr['E'-'A']--;
                arr['V'-'A']--;
                arr['E'-'A']--;
                arr['N'-'A']--;
                aa[7]++;
            }
              else
                break;
        }
        while (arr['O'-'A']) {
            if(arr['O'-'A']>0&&arr['N'-'A']>0 &&arr['E'-'A']>0) {
                arr['O'-'A']--;
                arr['N'-'A']--;
                arr['E'-'A']--;
                aa[1]++;
            }
              else
                break;
        }

        while (arr['I'-'A']>0) {
            if(arr['N'-'A']>0&&arr['I'-'A']>0 &&arr['N'-'A']>0 &&arr['E'-'A']>0) {
                arr['N'-'A']--;
                arr['I'-'A']--;
                arr['N'-'A']--;
                arr['E'-'A']--;
                aa[9]++;
            }
              else
                break;
        }

        cout<<"Case #"<<tt<<": ";
        for(int i=0; i<=9; i++) {
            for(int j=0; j<aa[i]; j++) {
                cout<<i;
            }
        }
        cout<<endl;

    }
    return 0;
}

