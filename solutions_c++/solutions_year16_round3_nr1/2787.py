#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct item
{
    int number;
    char party;
};

bool order(item a, item b)
{
    return a.number>b.number;
}

int solve(int position)
{
    int n;
    item aux;
    int majority;
    vector<item> v;
    cin>>n;
    int total = 0;
    for(int i=0;i<n;i++)
    {
        cin>>aux.number;
        aux.party = 'A' + i;
        v.push_back(aux);
        total+=aux.number;
    }

    cout<<"Case #"<<position<<":";

    while(total>0)
    {
        std::sort(v.begin(), v.end(), order);
        majority = (total-2)/2+1;
        if(v[0].number>0 && v[1].number>0 && (n==2 || v[2].number<majority))
        {
            cout<<" "<<v[0].party<<v[1].party;
            v[0].number--;
            v[1].number--;
            total-=2;
        }
        else
        {
            if(v[0].number>=2 && v[1].number<majority)
            {
                cout<<" "<<v[0].party<<v[0].party;
                v[0].number-=2;
                total-=2;
            }
            else
            {
                cout<<" "<<v[0].party;
                v[0].number--;
                total--;
            }
        }
    }
    cout<<endl;
}

int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
        solve(i+1);
    return 0;
}
