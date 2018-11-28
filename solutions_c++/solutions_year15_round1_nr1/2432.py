#include <iostream>
using namespace std;

short int tab[1001];
int main()
{
ios_base::sync_with_stdio(0);
int t,n,maximum,tmp,odp1,odp2;
cin>>t;
for(int i=0;i<t;i++){
    cin>>n;
    for(int j=0;j<n;j++){
        cin>>tab[j];
    }
    maximum=0;
    tmp=0;
    odp1=0;
    odp2=0;
    for(int j=0;j<n-1;j++){
            tmp=tab[j]-tab[j+1];
        if(tmp>maximum)
            maximum=tmp;
        if(tmp>0)
            odp1+=tmp;
    }
    for(int j=0;j<n-1;j++){
    if(tab[j]>=maximum)
        odp2+=maximum;
    else
        odp2+=tab[j];
    }
    cout<<"Case #"<<i+1<<": "<<odp1<<" "<<odp2<<"\n";
}
}
