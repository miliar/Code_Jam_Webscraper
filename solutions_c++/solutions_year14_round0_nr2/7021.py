#include<iostream>
#include<algorithm>
#include<iomanip>
using namespace std;
int main(){
    int T;
    freopen("D:\\a.txt","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    cin>>T;
    for (int t=1;t<=T;t++){
        double c,f,x;
        cin>>c>>f>>x;
        double besttime=x/2.0;
        double cnt=0.0;
        for (int farm=1;farm<100000;farm++){
            cnt+=c/(2.0+(farm-1)*f);
            besttime=min(besttime,cnt+x/(2.0+farm*f));
        }
        //cout<<fixed<<setprecision(7)<<besttime<<endl;
        int farm=(int)(x/c-2.0/f);
        double now=0.0;
        farm=max(0,farm);
        for (int i=0;i<farm;i++)
            now+=c/(2.0+i*f);
        now+=x/(2.0+farm*f);
        if (fabs(now-besttime)>1e-7) cout<<"error"<<endl;
        cout<<"Case #"<<t<<": ";
        cout<<fixed<<setprecision(7)<<now<<endl;
    }
}
