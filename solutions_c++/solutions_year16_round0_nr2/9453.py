#include <iostream>
#include <cstdio>
using namespace std;

string __str, frozen_onion;

int main(){
//freopen("input.txt", "r", stdin);
//freopen("output.txt", "w", stdout);
int t;
scanf("%d",&t);

int inc=1;
while(inc<=t)
{
    cin>>__str;
    int counter = 0;
    int right = __str.size()-1;
    while(__str[right] == '+')
        __str.erase(__str.begin()+right), --right;

    right = __str.size();
    frozen_onion = "";

    for(int i = 0; i < right; i++)
        frozen_onion += "+";

    while(__str != frozen_onion)
    {
        int left = 0;
        if(__str[left] == '-')
        {
            while(__str[left] == '-')
                __str[left] = '+', ++left;
            ++counter;
        }
        else
        {
            while(__str[left] == '+')
                __str[left] = '-', ++left;
            ++counter;
        }

    }

    cout<<"Case #"<<inc<<": "<<counter<<endl;
    inc++;
}

return 0;}
