#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;


int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
		freopen("2.out","w",stdout);
    #endif // ONLINE_JUDGE
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string num[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    int arr[]= {2,8,6,0,3,4,5,7,1,9};
    char x[]= {'W','G','X','Z','H','R','F','V','O','N'};
    int T;
    cin>>T;
    for(int ic=1;ic<=T;ic++) {
      string s;
      cin>>s;
      map<char,int> m;
      for(int i=0;i<s.size();i++) {
        m[s[i]]++;
      }
      vector<int> v;
      for(int i=0;i<10;i++) {
        while(m[x[i]] > 0) {
          v.push_back(arr[i]);
          string n = num[arr[i]];
          for(int j=0;j<n.size();j++)
            m[n[j]]--;
        }
      }
      cout<<"Case #"<<ic<<": ";
      sort(v.begin(),v.end());
      for(int i=0;i<v.size();i++)
        cout<<v[i];
      cout<<endl;
    }
    return 0;
    
}
