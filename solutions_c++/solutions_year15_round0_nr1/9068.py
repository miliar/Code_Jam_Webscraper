#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

int main(int argc, char *args[]) {
    int N;
    freopen("small.in","rt",stdin);
    freopen("small.out","wt",stdout);

    cin>>N;

    for(int o=1; o<=N; ++o) {

        int max_shyness;
        string s;
        cin>>max_shyness>>s;

        int so_far = s[0] - 48;
        int invited = 0;

        for(int i=1; i<=max_shyness; ++i) {
            if(so_far + invited < i) {
                invited += (i - (so_far + invited));
                so_far += (s[i] - 48);

            }
            else {
                so_far += (s[i] - 48);
            }
        }
      cout<<"Case #"<<o<<": "<<invited<<endl;

    }
    return 0;
}
