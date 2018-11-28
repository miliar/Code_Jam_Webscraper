#include <bits/stdc++.h>
using namespace std;
int T,N,arr[1000];
char a;
int counter,test,peop;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>T;
    test=T;
    while(T--)
    {
        cin>>N;
        for(int k=0;k<N+1;k++){
            cin>>a;
            arr[k]=a-'0';
        }
        if(arr[0]==0){
        counter+=1;
        peop+=1;
        peop+=arr[1];
        }
        else{
            peop+=arr[0];
            peop+=arr[1];}
        for(int k=2;k<N+1;k++)
        {
            if(arr[k]){
            if(k>peop){
            counter+=(k-peop);
            peop+=(arr[k]+counter);
            }
            else
                peop+=arr[k];
            }
        }
        cout<<"CASE #"<<test-T<<": "<<counter<<"\n";
             for(int l=0;l<8;l++)
                arr[l]=0;
            counter=0;
            peop=0;
    }
    return 0;
}
