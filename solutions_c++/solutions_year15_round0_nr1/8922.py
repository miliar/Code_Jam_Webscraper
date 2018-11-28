#include <bits/stdc++.h>

using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
freopen ( "input.txt","rt",stdin ); //Read Input From File
freopen ("output.txt","wt",stdout); //Put Output In File
#endif
//---------------------------
    int T,Smax;
    string Persons;
    cin>>T;
    for(int Ti = 0; Ti<T; ++Ti){
        cin>>Smax>>Persons;

        int Frinds = 0;
        int sum = 0;
        int n = Smax+1;

        for(int k =0; k<n; ++k){
            if(sum+Frinds<k)
                Frinds = k-sum;

            sum += Persons[k]-'0';
        }
        cout<<"Case #"<<Ti+1<<": "<<Frinds<<endl;
    }

//---------------------------
return 0;
}
