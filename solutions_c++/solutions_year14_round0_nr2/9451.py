#include <iostream>
#include <cstdio>

#define time tim

using namespace std;
double t,c,f,x,time,r;
int temp;
int main()
{   freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>c>>f>>x;
        r=2;time=0;temp=1;
        while (temp){
            if ((x/r)>((c/r)+(x/(r+f))) ) {
                time+=c/r;
                r+=f;
            } else
            {
            temp=0;
            time+=x/r;
            }
        }
    cout<<"Case #"<<i+1<<": ";
    printf("%.7lf",time);
    cout<<endl;
    }
    return 0;
}
