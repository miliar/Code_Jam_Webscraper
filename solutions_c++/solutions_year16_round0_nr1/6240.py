#include<iostream>

using namespace std;

int main(){
freopen("jam1in.txt","r",stdin);
freopen("jam1out.txt","w",stdout);
int t;
cin>>t;
for(int z=0;z<t;z++){
    int n;
    cin>>n;
    int arr[10];
    for(int i=0;i<10;i++){
        arr[i]=0;
    }
    int k=0;
    if(n==0){
        cout<<"Case #"<<z+1<<": INSOMNIA"<<endl;
    }
    else{
        int s=0;
        while(k!=10){
            s++;
            int f=s*n;
            while(f!=0){
                if(arr[f%10]==0){
                    arr[f%10]=1;
                    k++;
                }
                f/=10;
            }
        }
        cout<<"Case #"<<z+1<<": "<<s*n<<endl;
    }
}
}
