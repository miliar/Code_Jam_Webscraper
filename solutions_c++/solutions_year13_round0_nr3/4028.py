#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <complex>
#include <list>
#include <functional>
#include <utility>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;

#define READ freopen("input.txt", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)
#define PI acos(-1)
#define F(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define C cout<<
#define E <<endl

typedef vector<long long> vi;

template <class T> inline bool isPwr2(T x){return (x != 0) && ((x & (x - 1)) == 0);}
template <class T> inline double D2R(T x){return (PI*x)/180;}

int main()
{
    READ;
    WRITE;
    vi ans;
    ans.push_back(1);
    ans.push_back(2);
    ans.push_back(3);
    ans.push_back(11);
    ans.push_back(22);
    ans.push_back(101);
    ans.push_back(111);
    ans.push_back(121);
    ans.push_back(202);
    ans.push_back(212);
    ans.push_back(1001);
    ans.push_back(1111);
    ans.push_back(2002);
    ans.push_back(10001);
    ans.push_back(10101);
    ans.push_back(10201);
    ans.push_back(11011);
    ans.push_back(11111);
    ans.push_back(11211);
    ans.push_back(20002);
    ans.push_back(20102);
    ans.push_back(100001);
    ans.push_back(101101);
    ans.push_back(110011);
    ans.push_back(111111);
    ans.push_back(200002);
    ans.push_back(1000001);
    ans.push_back(1001001);
    ans.push_back(1002001);
    ans.push_back(1010101);
    ans.push_back(1011101);
    ans.push_back(1012101);
    ans.push_back(1100011);
    ans.push_back(1101011);
    ans.push_back(1102011);
    ans.push_back(1110111);
    ans.push_back(1111111);
    ans.push_back(2000002);
    ans.push_back(2001002);
    ans.push_back(10000001);
    ans.push_back(10011001);
    ans.push_back(10100101);
    ans.push_back(10111101);
    ans.push_back(11000011);
    ans.push_back(11011011);
    ans.push_back(11100111);
    ans.push_back(11111111);
    ans.push_back(20000002);



    int tc=1,N;
    cin>>N;
    long long a,b;
    while(N--)
    {
        cin>>a>>b;
        int cnt=0;
        F(i,0,ans.size()-1)
            if((ans[i]*ans[i])>=a&&(ans[i]*ans[i])<=b) cnt++;

        cout<<"Case #"<<tc++<<": "<<cnt<<endl;


    }




    return 0;
}
