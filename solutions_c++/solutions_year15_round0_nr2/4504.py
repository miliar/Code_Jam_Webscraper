#include <iostream>
#include <algorithm>

using namespace std;

int getMax(int a[], int n){
    int maximum=a[0];
    for(int i=1;i<n;i++){
        if(a[i]>maximum) maximum=a[i];
    }
    return maximum;
}

int divby2(int x){
    if(x%2==0)
        return x/2;
    else
        return x/2 + 1;
}

int main()
{
   int T,t;
   cin>>T;
   for(t=0;t<T;t++){
    int nd;
    cin>>nd;
    int D[nd],iD[nd],overhead;
    for(int i=0;i<nd;i++){
        cin>>D[i];
    }
    sort(D, D+nd, std::greater<int>());
    int maxTime=D[0];

     //1 Split 9
    for(int i=0;i<nd;i++){
        iD[i]=D[i];
    }
    overhead=0;
    for(int i=0;i<nd;i++){
        if(D[i]<4) break;
        iD[i]=divby2(D[i]);
        overhead+=1;
        if(getMax(iD,nd)+overhead<maxTime)
            maxTime=getMax(iD,nd)+overhead;
    }

    //2 Split 9
    for(int i=0;i<nd;i++){
        iD[i]=D[i];
    }
    overhead=0;
    for(int i=0;i<nd;i++){
        if(D[i]<4) break;
        if(D[i]==9){
            iD[i]=3;
            overhead+=2;
        }
        else{
            iD[i]=divby2(D[i]);
            overhead+=1;
        }
        if(getMax(iD,nd)+overhead<maxTime)
            maxTime=getMax(iD,nd)+overhead;
    }
    cout<<"Case #"<<t+1<<": "<<maxTime<<endl;

   }
   return 0;
}
