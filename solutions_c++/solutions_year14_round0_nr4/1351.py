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
    freopen("D-large.in","r",stdin);
    freopen("swag.txt","w",stdout);

    int T;
    double temp;
    cin>>T;
    for (int i=0;i<T;i++){
        int N;
        cin>>N;
        std::vector<double> alist;
        std::vector<double> blist;
        for (int j=0;j<N;j++){
            cin>>temp;
            alist.push_back(temp);
        }
        for (int j=0;j<N;j++){
            cin>>temp;
            blist.push_back(temp);
        }
        sort(alist.begin(),alist.end());
        sort(blist.begin(),blist.end());
        //war
        /*for (int j=0;j<N;j++){
            cout<<alist[j]<<endl;
        }*/

        int warcount=0;
        int place=N-1;
        double highest=blist[N-1];
        int forward=0;
        int backward=N-1;

        while (place>-1){
            if (alist[place]>blist[backward]){
                warcount++;
                forward++;
            }
            else{
                backward--;
            }
            place--;
        }

        //deceit

        place=0;
        int dcount=0;
        for (int j=0;j<N;j++){
            for (int k=place;k<N;k++){
                if ( alist[k]>blist[j] ){
                    place=k+1;
                    dcount++;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",i+1,dcount,warcount);

    }

    return 0;
}
