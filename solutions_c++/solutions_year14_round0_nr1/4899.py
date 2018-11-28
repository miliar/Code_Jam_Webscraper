#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int arr[17];

int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int index,icase=0;
    scanf("%d",&index);
    while(index--){
        int t1,t2;
        cin>>t1;
        for (int i=0;i<16;i++){
            int t;
            cin>>t;
            arr[t]=i/4;
        }
        cin>>t2;
        for (int i=0;i<16;i++){
            int t;
            cin>>t;
            arr[t]+=(i/4)*4;
        }
        int res,flag=0;
        for (int i=1;i<=16;i++)
            if (t1-5+t2*4==arr[i]){
                res=i;
                flag++;
            }
        res;
        printf("Case #%d: ",++icase);
        if (flag==0)puts("Volunteer cheated!");
        else if (flag>1)puts("Bad magician!");
        else cout<<res<<endl;
    }
    return 0;
}
