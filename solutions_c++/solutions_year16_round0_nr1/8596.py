#include<iostream>
#include<map>
using namespace std;
int check=0;
map<int,int> l;
int count(int N){
    int x;
    if(N==0) return 0 ;
    while(N!=0){
        x = N%10;
        N = N/10;
        if(l[x]==0){
            l[x] = 1;
            check++;
        }
    }
    return 1;


}

int main(){
    int t,counter=1;

    for(cin>>t;t--;){
        for(int k=0;k<10;k++){
            l[k] = 0;
        }
        int N,i=1,c;
        cin>>N;
        while(check!=10){
            c = count(i*N);
            if(c==0){
                c = 2;
                break;
            }
            i++;
        }
        if(c==2) cout<<"Case #"<<counter<<": INSOMNIA\n";
        else cout<<"Case #"<<counter<<": "<<(i-1)*N<<endl;
        counter++;
        check = 0;
        c = 5;

        }










    return 0;
}
