// Coded by shubham1402
// DATE :  4/12          TIME :


/**************************************************************
*	Problem code: Cookie
*	REFERENCES (if any):
*
*
**************************************************************/
#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream cin("input2.txt");
    ofstream cout("out2.txt");
    int t;
    int k = 0;
    cin>>t;
    while(t--)
    {
        k++;
        double c,f,x;
        cin>>c>>f>>x;
        double inhand = 0;
        double time = 0;
        double prate  = 2;
        if(x <= c)
        {
            time = (x/2.0);
        }
        else
        {
            while(inhand < x)
            {
                time += (c/prate);
                inhand = c;
                if((x-inhand)/prate <= (x)/(prate + f))
                {
                    time += (x-inhand)/prate;
                    break;
                }
                else
                {
                    inhand = 0;
                    prate += f;
                }
            }
        }
        cout<<"Case #"<<k<<": "<<setprecision(7)<<fixed<<time<<endl;
    }
	return 0;
}
