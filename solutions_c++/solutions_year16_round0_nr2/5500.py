#include <iostream>
#include <string>





using namespace std;
 




int main()
 {
    int t, j;
    string N;
    long int noo;
    long int kkkkkk;
    cin>>t;
 
    for(int i = 1;i<=t;++i)
    {
        cin>>N;
        kkkkkk = 0;
        noo = 0;
        while(noo < N.size()){
 
            noo = 0;
 
            if(N[0] == '-'){
                N[0] = '+';
                ++noo;
                j = 1;
                while(j<N.size() && (N[j] == '-')){
                    N[j] = '+';
                    ++noo;
                    ++j;
                }
                ++kkkkkk;
 
            }else{
                N[0] = '-';
                ++noo;
                j = 1;
                while(j<N.size() && (N[j] == '+')){
                    N[j] = '-';
                    ++noo;
                    ++j;
                }
                if(noo < N.size())
                    ++kkkkkk;
            }
        }
        cout<<"Case #"<<i<<": "<<kkkkkk<<endl;
    }
    return 0;
}