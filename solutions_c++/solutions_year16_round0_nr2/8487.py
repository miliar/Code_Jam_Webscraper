#include<bits/stdc++.h>
using namespace std;
int check(string str){
    for(int i=0;i<str.size();i++){
        if(str[i]=='-')
            return 0;
    }
return 1;
}
void flip(string &str,int i,int j){
    for(int k=i;k<=j;k++){
        if(str[k]=='+')
            str[k]='-';
            else
                str[k]='+';
    }

}
int fun(string str){
    int ans=0;
    char ch=str[0];
    int i=0;
    int j=0;
    while(!check(str)){
            while(j<str.size() and ch==str[j])
                j++;

            flip(str,i,j-1);
                ans++;
                ch=str[0];
    }
return ans;
}
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int tt;
    cin>>tt;
    for(int test=1;test<=tt;test++){
            cout<<"Case #"<<test<<": ";
            string str;
            cin>>str;
            int ans=0;
                ans=fun(str);


            cout<<ans<<endl;
    }


}
