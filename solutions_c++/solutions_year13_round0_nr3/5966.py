#include <iostream>
#include <cmath>
using namespace std;

int power(int a, int b)
{
     int c=a;
     for (int n=b; n>1; n--) c*=a;
     return c;
}

bool isPalindrome(int a){
     int c = 0;
     if(a <10 ){
          return true;
     }else{
           int temp = a;
           while((a/10) > 0){
               c++;
               a = a/10;
           }  
           int tot = c;
           if(c  > 0 ) {
                 if( ( (temp / power(10,c)) % 10 ) == (temp % 10 ) ){                               
                          c = c - 2;
                          temp = temp/10;
                 }else{
                       return false;
                 }
           }
     }return true;
}
           
int main(){
    int num,a,b;
    cin >> num;
    int sqr_a,sqr_b;
    int t =1;
    while( t <=num){
           int count = 0;
           cin >> a >> b;
           sqr_a = (int)sqrt(float(a));
           sqr_b = (int)sqrt(float(b));
           for(int i= sqr_a; i <= sqr_b; i++){
                    if( isPalindrome(i) && power(i,2)>= a && isPalindrome( power(i,2) ) ){
                                          count++;
                    }
           }
           cout << "Case #" << t++ << ": " << count << "\n";
    }
    //system("pause");
    return 0;
}
                                          
