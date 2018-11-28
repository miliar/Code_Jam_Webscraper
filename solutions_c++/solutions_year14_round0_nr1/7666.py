#include <vector>
#include <list>
#include <map>
#include <math.h>
#include <cmath>
#include <set>
#include <queue>
#include <deque>
#include <string>
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
#include <string.h>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int F=1;F<=t;F++)
    {
        cout<<"Case #"<<F<<": ";
        int row;
        int arr[17]={0};
        cin>>row;
        for(int f=0;f<4;f++)
            for(int f1=0;f1<4;f1++)
            {
                int x;
                cin>>x;
                if(f+1==row)
                    arr[x]++;
            }
        cin>>row;
        for(int f=0;f<4;f++)
            for(int f1=0;f1<4;f1++)
            {
                int x;
                cin>>x;
                if(f+1==row)
                    arr[x]++;
            }
        int two,twos=0;
        for(int f=0;f<17;f++)
            if(arr[f]==2)
                two=f,twos++;
        if(twos==1)
            cout<<two<<endl;
        else if(twos>1)
            cout<<"Bad magician!"<<endl;
        else
            cout<<"Volunteer cheated!"<<endl;
    }
}
