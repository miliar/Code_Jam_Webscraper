#include <iostream>
#include <sstream>
#include <string>

#include <cmath>
#include <algorithm>
#include <vector>

typedef long long ll;
using namespace std;
const ll MAX=1e15;
vector <ll> v;

bool isPalindrome(ll i){
    string s; stringstream sst;
    sst << i; sst >> s; string rs=s;
    reverse(rs.begin(),rs.end());
    if(s==rs) return true;
    else return false;
}

void precompute(){

    for (ll i=1;pow(i,2)<=MAX;i++)
        if(isPalindrome(pow(i,2)) && isPalindrome(i))
            v.push_back(pow(i,2));
}

int solve(){
    int result=0;
    ll a,b; cin>>a>>b;
    for (unsigned int i=0; i<v.size(); i++){
        if ((a<=v[i])&&(v[i]<=b)) result++;
    }
    return result;
}

int main()
{
    int t; cin>>t;
    precompute();
    for (int i=1; i<=t; i++)
        cout<<"Case #"<<i<<": "<<solve()<<endl;
    return 0;
}

