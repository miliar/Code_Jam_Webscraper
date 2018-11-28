#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <complex>
#include <iomanip>
using namespace std;

int main() {    
    
    freopen("D:\\Desktop\\B-large.in","r",stdin);
    freopen("D:\\Desktop\\B-large.out","w",stdout);
            
    int T, cnt;
    string str;
    
    cin>>T;    
    for(int i=1;i<1+T;i++){
        
        cin>>str;
        cnt=0;        
        for(int j=1;j<str.length();j++){
            if(str[j]!=str[j-1])
                cnt++;
        }
        cout<<"Case #"<<i<<": "<<cnt + (str[str.length()-1]=='-'? 1:0)<<endl;
    }    
    return 0;
}
