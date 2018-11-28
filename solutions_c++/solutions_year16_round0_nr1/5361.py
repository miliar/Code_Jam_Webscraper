#include"iostream"
#include"vector"
using namespace std;
main(){
    int t,n;
    cin>>t;
    for(int i =1 ; i <= t; i++){
        cin >> n;
        cout<<"Case #"<<i<<": ";
        if(n == 0)
            cout<<"INSOMNIA"<<endl;
        else{
            int x = n, count = 1, follow=n,k;
            vector<int> myvector(9, -1);
            myvector[myvector.size()] = -1;
            bool val = true;
            while(val){
                if(n != 0){
                    k = 0;
                    int mod = n % 10;
                    myvector[mod] = mod;
                    for(int j = 0; j <= myvector.size(); j++){
                        if(myvector[j] == j)
                            k++;
                        else
                            break;
                    }
                    if(k == 10)
                        val = false;
                    n = n / 10;
                }
                else{
                    n = (++count)*x;
                    follow = n;
                    //x = n;
                }
            }
            cout<<follow<<endl;
        }
    }
}
