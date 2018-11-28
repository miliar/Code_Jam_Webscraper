#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>
using namespace std;
int ispalin(int k)
{
    vector <int> vec;
    while (k)
        vec.push_back(k%10),
        k/=10;
    for (int i=0;i<vec.size()/2;i++)
        if (vec[i] != vec[vec.size()-1-i])
            return 0;
    return 1;
}
int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int t;
    cin>>t;
    for (int T=0;T<t;T++)
    {
        int a,b,cnt = 0;
        cin>>a>>b;
        for (int i=a;i<=b;i++)
        {
            int j = sqrt(i*1.0);
            if (i != j*j) continue;
            if (ispalin(i) && ispalin(j))
                cnt++;
        }
        cout<<"Case #"<<T+1<<": "<<cnt<<endl;
    }
    return 0;
}
