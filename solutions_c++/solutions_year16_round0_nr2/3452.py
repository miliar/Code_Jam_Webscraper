#include<iostream>
using namespace std;
int main(){
    int n;
    int i,j,end;
    string s,temps;
    string a[200];
    char current;
    int ans;
    cin>>n;
    for (i=0;i<n;i++) {
        temps="";
        cin>>s;
        end=s.length()-1;
        while (s[end]=='+') end--;
        for (j=0;j<=end;j++) temps=temps+s[j];
        a[i]=temps;
    }
    for (i=0;i<n;i++){
        cout<<"Case #"<<i+1<<": ";
        if (a[i]=="") {
           cout<<0<<endl;
           continue;
        }
        end=a[i].length();
        ans=1;
        current=a[i][0];
        for (j=1;j<end;j++){
            if (a[i][j]!=current){
               current=a[i][j];
               ans++;
            }
        }
        cout<<ans<<endl;
    }
    //while (1);
}
