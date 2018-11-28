#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    long long tests,t;
    cin>>tests;
    for(t=1;t<=tests;t++){
        long long a,x,y,broi[3000],max_n=3000,n;

        for(x=0;x<max_n;x++){
            broi[x]=0;
        }

        cin>>n;

        for(x=0;x<n*2-1;x++){
            for(y=0;y<n;y++){
                cin>>a;
                broi[a]++;
            }
        }

        cout<<"Case #"<<t<<": ";
        y=0;
        for(x=0;x<max_n;x++){
            if(broi[x]%2!=0){
                cout<<x;
                if(y+1<n)
                    cout<<" ";
                y++;
            }
        }
        cout<<endl;
    }
    return 0;
}
