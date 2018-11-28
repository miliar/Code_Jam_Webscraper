#include <cmath>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <functional>
using namespace std;

int main() {
    int ntc;
    cin>>ntc;
    for (int tc=1; tc<=ntc; ++tc) {
        string t;
        vector<int> v(10);
        cin>>t;
        while (t.find('Z')!=string::npos) {
            ++v[0];
            t.erase(t.begin()+t.find('Z')); t.erase(t.begin()+t.find('E')); t.erase(t.begin()+t.find('R')); t.erase(t.begin()+t.find('O'));
        }
        while (t.find('G')!=string::npos) {
            ++v[8];
            t.erase(t.begin()+t.find('E')); t.erase(t.begin()+t.find('I')); t.erase(t.begin()+t.find('G')); t.erase(t.begin()+t.find('H')); t.erase(t.begin()+t.find('T'));
        }
        while (t.find('W')!=string::npos) {
            ++v[2];
            t.erase(t.begin()+t.find('T')); t.erase(t.begin()+t.find('W')); t.erase(t.begin()+t.find('O'));
        }
        while (t.find('X')!=string::npos) {
            ++v[6];
            t.erase(t.begin()+t.find('S')); t.erase(t.begin()+t.find('I')); t.erase(t.begin()+t.find('X'));
        }
        while (t.find('U')!=string::npos) {
            ++v[4];
            t.erase(t.begin()+t.find('F')); t.erase(t.begin()+t.find('O')); t.erase(t.begin()+t.find('U')); t.erase(t.begin()+t.find('R'));
        }
        while (t.find('F')!=string::npos) {
            ++v[5];
            t.erase(t.begin()+t.find('F')); t.erase(t.begin()+t.find('I')); t.erase(t.begin()+t.find('V')); t.erase(t.begin()+t.find('E'));
        }
        while (t.find('V')!=string::npos) {
            ++v[7];
            t.erase(t.begin()+t.find('S')); t.erase(t.begin()+t.find('E')); t.erase(t.begin()+t.find('V')); t.erase(t.begin()+t.find('E')); t.erase(t.begin()+t.find('N'));
        }
        while (t.find('H')!=string::npos) {
            ++v[3];
            t.erase(t.begin()+t.find('T')); t.erase(t.begin()+t.find('H')); t.erase(t.begin()+t.find('R')); t.erase(t.begin()+t.find('E')); t.erase(t.begin()+t.find('E'));
        }
        while (t.find('O')!=string::npos) {
            ++v[1];
            t.erase(t.begin()+t.find('O')); t.erase(t.begin()+t.find('N')); t.erase(t.begin()+t.find('E'));
        }
        while (t.find('I')!=string::npos) {
            ++v[9];
            t.erase(t.begin()+t.find('N')); t.erase(t.begin()+t.find('I')); t.erase(t.begin()+t.find('N')); t.erase(t.begin()+t.find('E'));
        }
       
        ostringstream oss;
        for (int i=0; i<v.size(); ++i) {
            while (v[i]!=0) {
                oss<<i;
                --v[i];
            }
        }
        cout<<"Case #"<<tc<<": "<<oss.str()<<'\n';
    }
    return 0;
}