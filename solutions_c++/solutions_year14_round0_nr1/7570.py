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
#include <iterator>
using namespace std;

#define READ freopen("input.txt", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)
#define PI acos(-1)
#define F(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define C cout<<
#define E <<endl

typedef vector<int> vi;

template <class T> inline bool isPwr2(T x){return (x != 0) && ((x & (x - 1)) == 0);}
template <class T> inline double D2R(T x){return (PI*x)/180;}
vector<string> &split(const string &s, char delim, vector<string> &elems) { stringstream ss(s); string item; while (getline(ss, item, delim)){if (!item.empty()) elems.push_back(item);}return elems;}


int main()
{

    READ;
    WRITE;

    int n,arr1[4][4],arr2[4][4],rslt[20],t1,t2,tc=1;
    cin>>n;

    while(n--)
    {
        cin>>t1;

        //cout<<t1<<endl;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        cin>>arr1[i][j];

        cin>>t2;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        cin>>arr2[i][j];

        memset(rslt,0,sizeof(rslt));
        //for(int i=0;i<20;i++) rslt[i]=0;

        //cout<<arr1[t1-1][0]<<endl;

        //cout<<t1-1<<endl;

        for(int i=0;i<4;i++)
        {
            //cout<<"in loop"<<endl;

            //cout<<arr1[t1-1][i]<<endl;

            rslt[arr1[t1-1][i]]++;
            rslt[arr2[t2-1][i]]++;
        }

        //cout<<"out loop"<<endl;

        int ans=-1,cnt=0;

        for(int i=0;i<20;i++)
        {
            if(rslt[i]==2) {cnt++;ans=i;}
        }

        if(cnt==0)
        cout<<"Case #"<<tc++<<": Volunteer cheated!"<<endl;
        else if(cnt>1)
        cout<<"Case #"<<tc++<<": Bad magician!"<<endl;
        else
        cout<<"Case #"<<tc++<<": "<<ans<<endl;
    }





    return 0;
}
