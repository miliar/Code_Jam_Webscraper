#include<iostream>
using namespace std;
int main()
{
    int t,A,B,j,k;
    cin>>t;
    for(j=0;j<t;++j)
    {
        cin>>A>>B; 
        k=0;
        if(A==1 && B>=1) ++k;
        if(A<=4 && B>=4) ++k;
        if(A<=9 && B>=9) ++k;
        if(A<=121 && B>=121) ++k;
        if(A<=484 && B>=484) ++k;
        cout<<"Case #"<<j+1<<": "<<k<<endl;
    }
    return 0;
}
