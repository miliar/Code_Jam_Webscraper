#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <bitset>


typedef float real;


static int
getMinBiggerThan(const std::vector<real>& v, real e, const std::bitset<1000>& used)
{
    int min = -1;
    real mv = 5.;
    for (int i = 0; i < v.size(); ++i) {
        if (used[i] == 0) {
            if (e < v[i] && (v[i] < mv || mv > 1.)) {
                min = i;
                mv = v[i];
            }
        }
    }
    
    return min;
}

static int
getLowestNotUsed(const std::bitset<1000>& used)
{
    for (int i = 0; i < 1000; ++i)
        if (used[i] == 0) return i;
    
    return -1;
}

static void
playNormal(const std::vector<real>& n, const std::vector<real>& k, int& result)
{
    // we need to check wich is the first element where ken wins noami
    std::bitset<1000> used;
    used.reset();
    int count = 0;
    for (int i = 0; i < n.size(); ++i) {
        int index = getMinBiggerThan(k, n[i], used);
        if (index < 0) {
            used[getLowestNotUsed(used)] = 1;
            ++count;
        } else {
            used[index] = 1;
        }
    }
    
    // now we know that noami will win at least count matches
    result = count;    
}

static void
playDeceitful(const std::vector<real>& n, const std::vector<real>& k, int& result)
{
    // we need to look for the element in noami that is bigger than ken, all the
    // others we can lie
    int count = 0;
    int nb = 0, ne = n.size() -1;
    int kb = 0, ke = k.size() - 1;
    while (nb <= ne && kb <= ke) {
        if (n[ne] > k[ke]) {
            ++count;
            ke--;
            ne--;
        } else {
            nb++;
            ke--;
        }
    }
    result = count;
}



int main(int argc, char** args)
{
    int N;
    std::vector<real> n,k;
    std::cin >> N;
    for (int i = 0; i < N; ++i) {
        n.clear();
        k.clear();
        int y,z;
        
        // read the blocks
        int count;
        std::cin >> count;
        for (int j = 0; j < count; ++j) {
            real val;
            std::cin >> val;
            n.push_back(val);
        }
        for (int j = 0; j < count; ++j) {
            real val;
            std::cin >> val;
            k.push_back(val);
        }
        
        // sort the values
        std::sort(n.begin(), n.end());
        std::sort(k.begin(), k.end());
        
        playDeceitful(n,k,y);
        playNormal(n,k,z);
        
        std::cout << "Case #" << i+1 << ": " << y << " " << z << std::endl;
    }    
    return 0;
}
