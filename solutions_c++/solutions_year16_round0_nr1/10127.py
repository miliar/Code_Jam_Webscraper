#include<iostream>
#include<algorithm>
#include<vector>
#include <set>
#define f(a) for(i=0;i<a;i++)
using namespace std;

int main(){
    int t,n,k,i,j,temp,rem;
    long long hash[1000001]={0};
    
    set<int> s;
    scanf("%d",&t);
    f(t){
        j=2;
     scanf("%d",&n);
        temp = n;
        k=n;
        if(n==0) printf("Case #%d: INSOMNIA\n",(i+1));
        else{
            if(hash[n]==0){
            while(s.size()<10){
                while(temp){
                    rem = temp%10;
                    s.insert(rem);
                    temp/=10;
                    if(s.size()==10) break;
                }
                if(s.size()==10) break;
                temp=n*j;
                k=temp;
               // cout<<"--"<<temp<<endl;
                j++;
            }
                hash[n]=k;
                printf("Case #%d: %d\n",(i+1),(k));
            }else{
                printf("Case #%d: %lld\n",(i+1),hash[n]);
            }
            
        }
        s.clear();
    }
    
    return 0;
}