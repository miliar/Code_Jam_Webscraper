#include<iostream>

using namespace std;

int solve(){
    int a,b,k;
    cin>>a>>b>>k;
    
    int *counters=new int[k];
    for(int i=0;i<k;i++){
        counters[i]=0;
    }

    for(int i=0;i<b;i++){
        for(int i2=0;i2<a;i2++){
            int res=i&i2;
            if(res<k){
                //cout<<"Y on "<<i<<" "<<i2<<endl;
                counters[res]++;
            }
        }
    }

    int total=0;
    for(int i=0;i<k;i++){
        total+=counters[i];
    }

    delete counters;

    return total;

}

int main(int argv,char** argc){

    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        cout<<"Case #"<<i+1<<": "<<solve()<<endl;
    }


    return 0;
}
