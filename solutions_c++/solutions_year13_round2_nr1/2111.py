#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> a;
int n;
int minop;
void search(int size, int op, int index)
{
    if(index == n)
    {
        minop = min(minop,op);
        return;
    }
    if(size <= a[index])
    {
        if(size != 1)
        {
            search(size*2-1,op+1,index);
        }
        search(size,op+1,index+1);
    }
    else
    {
        search(size+a[index],op,index+1);
    }
}
int main()
{
    int t;
    int begin;
    cin>>t;
    for(int i = 0; i < t; i ++)
    {
        a.clear();
        minop = 100000000;
        cin>>begin>>n;
        int temp;
        for(int k = 0; k < n; k++)
        {
            cin>>temp;
            a.push_back(temp);
        }
        sort(a.begin(),a.end());
        search(begin,0,0);
        cout<<"Case #"<<i+1<<": "<<minop<<""<<endl;
    }
    return 0;
}
