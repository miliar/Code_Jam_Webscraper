#include <iostream>
#include <string>
using namespace std;
bool checkDigits(bool digits[10]){
        for (int i=0;i<10;i++){
                if (digits[i]==false){
                        return false;
                }
        }
        return true;
}
int main(){
        int T;
        cin>>T;
        int tests[T];
        for (int i=0;i<T;i++){
                cin>>tests[i];
        }
        for (int i=0;i<T;i++){
                bool digits[10] = {false,false,false,false,false,false,false,false,false,false};
                int N = tests[i];
                cout<<"Case #"<<(i+1)<<": ";
                if (N==0){
                        cout<<"INSOMNIA"<<endl;
                }
                else{
                        int multiplier=0;
                        do{
                                multiplier++;
                                int temp=N*multiplier;
                                while (temp>0){
                                        int digit = temp%10;
                                        digits[digit] = true;
                                        temp = temp/10;
                                }
                        }while(!checkDigits(digits));
                        cout<<(N*multiplier)<<endl;
                }
        }
}
