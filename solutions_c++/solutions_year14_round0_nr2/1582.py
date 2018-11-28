#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <set>
#include <sstream>
#include <iomanip>


#define forf(a,b) for(a=0;a<b;a++)
#define forb(a,b) for(a=b;a>0;a--)
#define count(a) for (int zzz=0;zzz<a;zzz++)
#define PI 3.14159265358979
#define MILLION 1000000
#define BILLION 1000000000
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("swag.txt","w",stdout);

    int T;
    double C,F,X;
    cin>>T;
    for (int i=0;i<T;i++){
        cin>>C>>F>>X;
        double cookie=0;
        double timetaken=0;
        double numfarms=0;
        while (1){
            //case 1: are we done?
            double temp=0;
            temp=(X)/(F*numfarms+2);

            //case 2: buy more farm

            double temp2=0;
            temp2=(C)/(F*numfarms+2) + (X)/(F*(numfarms+1)+2);

            if (temp<=temp2){
                timetaken+=temp;
                //cout<<"finished"<<endl;
                break;
            }
            else{
                double before=timetaken;
                timetaken+=temp2-(X)/(F*(numfarms+1)+2);
                //cout<<"here"<<temp<<"  "<<temp2<<endl;
                //cout<<"new farm"<<timetaken-before<<endl;
                numfarms=numfarms+1;
            }
        }
        printf("Case #%d: %.7f\n",i+1,timetaken);


    }

    return 0;
}
