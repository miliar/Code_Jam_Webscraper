#include<iostream>
using namespace std;
/*long long power(int a, int b){
          int i;
          long long ans=1;
          for (i=0;i<b;i++) ans=ans*a;
          return ans;
}*/
int main(){
    /*long long x;
    int i,j,temp,counter,n;
    int k[200],c[200],s[200];
    cin>>n;
    for (i=0;i<n;i++){
        cin>>k[i];
        cin>>c[i];
        cin>>s[i];
    }
    for (i=0;i<n;i++){
        cout<<"Case #"<<i+1<<": ";
        temp=k[i]/c[i];
        if (k[i]%c[i]!=0) temp++;
        if (temp>s[i]){
           cout<<"IMPOSSIBLE"<<endl;
           continue;
        }
        counter=0;
        x=0;
        for (j=0;j<k[i];j++){
            x=x+j*power(j,counter);
            counter++;
            if (counter==c[i]){
               cout<<x+1;
               if (j!=k[i]-1) cout<<' ';
               x=0;
               counter=0;
            }
        }
        if (counter!=0) cout<<x+1;
        cout<<endl;
    }*/
    int n,i,j;
    cin>>n;
    int k[200],c[200],s[200];
    for (i=0;i<n;i++){
        cin>>k[i];
        cin>>c[i];
        cin>>s[i];
    }
    for (i=0;i<n;i++){
        cout<<"Case #"<<i+1<<": ";
        for (j=1;j<s[i];j++) cout<<j<<' ';
        cout<<s[i]<<endl;
    }
    //while (1);
}
