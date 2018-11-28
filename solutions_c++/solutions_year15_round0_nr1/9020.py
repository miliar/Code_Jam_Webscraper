#include<iostream>
#include<string>
using namespace std;
int main(){
int ip=0,cs=0,cas,shy,t,smax;
string I;
cin>>t;
for(cas=1;cas<=t;cas++){
    cin>>smax>>I;
    cs=0;ip=0;
    for(shy=0;shy<=smax;shy++){
        if(cs>=shy){
        cs=cs+(I[shy]-'0');
        }
        else if( I[shy]-'0' > 0){
        ip=ip+ (shy-cs);
        cs=cs+(shy-cs);
        cs=cs+(I[shy]-'0');
        }
    }
    cout<<"Case #"<< cas<< ": "<<ip<<endl;
}

}
