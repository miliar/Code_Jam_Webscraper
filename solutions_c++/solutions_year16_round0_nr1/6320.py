#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;

#define SSTR( x ) dynamic_cast< std::ostringstream & >(( std::ostringstream() << std::dec << x ) ).str()

int res(int x){
    string s;
    int r=0,l=0,mask;
    for (l=x; ;l+=x){
        s = SSTR( l );
        for (string::iterator it = s.begin();it != s.end(); ++it){
            mask = 1;
            mask = mask << (*it-'0');
            r = r | mask;
            }

        if (r == 1023){ //1111111111
            break;
            }
        }
    return l;
    }

int main(){
int n,k;
cin >> n;
for (int i=1;i<=n;i++){
    cin >> k;
    if (k==0){
        cout << "Case #" << i << ": " << "INSOMNIA" << endl;
        }
        else{
            cout << "Case #" << i << ": " << res(k) << endl;
        }

    }
return 0;
}



