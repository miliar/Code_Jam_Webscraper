#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;

#define SSTR( x ) dynamic_cast< std::ostringstream & >(( std::ostringstream() << std::dec << x ) ).str()

int res(string s){
    int l=0;
    int ends,cont=1;
    while (cont>0){
        ends=-1,cont=0;
        for (int i=0; i<s.size() && cont<2; i++){
            if (cont==0 && s[i] == '-'){
                cont=1;
                ends=i;
                }
            if (cont==1 && s[i] == '+'){
                cont=2;
                ends=i-1;
                }
            }
        if (cont>0){
            for (int i=0;i<=(cont==1?s.size()-1:ends);i++){
                s[i]=(s[i]=='-'?'+':'-');
                }
            //cout << s << endl;
            l++;
            }
        }
    return l;
    }

int main(){
int n;
string k;
cin >> n;
for (int i=1;i<=n;i++){
    cin >> k;
    cout << "Case #" << i << ": " << res(k) << endl;
    }
return 0;
}



