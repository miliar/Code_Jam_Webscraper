#include <bits/stdc++.h>

using namespace std;

set<string> vc;
set<string> tmp;

int main()
{
    int tetC;
    cin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++)
    {
        string vl;
        cin >> vl;
        cout << "Case #"<<cnt+1<<": ";
        string ret = "";
        ret = vl[0] + ret;
        for(int ct = 1; ct < vl.size(); ct++)
        {
            //cout << vl[ct] << endl;
            if(vl[ct] >= ret[0])
                ret = vl[ct] + ret;
            else
                ret += vl[ct];
        }

        /*string ret = "";
        vc.insert("");
        for(int ct = 0; ct < vl.size(); ct++)
        {
            tmp.clear();
            set<string>::iterator trv;
            for(trv = vc.begin(); trv != vc.end(); trv++)
            {
                tmp.insert(*trv + vl[ct]);
                tmp.insert(vl[ct] + *trv);

            }
            vc.clear();
            for(trv = tmp.begin(); trv != tmp.end(); trv++)
            {
                //cout << " tmp " <<*trv << endl;
                vc.insert(*trv);
            }
            //vc.insert(vc.end() , tmp.begin() , tmp.end());
        }

        //sort(vc.begin(), vc.end());

        cout << *vc.rbegin() << endl;
*/

cout << ret << endl;
    }
}
