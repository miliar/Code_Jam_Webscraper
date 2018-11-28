#include<bits/stdc++.h>
#include<fstream>
using namespace std;

int main()
{
    freopen("C:\\Users\\Anick\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Anick\\Desktop\\out.txt","w",stdout);

    int t;
    int tc=1;

    cin>>t;
    while(t--)
    {

        double c,f,x;
        cin>>c>>f>>x;

        double rate=2.000000;
        double time=x/rate;
        double temp=time;
        double required=0.000000;
        double old=0.000000;
        int ctr=1;
        while(1)
        {
            required+=c;
            old+=c/rate;
            rate+=f;
            temp= old+(x/rate);
            //cout<<required<<" "<<rate<<" "<<temp<<endl;

            if(temp>time)
                break;
            time=temp;
        }

        cout<<"Case #"<<tc++<<": ";
        printf("%.7lf\n",time);
    }
}
