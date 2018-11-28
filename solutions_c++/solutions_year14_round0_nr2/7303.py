#include "iostream"
#include "cstdio"

using namespace std;

int main(){
    int t;
    long double c,f,x,tot,r;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        //scanf("%Lf %Lf %Lf",&c,&f,&x);
        cin>>c>>f>>x;
        //cout<<c<<"\t"<<x<<"\t"<<f<<endl;
        tot=0;
        r=2;
        printf("Case #%d: ",i+1);
        if(x/r<c/r+x/(r+f))
            printf("%.7llf\n",x/r);
        else{
            while(x/r>=c/r+x/(r+f)){
                //cout<<"Entering here\n";
                tot+=c/r;
                r+=f;
            }
            tot+=x/r;
            //cout<<tot<<endl;
            printf("%.7llf\n",tot);
        }
    }
    return 0;
}
