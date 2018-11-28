#if 1

#include <math.h>
#include <iostream>
#include <deque>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <string>
#include <ctime>
#include <vector>
using namespace std;
typedef long double LD; 
typedef long long LL; 

#define PROBLEM "sub-1"
int a[4][4], b[4][4];

int main()
{
    freopen(PROBLEM ".in","r",stdin); freopen(PROBLEM ".out","w",stdout);
    //freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
    time_t START = clock();

    int t, c, d;
    scanf ("%d", &t);
    for (int i=0;i<t;i++)
    {
          scanf ("%d", &c);
          c--;
          for (int j=0; j<4; j++)
             for (int k=0; k<4; k++) 
                 scanf ("%d",&a[j][k]);
          scanf ("%d", &d);
           d--;       
           for (int j=0; j<4; j++)
             for (int k=0; k<4; k++) 
                 scanf ("%d",&b[j][k]);
            set <int> z, x;
            vector <int> to(10);
            for (int j=0; j<4; j++)
            {
                 z.insert (a[c][j]);
                 x.insert (b[d][j]);           
            }  
           auto it=set_intersection(x.begin(), x.end(), z.begin(), z.end(), to.begin());
           to.resize(it-to.begin());
           set<int> ans(to.begin(), to.end());
           cout <<"Case #"<<i+1<< ": ";     
           if (ans.size()==1)
               cout<<*ans.begin()<<endl; 
           else if (ans.size()==0)
               cout <<"Volunteer cheated!"<<endl;
           else
                cout <<"Bad magician!"<<endl; 
    }    
    

    time_t FINISH = clock(); 
    cerr << "Time = " << double(FINISH - START) / CLOCKS_PER_SEC << endl;
    return 0;
}
#endif