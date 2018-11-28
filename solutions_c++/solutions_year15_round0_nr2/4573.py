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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
set<int> sett;
void fun(vector<int> vec,int count)
{



    // Mafeeesh Fayda ~o~ /o/ \o\


    sort(vec.begin(), vec.end());
    int x=vec[vec.size()-1];
    if(x==1)
    {
        sett.insert(count+x);
        return;
    }

	vector <int> vec2=vec;
        for(int i=vec2.size()-1; i>=0; i--)
        {
            if(vec2[i])
                vec2[i]--;
        }
        fun(vec2,count+1);
    for(int lol=1; lol<=x/2; lol++)
    {

		int j;
        vector <int> vec3=vec;
        sort(vec3.begin(), vec3.end());
        j=vec3.size();
        j--;
		int a7eh=0;
        while(vec3[j]==x)
        {
            vec3[j]-=lol;
            vec3.push_back(lol);
            sort(vec3.begin(), vec3.end());
            j=vec3.size()-1;
            a7eh++;
        }
        fun(vec3,count+a7eh);
    }
}
int main()
{
    ifstream in;
    in.open("B-small-attempt10.in");
    ofstream out;
    out.open("sub-2.out");
    int t;
    in>>t;
    for(int j=0; j<t; j++)
    {
        sett.clear();
        int d;
        in>>d;
        int max=0;
        vector<int> vec;
        for(int i=0; i<d; i++)
        {
            int x;
            in>>x;
            vec.push_back(x);
        }
        fun(vec,0);
        out<<"Case #"<<j+1<<": "<<*sett.begin()<<endl;
    }
    return 0;
}
// END KAWIGIEDIT TESTING
