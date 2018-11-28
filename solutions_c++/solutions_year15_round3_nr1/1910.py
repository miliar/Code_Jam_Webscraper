#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>
#include <cmath>
#include <vector>
#include <algorithm>




#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

ifstream in("INPUT.TXT");
ofstream out("OUTPUT2.TXT");


typedef long long Int;
typedef pair<int,int> PII;
typedef vector<int> VInt;


int main()
{
    int T = 0;
    int R = 0;
    int C = 0;
    int W = 0;
    in >> T;
    for (int iT = 0; iT<T; iT++)
    {
        cout<<"iT "<<iT<<endl;
        in >> R;
        in >> C;
        in >> W;
        //int answ = R*(C/W +W -1);
        int answ = 0;
        //cout<<"C%(2*W-1) "<<C%(2*W-1)<<endl;
        if ((C%W) == 0)
        {

            answ = C/W + W-1;
            //cout<<N<<endl;
        }
        else
        {

            answ = C/W + W;
            //cout<<"Nrem  "<<Nrem<<endl;
        }
        out<<"Case #"<<iT+1<<": "<<answ<<endl;
    }



    return 0;
}
