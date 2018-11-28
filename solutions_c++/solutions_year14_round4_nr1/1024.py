#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iterator>
#include <cctype>

using namespace std;

//T N X S


int main(){
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        int N,X;
        cin >> N >> X;
        deque <int> vS;
        for(int i=0;i<N;i++){
            int a;
            cin >> a;
            vS.push_back(a);
        }
        sort(vS.begin(),vS.end());
        int cnt=0;
        while(vS.size()>1){
            if(vS.front()+vS.back()<=X){
                cnt++;
                vS.erase(vS.begin());
                vS.erase(vS.end()-1);
            }
            else{
                vS.erase(vS.end()-1);
                cnt++;            }
        }
        cnt+=vS.size();
        cout << "Case #" << t+1 << ": " << cnt << endl;
    }
    
    return 0;
}

