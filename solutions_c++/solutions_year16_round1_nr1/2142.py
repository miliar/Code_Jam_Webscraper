//DEEPAK AHIRE
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <cassert>
#include <climits>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <fstream>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define abs(x) ((x) > 0 ? (x) : -(x))
#define FOREACH(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
typedef long long int LL;
#define INF 1000001

#define IF 1000000000000000L


vector<char> func(string s)
{
    vector <char> v;
    int i;
    v.clear();
    for(i=0;i<s.size();i++)
    {
        if(v.empty())
            v.push_back(s.at(i));
        else if(s.at(i) >= v.at(0))
            v.insert(v.begin(),s.at(i));
        else
            v.push_back(s.at(i));
    }

    //cout<<"ijtiojbog";

    return v;
}
int main()
{
    string s;
    LL t;
    int c=1;
    ofstream myfile;
    myfile.open ("3.txt");
    vector<char> s1;
    cin>>t;
    while(t--)
    {
        cin>>s;
       myfile<<"Case #"<<c++<<": ";
        s1 = func(s);
        for (vector<char>::iterator it=s1.begin(); it<s1.end(); it++)
        {
            myfile<<*it;
        }
        myfile<<endl;
    }
    return 0;
}
