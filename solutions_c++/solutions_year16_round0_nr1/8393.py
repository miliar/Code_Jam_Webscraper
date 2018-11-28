#include<bits/stdc++.h>
using namespace std;

int fun(int *arr){
    for(int i=0;i<10;i++){
        if(arr[i]==0)
            return 0;
    }
    return 1;

}
void check(int num,int *arr,int *ans){

    while(num){
            int r=num%10;
            num/=10;
            arr[r]=1;
    }
    if(fun(arr))
        *ans=1;


}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int tt;
    cin>>tt;
    for(int test=1;test<=tt;test++){
        cout<<"Case #"<<test<<": ";
        int num;
        cin>>num;

        int N=num;
        int arr[10]={0};
        int ans=0;
        int i=1;

        while(N!=0 and num<10e11  and num>=0 and ans==0){
            check(num,arr,&ans);
                if(ans)
                    break;
                    else{
                        num=N*i;
                        ++i;
                    }
        }
        if(ans==1)
            cout<<num<<endl;
            else if(N==0)
                cout<<"INSOMNIA"<<endl;
                else
                    cout<<"INSOMNIA"<<endl;


    }

}
