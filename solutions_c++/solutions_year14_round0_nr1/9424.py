#include <iostream>
#include <cstdio>
using namespace std;
int n,k,l,a1,a2,a3,a4,otv;
int mas[16];
int main()
{   freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>n;
    //cout<<n;
    for(int i=0;i<n;i++){
        cin>>k;
        int j=0;
        while(j<4){
            cin>>a1>>a2>>a3>>a4;
            if ( (j+1)==k) { mas[a1]=i+1; mas[a2]=i+1; mas[a3]=i+1; mas[a4]=i+1; }
            j++;
        }
        cin>>k;
        j=0;l=0;
        while(j<4){
            cin>>a1>>a2>>a3>>a4;

            if ( (j+1)==k) {
                //cout<<a1<<" "<<a2<<" "<<a3<<" "<<a4<<endl;
                if (mas[a1]==i+1) {l++; otv=a1; }
                if (mas[a2]==i+1) {l++; otv=a2; }
                if (mas[a3]==i+1) {l++; otv=a3; }
                if (mas[a4]==i+1) {l++; otv=a4; }
            }
            j++;
        }
        //cout<<mas[5]<<otv<<endl;
        cout<<"Case #"<<i+1<<": ";
    if (l==0) cout<<"Volunteer cheated!"<<endl; else
            if(l==1) cout<<otv<<endl; else cout<<"Bad magician!"<<endl;
    l=0;otv=0;
    }
    return 0;
}
