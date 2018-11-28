#include <iostream>
#include <math.h>
using namespace std;

int palindrome(int number){
    int i=0,idx,cek=0;
    float digits[20];
    while(number>=1){
        digits[i]=number%10;
        number/=10;
        i++;
    }
    for(idx=0;idx<(ceil((i+1)/2));idx++){
        //cout<<digits[idx]<<" "<<digits[i-idx-1]<<endl;    
        if(digits[idx] == digits[i-idx-1]){
            cek++;
        }
    }
    if((ceil((i+1)/2)) == cek) return 1; else return 0;
}

int main(){
    int T,A,x,B,idx,result;
    
    cin >> T;
    for(idx=1;idx<=T;idx++){
        result=0;
        cin >> A >> B;
        for(x=A;x<=B;x++){
            float root=sqrt(x);
            int fair=palindrome(x);
            int fairrt=palindrome((int)root);
            float cl=ceil(root);
            float fl=floor(root);
            if(fair && fairrt && (cl==root && fl==root)) {
                result++;
                //cout<<root<<" "<<cl<<" "<<fl<<" "<<fair<<endl;
            }
        }
        cout << "Case #" << idx << ": " << result << endl;
    }
}
