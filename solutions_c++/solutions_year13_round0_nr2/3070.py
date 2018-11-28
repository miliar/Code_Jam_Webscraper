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
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
    string output[3]={"","YES","NO"};
    cin>>n;
    for(i=1;i<=n;i++)
    {
        int x,y,m[101][101],j,k,flag=1;
        cin>>x>>y;
        for(j=1;j<=x;j++){
            for(k=1;k<=y;k++){
                cin>>m[j][k];
            }
        }
        for(j=1;j<=x;j++){
            for(k=1;k<=y;k++){
                int flagx=0,flagy=0,a,b,height;
                height=m[j][k];
                for(a=1;a<=y;a++){if(m[j][a]>height){flagx=1;}}
                for(b=1;b<=x;b++){if(m[b][k]>height){flagy=1;}}
                if(flagx==1&&flagy==1){flag=2;break;}
            }
        }
        cout<<"Case #"<<i<<": "<<output[flag]<<endl;
    }



    return 0;
}
   