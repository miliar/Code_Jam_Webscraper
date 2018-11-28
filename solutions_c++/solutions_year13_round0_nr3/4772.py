#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
using namespace std;
bool ispalin(int i){
    char A[15];
    sprintf(A,"%d",i);
    //cout<<A<<endl;
    string val(A);
    string d=val;
    reverse(d.begin(),d.end());
    if(val==d)
        return 1;
    return 0;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("Csmall","w",stdout);
    int t,k=0;
    scanf("%d",&t);
    while(t--){
        k++;
        int A,B;
        scanf("%d %d",&A,&B);
        int count=0;
        int m=(int)ceil(sqrt(B/1.0));
        int p=floor(sqrt(A/1.0));
        for(int i=p;i<=m;i++){
            if(ispalin(i*i)&&ispalin(i)&&i*i<=B&&i*i>=A){
                //cout<<i<<" "<<i*i<<endl;
                count++;
            }

        }
    printf("Case #%d: %d\n",k,count);
    }
	return 0;
}
