#include <bits/stdc++.h>

using namespace std;

int main()
{
    int k,c,s;
    int t;
    fstream cin("b");
    ofstream cout("br");
    vector<int> v;
    cin>>t;
    int cases=0;
    while(t--){
    v.clear();
    cin>>k>>c>>s;
    cases++;
    for(int i=1;i<=k;i++){
    v.push_back(i);
    }



     cout<<"Case #"<<cases<<": ";
     for(int j=0;j<v.size()-1;j++){
     cout<<v[j]<<" ";
     }
     cout<<v[v.size()-1]<<endl;



    }
    return 0;
}
