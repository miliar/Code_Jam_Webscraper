#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

int T,N;
vector<int> A,B;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++) {
        cin>>N;
        A.clear();
        B.clear();
        for(int i=1;i<=(2*N-1);i++) {
            for(int j=0;j<N;j++) {
                int tmp;
                cin>>tmp;
                A.push_back(tmp);
            }
        }
        sort(A.begin(),A.end());
        cout<<"Case #"<<ca<<":";
        int last = 0, cnt = 0;
        for(int i=0;i<A.size();i++) {
            if(A[i] != last) {
                if(cnt % 2 == 1) {
                    B.push_back(last);
                }
                cnt = 1;
                last = A[i];
            } else cnt++;
        }
        if(cnt % 2 == 1) {
            B.push_back(last);
        }
        for(int i=0;i<B.size();i++) {
            cout<<" "<<B[i];
        }
        cout<<endl;
    }

    return 0;
}
