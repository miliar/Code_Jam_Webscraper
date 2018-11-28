#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <iterator>


using namespace std;

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    
    
    int test_case,this_case=0;
    cin>>test_case;
    int X,R,C;
    int ans;
    while (this_case<test_case) {
        cin>>X;
        cin>>R;
        cin>>C;
        
        if (R*C%X==0) {
            if (X==1) {
                ans=0;
            }else if(X==2)
            {
                ans=0;
            }else if(X==3)
            {
                if (R*C==3) {
                    ans=1;
                }else{
                    ans=0;
                }
            }else if(X==4)
            {
                if (R*C==4||R*C==8) {
                    ans=1;
                }else{
                    ans=0;
                }
            }
        }else{
            ans =1;
        }
        
        
        
        this_case++;
        
        cout<<"Case #"<<this_case<<": "<<(ans?"RICHARD":"GABRIEL")<<endl;

    }
    
    
    
    return 0;
}