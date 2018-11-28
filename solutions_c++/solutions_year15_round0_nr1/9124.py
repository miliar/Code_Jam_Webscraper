#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>

using namespace std;

int main() {
    int test;
    cin>>test;
    int k=1;
    while(test--)
    {
	string str;
        int size,tmp=0,ret=0;
        cin>>size;
        cin>>str;
        for(int j=0;j<str.size();j++)
        {
            if(tmp<j)
            {
                ret+=j-tmp;
                tmp+=j-tmp;
            }
            tmp+=str[j]-48;
        }
        cout<<"Case #"<<k<<": "<<ret<<endl;
	k++;
    }
}
