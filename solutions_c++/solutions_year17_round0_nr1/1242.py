#include <iostream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

int main()
{
    int N;
    int k;
    string s;
    cin>>N;
    
    for(int i=0; i<N; ++i){
            int sum = 0;
            cin>>s>>k;
            for(int t=0; t<s.length() && t<=s.length()-k; ++t){
                if(s[t]=='+')
                        continue;
                ++sum;
                for(int j=t; j<t+k; ++j)
                    s[j]=(s[j]=='+' ? '-' : '+');
            }
            bool b = 1;
            for(int t=0; t<s.length(); ++t)
                    b = b && s[t]=='+';
                    if(!b)
                cout<<"Case #"<<i+1<<": IMPOSSIBLE\n";
            else
                cout<<"Case #"<<i+1<<": "<<sum<<"\n";
    
    }
return 0;
}
 
