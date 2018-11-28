#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

#define D(x) cout << #x " is " << x << endl

using namespace std;

int main(){
    int cases; cin >> cases;
    for(int i=1; i<= cases; i++){
        double c,x,f,realf; 
        cin >> c >> f >> x;
        realf = 2;
        double aux1=0, aux2=0, save=0;
        aux1 = x/realf; aux2 = (c/realf)+(x/(realf+f));
        save = (c/realf); realf += f;
        while(aux1 > aux2){
            aux1 = aux2;
            aux2 = save + (c/realf) + (x/(realf+f));
            save += (c/realf);
            realf += f;
        }
        printf("Case #%d: %.7f\n", i, aux1);    
    }
	return 0;
}
