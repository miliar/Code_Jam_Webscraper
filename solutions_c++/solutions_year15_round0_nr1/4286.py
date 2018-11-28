//#include <bits\stdc++.h>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <deque>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    fstream f("A-large.in" , ios::in);
    fstream ff("A-small-attempt0.out" , ios::out);
    int t; f >> t;
    for(int q = 0; q < t; q++)
    {
        int n,c = 0 , sum = 0; f >> n;
        for(int i = 0; i <= n; i ++)
        {
            char ch; f >> ch;
            sum += (ch-48);
            if(sum < i+1){
                sum = i+1;
                c++;
            }
        }
        ff << "Case #"; ff << q+1; ff << ": "; ff <<  c; ff << '\n';
    }
}
/*//#include <bits\stdc++.h>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <deque>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
   // fstream f("A-small-attempt0.in" , ios::in);
    //fstream ff("A-small-attempt0.out" , ios::out);
    int t;
    //f << t;
    cin >> t;
    for(int q = 0; q < t; q++)
    {
        int n,c = 0;
        //f << n;
        cin >> n;
        for(int i = 0; i <= n; i ++)
        {
            char ch;
            //f << ch;
            cin >> ch;
            if(ch == '0')
                c++;
        }
        cout <<"Case #"<< q+1 << ": " <<  c << '\n';
       // ff << "Case #"; ff << q+1; ff << ": "; ff <<  c; ff << '\n';
    }

}


*/

