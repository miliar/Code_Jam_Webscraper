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
int a[35];
long long s[10];

int main(){
    int t,kase=0,n,j,k;
    cin>>t;
    while (t--) {
        kase++;
        cin>>n>>k;
        int time=1;
        long long sum=0,temp;
        memset(a, 0, sizeof(a));
        a[n-1]=1;
        a[0]=1;
        printf("Case #1:\n");
        for (int i=0; i<pow(2, n-2); i++) {
            sum+=2;
            temp=sum;
            for (int j=n-2; j>0; j--) {
                if (temp>=pow(2, j)) {
                    temp-=pow(2, j);
                    a[j]=1;
                } else a[j]=0;
            }
            int flag=0;
            temp+=1+pow(2, n-1);
            memset(s, 0, sizeof(s));
            for (int i=2; i<=10; i++) {
                flag=0;
                temp=0;
                for (int j=0; j<n; j++) {
                    if (a[j]==1)
                        temp+=pow(i, j);
                }
                if (temp%2==0) {
                    flag=1;
                    s[i]=2;
                } else {
                    for (int j=3; j<=sqrt(temp); j+=2) {
                        if (temp%j==0) {
                            flag=1;
                            s[i]=j;
                            break;
                        }
                    }
                }
                if (flag==0) {
                    break;
                }
            }
            if (flag==1) {
                for (int i=n-1; i>=0; i--) {
                    cout<<a[i];
                }
                cout<<" ";
                for (int i=2; i<=10; i++) {
                    cout<<s[i]<<" ";
                }
                cout<<endl;
                time++;
            }
            if (time>k) {
                break;
            }
        }
    }
    return 0;
    
}
