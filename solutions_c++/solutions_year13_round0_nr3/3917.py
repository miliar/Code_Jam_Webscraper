#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

int isPalindrome(long long int x){
    int i,j,k,len,res;
    vector<int> cislo;
    len = 0;
    j=1;
    for(i=0;j<=x;i++){
        j*=10;
    }
    len=i;
    //printf("len = %d\n",len);
    k=x;
    
    for(i=0;i<len;i++){
        cislo.push_back(k%10);
        k/=10;
    }
    
    k=1;
    for(i=0;i<len;i++){
        if(cislo[i]!=cislo[len-1-i]){
            k=0;
            break;
        }
    }
    
    return k;    
}

int main(){
    int i,j,k,l,m,n,o,p;
    double d,e;
    
    /*for(i=0;i<150;i++){
        printf("%d: %d\n",i,isPalindrome(i));
    }*/
    
    scanf("%d",&n);
    
    for(l=0;l<n;l++){
        scanf("%d",&o);
        scanf("%d",&p);
        k=0;
        for(i=o;i<=p;i++){
            if(isPalindrome(i)){
                d = (double) i;
                e = sqrt(d);
                m = (int) e;
                if((m*m==i)&&isPalindrome(m)){
                    //printf("%d %d\n",i,m);
                    k++;
                }
            }
        }
        printf("Case #%d: %d\n",l+1,k);
    }
    
    return 0;
}
