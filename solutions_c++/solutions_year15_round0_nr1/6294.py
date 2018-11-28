#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int main()
{


      freopen("input.txt","r",stdin);
	    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for(int i = 1; i <=T; i++) {
            string input;
            long long standing=0;
        long long n, smax[2000], ans=0;
        cin>>n>>input;
        for(int q=0; q<input.length(); q++){
            smax[q]=(unsigned int)input[q]-'0';
          //  cout<<smax[q]<<" ";
        }
      //  for(int k=0; k <n+1; k++)
        //    cin>>smax[k];
for(int z=0; z < n+1; z++){
    if (standing >=z)
        standing+=smax[z];
    else {
        ans+=(z-standing);
        standing+=smax[z]+(z-standing);
    }

}


        cout<<"Case #"<<i<<": "<<ans<<endl;
    }

    return 0;
}
