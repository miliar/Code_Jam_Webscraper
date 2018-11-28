#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	freopen("B-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t,k=0;
    cin>>t;
    while(k++<t)
    {
    	double c,f,x,ans=0.0,r=2.0;
        cin>>c>>f>>x;
        cout<<"Case #"<<k<<": ";
        if(x<c)
        {
            ans+=(x/r);
            printf("%0.7lf\n",ans);
        }
        else
        {
            while(1)
            {
                double t1,t2;
                t1=x/r;
                t2=(c/r)+(x/(r+f));
                if(t2>=t1)
                {
                    ans+=(x/r);
                    break;
                }
                else 
                {
                    ans+=(c/r);
                    r+=f;
                }
            }
            printf("%0.7lf\n",ans);
        }
    }
	return 0;
}
