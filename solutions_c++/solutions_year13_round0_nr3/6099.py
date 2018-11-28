#include<iostream>
#include<algorithm>
#include<vector>
#include<stdio.h>
#include<cmath>

using namespace std;

bool ispalin(int num){
    int temp=num,tt=0;
    while(temp){
        int r=temp%10;
        tt=tt*10+r;
        temp/=10;
    }
    if(tt==num)
        return true;
    return false;
}

bool sqrchk(int num){

    int aa = sqrt(num);
    if(aa*aa==num && ispalin(aa))
        return true;

    return false;
}
/*int bsearch(long long num){

    int low=0, high = arr.size(),mid;

    while(low<=high){
        mid=(low+high)/2;

        if(arr[mid]*arr[mid]<num && arr[mid+1]*arr[mid+1]
           )
    }
}*/

int result(){

        int a,b,count=0;
        cin>>a>>b;

        int i;
        for(i=a;i<=b;i++){
            if(ispalin(i) && sqrchk(i))
                count++;
                //cout<<i<<"\n" , arr.push_back(i);
        }

        return count;
        //bsearch(b)-bsearch(a);

}
int main(){

    freopen("out_small.txt","w",stdout);
    freopen("C-small-attempt0.in","r",stdin);
    int N,M,T;
    cin>>T;

    for(int tt=1;tt<=T;tt++){

        cout<<"Case #"<<tt<<": "<<result()<<endl;

    }
    return 0;
}
