#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main()
{
    ifstream fe ("A-large.in");
    ofstream fs ("resp2.out");
    int t;
    fe>>t;
    string cad;
    for (int q = 1; q <= t; q++)
    {
        fe>>cad;
        list <char> res;
        list <char> ::iterator s;
        res.push_back(cad[0]);
        for (int w = 1; w < cad.length(); w++)
        {
            int n1 = cad[w];
            int n2 = *(res.begin());
            string aux = "";
            if (n1 >= n2)
            {
                res.push_front(cad[w]);

            }
            else
            {
                res.push_back(cad[w]);

            }
            //cout<<aux<<" "<<res<<endl;
        }
        fs<<"Case #"<<q<<": ";
        for (s = res.begin(); s != res.end(); s++)
        {
            fs<<*s;
        }
        fs<<endl;
    }
    return 0;
}
