#include <iostream>

using namespace std;

int checkarray(int a[]);

int countsheep(long n,int tc){

    int arr[10]={0,0,0,0,0,0,0,0,0,0};
    int z,m,status;

    for(int i=1;i<=1000;i++){

        z=i*n;
        m=z;
        while(z!=0){
            arr[z%10]=1;
            z/=10;
        }

        status = checkarray(arr);

        if (status==1)
            break;

    }

    if(status==1)
        cout<<"Case #"<<++tc<<": "<<m<<endl;
    else if (status == 0)
        cout<<"Case #"<<++tc<<": "<<"INSOMNIA"<<endl;

    return 0;
}

int checkarray(int a[]){
    int g=1;
    for (int k=0;k<10;k++){
        if(a[k]==0)
            g=0;
    }
    return g;
}

int main()
{
    int tc;
    long n;
    cin>>tc;

    for(int j = 0;j<tc;j++){
        cin>>n;
        countsheep(n,j);
    }
    return 0;
}
