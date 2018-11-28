#include <iostream>
#include <bits/stdc++.h>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <memory.h>
#include <cassert>
using namespace std;

int main()
{
    freopen ("A-large.in", "r", stdin);
	freopen ("myfile.txt","w",stdout);

    long long n,temp;
    long long visited ;
     int t ;
    scanf("%d",&t);
    for(int a=1;a<=t;a++){
        visited=0;
        cin>>n;
        temp=n;
        int j=2;
        do{

                visited=1<<(n%10)|visited;

            n=n/10;
            if(n==0&&visited!=1023){
                n=temp*j++;

            }

        }while(n!=0&&visited!=1023);
        bool flag=false;
        for(int i=0;i<10;i++){
            int t=(1<<i)&visited;
            if(t==0){
                flag=true;
            }

        }

        printf("Case #%d: ",a);
        if(flag){
            printf("INSOMNIA\n");
        }else{
            cout<<(j-1)*temp<<endl;
        }

    }

    return 0;
}
