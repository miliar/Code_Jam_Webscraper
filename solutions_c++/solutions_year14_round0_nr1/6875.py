using namespace std;

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <iomanip>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>

// CONSTANTS
#define INF (1<<31)-1
#define PI 3.14159265358979323846264338327950288419716939937510

// FUNCTIONS
#define MAX(x,y) (x)>(y)?(x):(y)
#define MIN(x,y) (x)<(y)?(x):(y)
// gcd(a,b){ return (b==0)?a:gcd(b,a%b); }
// lcm(a,b){ return a*b/gcd(a,b); }

typedef long long LL;
typedef long double LD;
typedef long long unsigned int LLU;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i=0,row1=0,row2=0;
    int arr1[4][4]={0},arr2[4][4]={0};
    int r1[4]={0},r2[4]={0};
    cin >> i;
    for(int l=0;l<i;l++)
    {
        int count = 0,num=0;
        row1=0,row2=0;
        arr1[4][4]={0},arr2[4][4]={0};
        r1[4]={0},r2[4]={0};
        cin>>row1;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                cin >> arr1[j][k];
            }
        }
        for(int j=0;j<4;j++){
            r1[j]=arr1[row1-1][j];
            //cout << r1[j] << endl;
        }
        //cout << endl;
        cin>>row2;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                cin >> arr2[j][k];
            }
        }
        for(int j=0;j<4;j++){
            r2[j]=arr2[row2-1][j];
          //  cout << r2[j] << endl;
        }
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                //cout<<"r1[j] = "<<r1[j]<<endl;
                //cout<<"r2[k] = "<<r2[k]<<endl;
            if(r1[j] == r2[k]){
                count++;
                num = r1[j];
            }
            }
        }
        if(count == 1)
        {
            cout << "Case #"<<(l+1)<<": "<<num<<endl;
        }
        else if(count == 0)
        {
            cout << "Case #"<<(l+1)<<": Volunteer cheated!"<<endl;
        }
        else if(count >1)
        {
            cout << "Case #"<<(l+1)<<": Bad magician!"<<endl;
        }
    }
    return 0;
}
