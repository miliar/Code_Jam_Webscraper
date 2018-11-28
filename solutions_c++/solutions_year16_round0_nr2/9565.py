#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <iomanip>
#include <list>
#include <ctime>
#include <memory.h>
#include <bitset>
#include <climits>
#include<cstdio>

using namespace std;

string lund, chut;

int main(){
//freopen("input.txt", "r", stdin);
//freopen("output.txt", "w", stdout);
int t,k=0;
cin>>t;

while(t--)
{
    cin>>lund;
    int jhatt_k_baal = 0;
    k++;
    int right_breast = lund.size()-1;
    while(lund[right_breast] == '+')
        lund.erase(lund.begin()+right_breast), --right_breast;
    right_breast = lund.size();
    chut  = "";
    for(int i = 0; i < right_breast; i++)
        chut += '+';
    while(lund != chut)
    {
        int left_breast = 0;
        if(lund[left_breast] == '+')
            while(lund[left_breast] == '+')
                lund[left_breast] = '-', ++left_breast;
        else
            while(lund[left_breast] == '-')
                lund[left_breast] = '+', ++left_breast;

        ++jhatt_k_baal;
    }
    cout<<"Case #"<<k<<": "<<jhatt_k_baal<<endl;
}

return 0;}
