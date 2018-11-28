#include <bits/stdc++.h>


using namespace std;

int main()
{
    ofstream out;
    ifstream in("A-large.in");
    out.open("output.txt");

    int t;
    in >> t;
    for(int tn = 1; tn <= t; tn++){
        long long n;
        in >> n;
        if(n == 0){
            out << "Case #" << tn << ": INSOMNIA" << endl;
            continue;
        }
        set<int> xs;
        long long cnt1 = 1;
        long long tmp = n;
        long long tmp2 = n;
        while(tmp){
            while(tmp){
                int c = tmp % 10;
                tmp = tmp / 10;
                xs.insert(c);
                if(xs.size() == 10){
                    out << "Case #" << tn << ": " << n << endl;
                    goto s;
                }
            }
            cnt1++;
            n = cnt1 * tmp2;
            tmp = n;
        }

        s:;

    }

    out.close();
    in.close();
    return 0;
}
