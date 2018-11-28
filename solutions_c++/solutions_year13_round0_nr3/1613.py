#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <string>
#include <cstring>

using namespace std;
int pwn[10];
vector <long long> vi;

bool ispalin(long long num){
    long long n = num;
    long long rev = 0, dig;
    while (num > 0)
    {
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
    }
    if(n==rev)return true;
    return false;
}

void rec(long long n, int len){
    if(len>8)return;
    long long tn;
    for(int i=0;i<=9;i++){
        tn = ( ( pwn[len]*i + n ) * 10 ) + i;
        rec(tn,len+2);
    }
    n*=n;
    if(n && ispalin(n))vi.push_back(n);
    return;
}

void doit(){
    long long a,b;
    int ret=0;
    cin>>a>>b;
    for(int i=0;i<vi.size();i++)
    if(vi[i]>=a && vi[i]<=b){
       ret++;
    }
    cout<<ret<<endl;
    return;
}
int main(){
    int tc;
    long long a=1;
    for(int i=0;i<10;i++){
        pwn[i]=a;
        a=a*10;
    }
    for(int i=0;i<=9;i++){rec(i,1);rec(i*11,2);}
    sort(vi.begin(),vi.end());
    cin>>tc;
    for(int i=1;i<=tc;i++){
      cout<<"Case #"<<i<<": ";
      doit();
    }
    return 0;
}

