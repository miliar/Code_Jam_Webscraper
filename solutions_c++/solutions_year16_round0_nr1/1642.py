#include<bits/stdc++.h>

using namespace std;

typedef long long llong;
void get_digits(llong x,set <llong> &s) {
    while(x) {
        if(s.find(x%10)==s.end())
            s.insert(x%10);
        x/=10;
    }
}
int main() {

    freopen("C:\\Users\\Saurabh\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Saurabh\\Desktop\\out.txt","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--) {
        llong n,i,c=0;
        cin>>n;
        llong x=n;
        set <llong> s;
        while(c<1000001 && s.size()<10) {
            get_digits(x,s);
            x+=n;
            c++;
        }
        cout<<"Case #"<<cas++<<": ";
        if(c==1000001)
            cout<<"INSOMNIA\n";
        else
            cout<<x-n<<endl;
    }

    return 0;
}
