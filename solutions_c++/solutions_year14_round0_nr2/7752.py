#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
int main(){
    int t;
    double c,f,x,p1,p2,p3;
    cin>>t;
  //  scanf("%d",&t);
    for(int i=0;i<t;i++){
        //scanf("%lf%lf%lf",&c,&f,&x);
       // printf("Case #%d: %.7lf",i+1,ile(0,c,x,f,0,2));
       // p1=4;
       // p3=x/2;
        cin>>c>>f>>x;
        p3=x/2;
        p1=2+f;
        p2=c/2;
        cout<<fixed;
        cout.precision(0);
        cout<<"Case #"<<i+1<<": ";
       // cout<<x/p1+p2<<endl;
        while(x/p1+p2<p3){
            p3=x/p1+p2;
            p2+=c/p1;
            p1+=f;
        }
        cout<<fixed;
        cout.precision(7);
        cout<<p3<<endl;;
    }
}
