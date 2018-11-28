#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;
long long int isprime(long long int t){
    for(long long int i=2;i<=sqrt(t);i++){
        if(t%i==0){
            return i;
        }
    }
    return 0;
}
class myvector:public vector<int>{
public:
    void operator++(){
        this->at(1)+=1;
        for(int j=0;j<this->size();j++){
            if(this->at(j)>=2){
                this->at(j)%=2;
                this->at(j+1)+=1;
            }
        }
    }
    long long int check(int i){
        long long int count=0;
        for(int j=0;j<this->size();j++){
            count+=this->at(j)*pow(i,j);
        }
        return isprime(count);
    }
};

int main(){
   // freopen("out.txt", "w", stdout);
    int t;
    cin>>t;
    int n,j;
    cin>>n>>j;
    printf("Case #1:\n");
    if(1){
        myvector a;
        a.push_back(1);
        for(int i=0;i<n-2;i++){
            a.push_back(0);
        }
        a.push_back(1);
        while(j--){
            vector<long long int> in;
            int flag=1;
            for(int c=2;c<=10;c++){
                long long int temp=a.check(c);
                if(temp==0){
                    flag=0;
                    break;
                }
                else{
                    in.push_back(temp);
                }
            }
            if(flag==0){
                ++a;
                j++;
                continue;
            }
            else{
                for(int i=(int)a.size()-1;i>=0;i--){
                    cout<<a[i];
                }
                for(int i=0;i<in.size();i++){
                    cout<<" "<<in[i];
                }
                cout<<endl;
                ++a;
            }
        }
    }
}