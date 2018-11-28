#include <iostream>

using namespace std;

int main()
{
    int T,t;
    string aud;
    cin>>T;
    for(int t=0;t<T;t++){
        int smax, stand, invite=0,temp;
        cin>>smax;
        int a[smax+1];
        cin>>aud;
        for(int i=0;i<=smax;i++){
            a[i]=(int)(aud.at(i)-48);
        }
        stand=a[0];
        for(int i=1;i<=smax;i++){
            if(stand>=i){
                    stand+=a[i];
            }
            else{
                temp=i-stand;
                invite+=temp;
                stand+=temp;
                stand+=a[i];
            }
        }
        cout<<"case #"<<t+1<<": "<<invite<<endl;
    }
    return 0;
}
