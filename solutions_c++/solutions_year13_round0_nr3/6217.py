#include <iostream>
#include <sstream>
#include <cmath>
#include <stdio.h>
#include <cstdlib>
using namespace std;

bool is_palind(int num)
{
stringstream ss;
ss << num;
string inp;
ss >> inp;
for(int i = 0 ; i <= inp.length()/2;++i)
    if(inp[i] != inp[inp.length()-i-1])
     return false;
return true;
}
int main()
{
    int t , x,y;
 freopen("C-small-attempt0.in","r",stdin);
 freopen("C-small-attempt0.out","w",stdout);

    cin >> t;
    for(int q = 1 ; q <=t ; ++q){
    int count = 0;
     cin >> x >> y;
     while(x <= y){
        if(is_palind(x) && (int)sqrt(x) *(int)sqrt(x) == x && is_palind((int)sqrt(x)))
            count++;
        x++;
     }
        cout << "Case #"<<q<<": "<<count<<endl;
    }

    return 0;
}
