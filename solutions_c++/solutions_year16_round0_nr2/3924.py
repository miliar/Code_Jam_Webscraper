#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(){
    freopen("B-large.txt","r",stdin);
    freopen("outCG.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=1; tc<=t; tc++){
        string s;
        cin>>s;
        cout<<"Case #"<<tc<<": ";
        int ans=0;
        for(int i=1; i<s.size(); i++){
            if(s[i]=='-'&&s[i-1]=='+') ans++;
        }
        cout<<ans*2+(s[0]=='-')<<endl;
    }
}