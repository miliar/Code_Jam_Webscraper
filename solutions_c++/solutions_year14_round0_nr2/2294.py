#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    double t,c,f,x;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>c>>f>>x;
        //printf("%.07f %.07f %.07f",c,f,x);
        double pre,current;
        int j=1;
        current=c/2+x/(f+2);
        pre=x/2;
        while(current<pre){
            pre=current;
            current-=x/(2+f*j);
            current+=c/(2+f*j);
            j++;
            current+=x/(2+f*j);
            //cout<<j<<"  ";
        }
        printf("Case #%d: %.07f\n",i,pre);

}
}
