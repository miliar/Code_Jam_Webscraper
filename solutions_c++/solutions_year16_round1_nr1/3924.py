#include <bits/stdc++.h>
#define LLI long long int
#define LLUI long long unsigned int
#define LD long double
#define MOD 1000000007LL
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?-(x):(x))
using namespace std;

int main() {
    int T,i,j;
    int arr[28];
    deque <char> vec;
    cin>>T;
    for(int tc=1;tc<=T;tc++){
        string str;
        cin>>str;
        
        vec.push_back(str[0]);
        for(i=1;i<str.length();i++){
            if(vec[0]>str[i])
                vec.push_back(str[i]);
            else
                vec.push_front(str[i]);
        }
        cout<<"Case #"<<tc<<": ";
        for(i=0;i<vec.size();i++){
            cout<<vec[i];
        }
        cout<<endl;
        vec.clear();
    }
    return 0;
}
