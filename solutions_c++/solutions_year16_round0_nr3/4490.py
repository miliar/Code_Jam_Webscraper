#include<iostream>
#include<cmath>
using namespace std;

long long preobrazuvane(long long a,long long base){
    long long res=0,k=1;
    while(a!=0){
        res=res+(a%2)*k;
        a/=2;
        k*=base;
    }
    return res;
}

long long divisiorOf(long long a){
    long long root=sqrt(a),i;
    root++;
    for(i=2;i<=root;i++){
        if(a%i==0){
            return i;
        }
    }
    return 0;
}

void print(long long a){
    bool in2[64];
    long long i=0;
    while(a!=0){
        in2[i]=a%2;
        a/=2;
        i++;
        //cout<<"a";
    }
    for(i--;i>=0;i--){
        cout<<in2[i];
    }
}

int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    long long test,lenght,numberOf=0,counter=0,jc,divisiors[20],i;
    cin>>test>>lenght>>numberOf;
    cout<<"Case #1:\n";
    for(jc=(1<<lenght-1)+1;counter<numberOf;jc++){
        if(jc%2==0)
            jc++;
        bool isItAnsw=true;
        for(i=2;i<11;i++){
            //cout<<preobrazuvane(jc,i)<<" ";
            divisiors[i]=divisiorOf(preobrazuvane(jc,i));
            if(divisiors[i]==0){
                i=11;
                isItAnsw=false;
            }
        }
        //cout<<endl;
        if(isItAnsw){
            print(jc);
            cout<<" ";
            for(i=2;i<11;i++){
                cout<<divisiors[i];
                if(i+1<11)
                    cout<<" ";
            }
            cout<<"\n";
            counter++;
        }
    }

    return 0;
}
