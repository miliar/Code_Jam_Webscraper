#include <iostream>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;
set<long long> primes;
long long maxp = 33333331L ;

string solve(string num)
{
    long long val = 0,mul =1;
    string ansLine = num;
    reverse(num.begin(),num.end());
    bool can = true;
    for (int base =2; base<=10; base++)
    {
        mul = 1;
        val = 0;
        for (int i=0; i<num.size(); i++)
        {
            val += mul*(num[i]-'0');
            mul *= base;
        }
        if (val <= maxp)
        {
            if (primes.count(val) != 0) {
                can = false;
                break;
            }
            else
            {
                for (auto x:primes) {
                    if (val%x == 0) {
                        ansLine += " "+to_string(x);
                        break;
                    }
                }
            }
        }
        else
        {
            bool tcan = false;
            for (auto x:primes) {
                if (val%x == 0) {
                    tcan = true;
                    ansLine += " "+to_string(x);
                    break;
                }
            }
            can = can && tcan;
        }
    }
    if (!can) {
        return "";
    }
    else
        return ansLine;
}

int main()
{
    std::ios::sync_with_stdio(false);
    
    for (long long i=2; i<33333334; i++) {
        bool can = true;
        for (set<long long>::iterator si=primes.begin(); si!=primes.end(); si++) {
            if(i%(*si) == 0)
            {
                can = false;
                break;
            }
            if (i < (*si)*(*si)) {
                break;
            }
        }
        if (can) {
            primes.insert(i);
        }
    }
    
    
    
    int N=16,J=50;
    vector<string> ans;
    for (int i=0; i<(1<<(N-2)); i++) {
        string bin = "1";
        string tmp = "";
        int tn = i;
        do {
            int rem = tn % 2;
            tn = tn /2 ;
            tmp += to_string(rem);
        } while (tn >0);
        reverse(tmp.begin(),tmp.end());
        int szdiff = N - 2 - tmp.size();
        string fil = string(szdiff,'0');
        bin += fil + tmp + "1";
        string ansLine = solve(bin);
        if (ansLine.size() > 0) {
            ans.push_back(ansLine);
        }
        
    }
    int cnt = 0;
    cout << "Case #1:" << endl;
    for (auto line:ans) {
        cnt++;
        cout<<line<<endl;
        if (cnt == J) {
            break;
        }
    }
    return 0;
}

