#include <iostream>
#include<set>
using namespace std;




int main()
{
    int T =0;
    long long N=0;
    set<int> numbersParsed;

    cin>>T;

    for(int i=1;i<=T;i++){
        cin>>N;

       unsigned long long result =0;
       unsigned long long j=0;
       unsigned long long ans=0;
       numbersParsed.clear();

       while(numbersParsed.size()<10){

            j++;

            result = j*N;
            ans = result;
            if(result==0){
                cout<<"Case #"<<i<<": INSOMNIA\n";
                break;
            }

             while(result>0)
            {

                numbersParsed.insert(result%10);
                result /=10;

            }
        }
        if(numbersParsed.size()==10)
            cout<<"Case #"<<i<<": "<<ans<<"\n";

    }

    return 0;
}
