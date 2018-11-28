#include<iostream>
using namespace std;
int main(){
    int T,case_count=0;
    int a,sum,fri;
    char b[2000];
    cin >> T;
    while((T--) > 0){
        case_count++;
        fri=sum=0;
        cin >> a;
        cin >> b;
        for(int i=0;i<=a;i++){
            if(b[i]!='0'){
            if(sum >= i)
                sum += ( b[i] - '0');
            else{
            //    cout << i << "  " << sum << endl;
                fri += ( i - sum );
                sum += ( fri+ (b[i]-'0'));
            }}
        }
        cout << "Case #"<<case_count << ": " <<fri << endl;
    }
    return 0;
}
