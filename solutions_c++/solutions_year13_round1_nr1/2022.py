
#include<iostream>
#include<list>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<math.h>
#include <sstream>

using namespace std;




int main()
{
    int caso = 1;

    int casos;
    cin>>casos;


    for(int i = 0; i< casos; i ++)
    {
        long long int r,t;
       cin>>r>>t;


        long long int radio = r;

        long long int blanco = 1;

       int conta = 0;
       while(true)
       {
            long long int area = ((r+blanco)*(r+blanco));
           area -= ((r+(blanco-1))*(r+(blanco-1)));
            // cout<<"area: "<<area<<"   "<<t-area<<endl;
           blanco+= 2;
           if(t - area >= 0)
           {
                t -= (area);
                //cout<<"si entre";
           }
            else
                break;

            conta ++;
       }

        cout<<"Case #"<<caso++<<": "<<conta<<endl;

        //cout<<conta<<endl;
    }




    return 0;
}
