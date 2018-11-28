#include<iostream>

using namespace std;

int main()
{
    int i,j,t,f,s,c,ans,n,num=0;
    int a[5],b[5];

    cin>>t;

    while(t--) {

        c=ans=0;num++;
        cin>>f;
        for(i=1;i<=4;i++) {
            for(j=1;j<=4;j++) {
                cin>>n;
                if(i==f)
                    a[j] = n;
            }
        }
        cin>>s;
        for(i=1;i<=4;i++) {
            for(j=1;j<=4;j++) {
                cin>>n;
                if(i==s)
                    b[j] = n;
            }
        }
        for(i=1;i<=4;i++) {
            for(j=1;j<=4;j++) {
                if(a[i]==b[j]) {
                    c++;
                    ans = a[i];
                }
            }
        }
        if(c==1)
            cout<<"Case #"<<num<<": "<<ans<<endl;
        else if(c>1)
            cout<<"Case #"<<num<<": "<<"Bad magician!"<<endl;
        else if(c==0)
            cout<<"Case #"<<num<<": "<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
