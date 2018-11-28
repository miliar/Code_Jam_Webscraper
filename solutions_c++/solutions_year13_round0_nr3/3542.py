#include<string.h>
#include<map>
#include<iostream>
#include<utility>
#include<math.h>
using namespace std;

bool isPalindrome(int num) {
    char arr[120];
    sprintf(arr,"%d", num);
    int len= strlen(arr);
    int i=0,j=len-1;
    for(; i<j;i++, j--) {
        if(arr[i]!=arr[j])
            return false;
    }
    return true;
}

int isSquare(int num) {
    int sqrtV = (int)sqrt(num);
    if(sqrtV*sqrtV == num)
        return sqrtV;
    return 0;
}

void process(int A, int B) {
    int count =0;
    int sqrtV;
    
    for(int i =A; i<=B;i++) {
        if(isPalindrome(i) && (sqrtV=isSquare(i)) && isPalindrome(sqrtV)) {
            count++;
        }
    }
    cout<<count;
}

int main() {
    int T;
    int A, B;
    cin>>T;
    int count=0;
    while(T>0) {
        cin>>A;cin>>B;
        count++;
        T--;
        cout<<"Case #"<<count<<": ";
        process(A, B);
        cout<<"\n";
    }
    return 0;
}
