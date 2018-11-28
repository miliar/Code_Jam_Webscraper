#include<iostream>
#include<vector>
#include<cstdio>

using namespace std;

main()
{
    freopen("input.txt","r",stdin);
    freopen("largeAout.txt","w",stdout);
    int T,c=1;
    int l,v[10]= {0},k;
    bool done=false;
    long long N,M=0;

    cin>>T;

    while(c<=T) {

        fill_n(v,10,0);
        l=0;
        cin>>N;
        cout<<"Case #"<<c<<": ";
        c++;
        done=false;
        if(N==0)
            cout<<"INSOMNIA\n";
        else {
            while(done!=true) {
                l++;
                M=N*l;
                do {
                    k=M%10;
                    if(v[k]==0)
                    v[k]++;
                    M=M/10;
                } while(M);
                for(int i=0; i<10; i++) {
                    if(v[i]==0) {
                        done=false;
                        break;
                    } else done=true;
                }
            }
            cout<<N*l<<"\n";
        }
    }
}
