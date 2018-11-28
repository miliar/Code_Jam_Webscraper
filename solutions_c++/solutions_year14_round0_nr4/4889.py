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
#include <string.h>
using namespace std;

double a[1010],b[1010];

int main()
{
    
    int T,N;
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        cin>>N;
        for(int i=0;i<N;i++)
            cin>>a[i];
        
        for(int i=0;i<N;i++)
            cin>>b[i];
        
        sort(a,a+N);
        sort(b,b+N);
        int k=0,kk=0;
        int j=N-1;
        for(int i=N-1;i>=0 && j>=0;i--)
            while(j>=0){
                if(b[i]>a[j]){
                    j--;
                    k++;
                    break;
                }
                j--;
            }
        
        j=N-1;
        for(int i=N-1;i>=0 && j>=0;i--)
            while(j>=0){
                if(a[i]>b[j]){
                    j--;
                    kk++;
                    break;
                }
                j--;
            }
        
        
        cout<<"Case #"<<cas<<": "<<kk<<" "<<N-k<<endl;
    }
}

