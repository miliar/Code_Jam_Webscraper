#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string.h>
#include <fstream>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <tuple>
#include <iomanip>
#define ull unsigned long long
#define ll long long
#define inf 1000000000000
#define bil 1000000000

using namespace std;


ifstream input;
ofstream output;


bool rsort(ll a, ll b){
    return a > b;
}

pair<bool, char> convert(char a, char b){
    //a * b
    if (a == '1'){
        return make_pair(0, b);
    }
    if (b == '1'){
        return make_pair(0, a);
    }
    if (a == b) return make_pair(1, '1');
    if (a == 'i'){
        if (b == 'j'){
            return make_pair(0, 'k');
        }
        if (b == 'k'){
            return make_pair(1, 'j');
        }
    }
    if (a == 'j'){
        if (b == 'i'){
            return make_pair(1, 'k');
        }
        if (b == 'k'){
            return make_pair(0, 'i');
        }
    }
    if (a == 'k'){
        if (b == 'i'){
            return make_pair(0, 'j');
        }
        if (b == 'j'){
            return make_pair(1, 'i');
        }
    }
    return make_pair(1, '1');
}

int main(int argc, char *argv[]) {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    input.sync_with_stdio(false);
    output.sync_with_stdio(false);
    input.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.in.txt");
    output.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.out.txt");
    
    ll cases, answer;
    pair<int, char>tot, tmpi, tmpj, tmpk, tmp, tmpfirst, tmpsecond, tmp2, tmp3;
    string s, tmps;
    int posi, posj, posk;
    posi = posj = posk = -1;
    ll appears;
    
    input>>cases;
    for (int i=0;i<cases;i++){
        output<<"Case #"<<i+1<<": ";
        input>>appears>>appears>>tmps;
        posi = posj = posk = -1;
        s.clear();
        for (int j=0;j<min((ll)100000, appears);j++){
            s += tmps;
        }
        //find tot
        tot.first = 0, tot.second = '1';
        for (int j=0;j<s.size();j++){
            tmp = convert(tot.second, s[j]);
            tot.first += tmp.first, tot.first %= 2;
            tot.second = tmp.second;
            if (tot.second == 'i' && posi == -1 && tot.first == 0)posi = j, tmpi = tot;
        }
        if (posi == -1) {
            output<<"NO\n";
            continue;
        }
        
        tmpk.first = 0, tmpk.second = '1';
        tmpj.first = 0, tmpj.second = '1';
        //find posk
        for (int j=(int)s.size()-1;j>=0;j--){
            tmp = convert(s[j], tmpk.second);
            tmpk.first += tmp.first, tmpk.first %= 2;
            tmpk.second = tmp.second;
            if (tmpk.first == 0 && tmpk.second == 'k' && posk == -1){
                posk = j;
                break;
            }
        }
        if (posk == -1){
            output<<"NO\n";
            continue;
        }
        if (appears <= 100000){
            if (posk <= posi+1){
                output<<"NO\n";
                continue;
            }
            
            else {
                for (int j=posi+1;j<posk;j++){
                    tmp = convert(tmpj.second, s[j]);
                    tmpj.first += tmp.first, tmpj.first %= 2;
                    tmpj.second = tmp.second;
                }
                if (tmpj.first != 0 || tmpj.second != 'j'){
                    output<<"NO\n";
                    continue;
                }
                else{
                    output<<"YES\n";
                    continue;
                }
            }
        }
        else{
            tot.first = 0, tot.second = '1';
            for (int j=0;j<tmps.size();j++){
                tmp = convert(tot.second, tmps[j]);
                tot.second = tmp.second;
                tot.first += tmp.first, tot.first %= 2;
            }
            
            if (tot.second != '1'){
                int mod = (appears)%4;
                if (mod % 2 == 0){
                    tot.second = '1';
                    if (mod == 0){
                        tot.first = 0;
                    }
                    else{
                        tot.first = 1;
                    }
                }
                else{
                    if (mod == 1){
                        tot.first = 0;
                    }
                    else{
                        tot.first = 1;
                    }
                }
            }
            else if (tot.first == 1 && appears%2 == 0)tot.first = 0;
            tmpfirst.first = 0, tmpfirst.second = '1';
            tmpsecond = tmpfirst;
            for (int j = posi+1;j<s.size();j++){
                tmp = convert(tmpfirst.second, s[j]);
                tmpfirst.second = tmp.second; tmpfirst.first = tmp.first, tmpfirst.first %= 2;
            }
            for (int j=0;j<posk; j++){
                tmp = convert(tmpsecond.second, s[j]);
                tmpsecond.second = tmp.second; tmpsecond.first = tmp.first, tmpsecond.first %= 2;
            }
            tmp = convert(tmpfirst.second, tot.second);
            tmp2 = convert(tmp.second, tmpsecond.second);
            tmp2.first = tmpfirst.first + tot.first + tmpsecond.first + tmp.first + tmp2.first;
            tmp2.first %= 2;
            if (tmp2.first != 0 || tmp2.second != 'j'){
                output<<"NO\n";
            }
            else output<<"YES\n";
        }
   //     output<<answer<<"\n";
    }
    
    
    return 0;
}
