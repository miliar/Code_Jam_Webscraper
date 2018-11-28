#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int main(){
    int n,i;
    //freopen("1.in","r",stdin);
    //freopen("1.out","w",stdout);
    //string output[3]={"","YES","NO"};
    int m[6]={0,1,4,9,121,484};
    cin>>n;
    for(i=1;i<=n;i++)
    {
        int a,b,j,sum=0;
        cin>>a>>b;
        for(j=1;j<=6;j++){
            if(m[j]>=a && m[j]<=b){sum++;}
        }

        cout<<"Case #"<<i<<": "<<sum<<endl;
    }
    return 0;
}
   