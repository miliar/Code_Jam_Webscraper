#include <iostream>

using namespace std;

int main()
{
    long long int t,l;long double time,c,f,k,t1,t2,r,temp1,temp2,temp3;
    cin>>t;
    for(l=1;l<=t;l++)
    {
        time=0;
        cin>>c>>f>>k;
        r=2.0;
            t1=c/r;
            t2=k/r;
            if(t2<=t1)
                time+=t2;
            else if(t2>t1)
            {
                while(1)
                {
                    temp1=k/r;
                    temp2=c/r;
                    r+=f;
                    temp3=temp2+k/r;
                    if(temp1<=temp3)
                    {
                        time+=temp1;
                        break;
                    }
                    else
                    {
                        time+=temp2;
                        continue;
                    }
                }
            }
            cout.precision(7);
        cout<<"Case #"<<l<<": "<<fixed<<time<<"\n";
    }
    return 0;
}
