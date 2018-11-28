#include <bits/stdc++.h>
#define pb push_back
#define Long long long
using namespace std;
int l = 0;
int a[10];
void f(int n) {
while(n!=0) {
    if(a[n % 10] == 0)
    l ++;
    a[n % 10] = 1;
    n /= 10;
}
}
int main() {
   freopen("A-large.in" , "r", stdin);
   freopen("output.txt" , "w" , stdout);
   int n;
   int t;
   cin >> t;
   for(int i = 1; i <= t; i ++) {
        cout<<"Case #"<<i<<": ";
        cin >> n;
        if(n == 0) {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
   for(int i = 1; ; i ++) {

        f(i * n);
        if(l == 10) {
            cout<<i * n << endl;
            break;
        }

   }
   l = 0;
   memset(a , 0 , sizeof a);
   }
}
