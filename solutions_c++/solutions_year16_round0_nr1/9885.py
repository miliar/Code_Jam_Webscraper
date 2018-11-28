#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <iomanip>
#include <list>
#include <ctime>
#include <memory.h>
#include <bitset>
#include <climits>

#define F first
#define S second
#define endl "\n"
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define pi 3.141592653589793
#define y1 zjdfshnvoavaofobiopj
using namespace std;

unsigned long long t, n, calc, start, k;
int found[12];
bool error;

void count(long long x)
{
    while(x)
        found[x%10] = 1, x /= 10;
}

int main(){
//freopen("input.txt", "r", stdin);
//freopen("/home/str/Downloads/A-large.in", "r", stdin);
//freopen("output.txt", "w", stdout);
ios_base::sync_with_stdio(0);
cin.tie(0);

cin>>t;
while(t--)
{
    memset(found, 0, sizeof found);
    ++k;
    cin>>n;
    start = 1;
    error = true;
    if(!n)
    {
        cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
        continue;
    }
    while(error)
    {
        error = false;
        calc = n*start;
        count(calc);
        for(int i = 0; i < 10; i++)
            if(found[i] == 0)
                error = true;
        ++start;
    }
    cout<<"Case #"<<k<<": "<<calc<<endl;
}

return 0;}
