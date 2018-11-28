
//Author£ºCY
//School: CUST

#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<stdlib.h>
#include<iomanip>
#include<list>
#include<deque>
#include<map>
#include <stdio.h>
#define PI 3.1415926535897
using namespace std;
double c,f,x;
double sumper,sumtime;
bool pai(){
    if(x/(sumper+f)+c/sumper<x/sumper)
        return true;
    return false;
}
int main()
{
    int t;

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>t;
    int copt=t;
    while(t--){
        sumper=0.0;
        sumtime=0.0;
        cin>>c>>f>>x;
        sumper=2.0;
        while(pai()){
           /* if(!pai()){
               sumtime+=x/sumper;
               cout<<sumtime<<endl;
               break;
            }*/

               sumtime+=c/sumper;
               sumper+=f;

        }
        sumtime+=x/sumper;
        printf("Case #%d: %.7lf\n",copt-t,sumtime);
    }
    return 0;
}
