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
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define abs(x) ((x) > 0 ? (x) : -(x))
#include <fstream>
#define FOREACH(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
typedef long long int LL;
#define INF 1000001

#define IF 1000000000000000L

int arr[11];

void func(int n)
{
    while(n)
    {
        arr[n%10]=1;
        n/=10;
    }
   // for(int i=0;i<=9;i++)
     //   cout<<arr[i]<<" ";
    //cout<<endl;
}
int check(int * arr)
{
    int i=0;
    for(i=0;i<=9;i++)
        {
            if(arr[i]!=1)
                break;
        }
        if(i<=9)
            return -1;
        else
            return 1;
}
int main()
{
    LL t,n,k,c=1;
    ofstream myfile;
    myfile.open ("2.txt");
    //myfile << "Writing this to a file.\n";
    //myfile.close();
    cin>>t;
    while(t--)
    {
        cin>>n;


        if(n==0)
        {myfile<<"Case #"<<c++<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        k=1;
        memset(arr,0,sizeof(arr));
        while(1)
        {
            if(check(arr) == -1)
                func(n*k++);
            else
            {myfile<<"Case #"<<c++<<": "<<n*(k-1)<<endl;break;}
        }
    }
    myfile.close();
    return 0;
}
