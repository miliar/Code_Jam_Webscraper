#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main()
{
    ofstream out;
    ifstream in("A-large.in");
    out.open("output.txt");

    int t;
    in >> t;
    for(int tn = 1; tn <= t; tn++){
        int n;
        in >> n;
        int p[n];
        ll sum = 0;
        for(int i = 0; i < n; i++){
            in >> p[i];
            sum += p[i];
        }
        int l, k;
        vector<string> sol;
        int mx1 = 0, mx2 = 0;
        while(sum > 1){
            string str = "";
            mx1 = 0;
            mx2 = 0;
            for(int i = 0; i < n; i++){
                if(p[i] > mx1){
                    mx2 = mx1;
                    k = l;
                    mx1 = p[i];
                    l = i;
                }
                if(p[i] > mx2 && p[i] <= mx1 && i != l){
                    mx2 = p[i];
                    k = i;
                }
            }
            p[l] -= 1;
            str += 'A' + l;
            p[k] -= 1;
            str += 'A' + k;
            sol.push_back(str);
            sum -= 2;
        }

        if(sum > 0){
            string str = "";
            for(int i = 0; i < n; i++){
                if(p[i] == 1){
                    mx1 = p[i];
                    p[i] -= 1;
                    str += 'A'+i;
                }
            }
            string xs = sol[sol.size()-1];
            sol.pop_back();
            sol.push_back(str);
            sol.push_back(xs);
        }
        out << "Case #" << tn << ": ";
        for(int i = 0; i < sol.size(); i++){
            if(i == sol.size()-1){
                out << sol[i] << endl;
                break;
            }
            out << sol[i] << " ";
        }


    }

    out.close();
    in.close();
    return 0;
}
