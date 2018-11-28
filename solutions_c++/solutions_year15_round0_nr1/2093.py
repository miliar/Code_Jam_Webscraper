#include <iostream>
#include <string>
using namespace std;

main(){
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    int licznik=1;
    while(t--){
        int n;
        cin >> n;
        string s;
        cin >> s;
        int friends=0;
        int sum=0;
        for(int i=0;i<=n;i++){
            int num=s[i]-'0';
            if(sum<i){
                friends+=i-sum;
                sum+=i-sum;
            }
            sum+=num;
        }
        cout << "Case #"<< licznik << ": "<< friends << endl;
        licznik++;
    }
    return 0;
}
