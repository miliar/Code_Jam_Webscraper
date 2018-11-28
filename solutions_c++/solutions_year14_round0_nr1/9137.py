#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

int T;

int main()
{
    //create the streams
    ifstream fin("C:/A-small-attempt3.in");
    ofstream cout("C:/response.txt");

    // create the arrays
    int ans1(0),ans2(0);
    int  arr1[4][4], arr2[4][4];

    //Hold all the  inputs
    fin>>T;
    for(int x(1); x<=T; x++)
    {
        fin>>ans1;
        for(int j=0; j<4; j++)
            for(int i=0; i<4;i++) fin>>arr1[j][i];
        fin>>ans2;
        for(int j=0; j<4; j++)
            for(int i=0; i<4;i++) fin>>arr2[j][i];


    // compare the 2 rows:
    int res(0), ans(0);
    for(int i=0; i<4; i++)
    {
        if(arr1[ans1 -1][i] == arr2[ans2-1][i])
        {
            res++;
            ans=arr1[ans1-1][i];
        }
    }

    // construct the solutions:
    if(res==1) cout<<"Case #"<<x<<": "<<ans<<endl;
    else if(res>1) cout<<"Case #"<<x<<": "<<"Bad magician!"<<endl;
    else if(res==0) cout<<"Case #"<<x<<": "<<"Volunteer cheated!" <<endl;
    }

	return 0;
}
