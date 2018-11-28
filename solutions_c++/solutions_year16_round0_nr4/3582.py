#include <iostream>
#include <fstream>
using namespace std;
long long n, T;
bool a[10];
int main()
{    freopen("D-small-attempt0.in", "r", stdin);
     freopen("out.txt", "w", stdout);
    cin>>T;
    int l = 1;
    while(T){
            bool flag = true;
        T--;
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<l<<": ";
        l++;
        for(int i=1; i<s; i++){
            cout<<i<<" ";
        }
        cout<<s<<endl;

    }

    return 0;
}
