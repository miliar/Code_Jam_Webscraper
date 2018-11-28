//counting sheep

#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    long T,N;


  //  freopen("A-large.in","r",stdin);
   // freopen("a.out","w",stdout);

    cin>>T;

    for(long i = 1;i<=T;i++){

        int a[10] ,m;
        for(int l=0;l<10;l++)
        {
            a[l] = -1;
        }
        cin>>N;

        int c = 0;
        long j = N;
        long k;

        //N not 0
        if (j!=0)
        while(true){
            k = j;

            //iterate over k to find the digits
            while(k){
                m = k%10;
                if(a[m] == -1){
                    c++;
                    a[m] = 0;
                }
                k = k/10;

            }

            if(c == 10) break;

            j = j+N;
        }
        if(j!=0) cout <<"Case #"<<i<<": "<<j<<endl;
        else cout <<"Case #"<<i<<": INSOMNIA"<<endl;

    }


    return 0;
}
