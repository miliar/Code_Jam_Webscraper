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

int num[10];
int alpha[26];

int main()
{

    string s;
    ofstream myfile;
    myfile.open ("1.txt");
     int c=1;
    LL t,i,r;
    cin>>t;
    while(t--)
    {
        cin>>s;
        memset(alpha,0,sizeof(alpha));
        memset(num,0,sizeof(num));
        for(i=0;i<s.length();i++)
        {
            alpha[s.at(i) - 65]++;
        }
        r = s.length();
        while(r)
        {

        ///2
        while(alpha['T'-65]>0 && alpha['W'-65]>0 && alpha['O'-65] >0)
        {
            num[2]++;
            //cout<<"222\n";
            alpha['T'-65]--;
            alpha['W'-65]--;
            alpha['O'-65]--;
                r--;
                r--;
                r--;

        }
        ///4
        while(alpha['F'-65]>0 && alpha['O'-65]>0 && alpha['U'-65] >0&& alpha['R'-65]>0)
        {
            num[4]++;
           //cout<<"444\n";
            alpha['F'-65]--;
            alpha['O'-65]--;
            alpha['U'-65]--;
            alpha['R'-65]--;
                r--;
                r--;
                r--;
                r--;


        }
        ///6
        while(alpha['S'-65]>0 && alpha['I'-65]>0 && alpha['X'-65] >0)
        {
            num[6]++;
            alpha['S'-65]--;
            alpha['I'-65]--;
            alpha['X'-65]--;
            //alpha['E'-65]--;r--;
           // cout<<"666\n";
            r--;
            r--;
            r--;
        }
        ///0
        while(alpha['Z'-65]>0 && alpha['E'-65]>0 && alpha['R'-65] >0&& alpha['O'-65]>0)
        {
           // cout<<"000000000000\n";
            num[0]++;
            alpha['Z'-65]--;r--;
            alpha['E'-65]--;r--;

            alpha['R'-65]--;
            r--;
            alpha['O'-65]--;
            r--;
        }
        ///G
        while(alpha['E'-65]>0 && alpha['I'-65]>0 && alpha['G'-65] >0&& alpha['H'-65]>0 && alpha['T'-65]>0)
        {
            num[8]++;
            //cout<<"888\n";
            alpha['E'-65]--;
            alpha['I'-65]--;
            alpha['G'-65]--;
            alpha['H'-65]--;
            alpha['T'-65]--;
                r--;
                r--;
                r--;r--;
                r--;


        }

        while(alpha['O'-65]>0 && alpha['N'-65]>0 && alpha['E'-65] >0)
        {

           //cout<<"111\n";
            num[1]++;
            alpha['O'-65]--;
            alpha['N'-65]--;
            alpha['E'-65]--;
            r--;r--;r--;
        }













        while(alpha['F'-65]>0 && alpha['I'-65]>0 && alpha['V'-65] >0&& alpha['E'-65]>0)
        {
            num[5]++;
            //cout<<"555\n";
            alpha['F'-65]--;
            alpha['I'-65]--;
            alpha['V'-65]--;
            alpha['E'-65]--;r--;
            r--;
                r--;
            r--;

        }


        while(alpha['N'-65]>1 && alpha['I'-65]>0 &&  alpha['E'-65]>0)
        {
            num[9]++;
            alpha['N'-65]-=2;
            alpha['I'-65]--;

            alpha['E'-65]--;
            r--;
            r--;
            r--;
            r--;

        }


        while(alpha['T'-65]>0 && alpha['H'-65]>0 && alpha['R'-65] >0&& alpha['E'-65]>1)
        {
            num[3]++;
          //  cout<<"333\n";
            alpha['T'-65]--;
            alpha['H'-65]--;
            alpha['R'-65]--;
            alpha['E'-65]-=2;r--;
            r--;
            r--;
            r--;
            r--;
        }

        while(alpha['S'-65]>0 && alpha['E'-65]>1 && alpha['V'-65] >0 && alpha['N'-65]>0)
        {
            //cout<<"777"<<endl;
            num[7]++;
            alpha['S'-65]--;
            alpha['E'-65]-=2;
            alpha['V'-65]--;
            alpha['N'-65]--;
            //cout<<"777\n";
            r--;
            r--;
            r--;
            r--;
            r--;

        }


    }
        myfile<<"Case #"<<c++<<": ";
        for(i=0;i<10;i++)
        {
            int y = num[i];
            while(y--)
                myfile<<i;
        }
        myfile<<endl;
    }
}
