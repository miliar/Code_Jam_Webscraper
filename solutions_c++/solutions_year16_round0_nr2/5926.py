#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <fstream>
#include <stack>
#include <cmath>
#include <queue>
#include <map>
#include <set>
using namespace std;

string n;
int a[105];

int main(){
    int t,kase=0;
    cin>>t;
    while (t--) {
        kase++;
        cin>>n;
        int len=n.length();
        for (int i=0; i<len; i++) {
            if (n[i]=='+') a[i]=1;
            else a[i]=-1;
        }
        int sum=0,flag=0,sig=0;
        for (int i=0; i<len-1; i++) {
            if (a[i]==a[i+1]) {
                a[i]=0;
                sig++;
            }
        }
        for (int i=0; i<len; i++) {
            if (a[i]!=0) {
                if (flag==0) {
                    flag=1;
                } else {
                    if (a[i]==-1) {
                        sum+=2;
                    }
                }
            }
        }
        for (int i=0; i<len; i++) {
            if (a[i]!=0) {
                if (a[i]==-1) {
                    sum++;
                }
                break;
            }
        }
        printf("Case #%d: %d\n",kase,sum);
    }
    return 0;
    
}
