  /*
Aditya R

*/
using namespace std;
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<limits>
#include<cmath>
#include<map>
#define LLU long long unsigned int
#define LLD long long double
#define FOR(i,N) for(int i=0;i<(N);i++)

    int main()
    {
        int test,caseno=0 ;
        cin>>test;
        while(test--)
        {
            caseno++;
        int r ,t,d,i=0;
        cin>>r>>t ;
        while(1)
        {

            if((2*i*i)+i*((2*r)-1)>t)break ;
            i++;
        }
        cout<<"Case #"<<caseno<<": "<<i-1<<endl;
        }
    return 0 ;
    }
