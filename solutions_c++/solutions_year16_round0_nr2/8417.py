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

int t, end, cnt, start, k;
string st, dest;

int main(){
//freopen("input.txt", "r", stdin);
//freopen("/home/str/Downloads/B-large.in", "r", stdin);
//freopen("output.txt", "w", stdout);
ios_base::sync_with_stdio(0);
cin.tie(0);

cin>>t;
while(t--)
{
    cin>>st;
    cnt = 0, ++k;
    end = st.size()-1;
    while(st[end] == '+')
        st.erase(st.begin()+end), --end;
    end = st.size();
    dest  = "";
    for(int i = 0; i < end; i++)
        dest += '+';
    while(st != dest)
    {
        start = 0;
        if(st[start] == '-')
        {
            while(st[start] == '-')
                st[start] = '+', ++start;
            ++cnt;
        }
        else
        {
            while(st[start] == '+')
                st[start] = '-', ++start;
            ++cnt;
        }
    }
    cout<<"Case #"<<k<<": "<<cnt<<endl;
}

return 0;}
