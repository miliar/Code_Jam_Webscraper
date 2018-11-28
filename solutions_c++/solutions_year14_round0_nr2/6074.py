
#include<string.h>

#include<stdio.h>

#include<stdlib.h>

#include<ctype.h>

#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include<cstdlib>
#include <cstdio>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <utility>
#include <fstream>
#define INF     9999999
using namespace std;
int main()
{
    ifstream cin("B-large.in");
    ofstream cout("out.out");
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<": ";
        double c,f,x,y;
        cin>>c>>f>>x;
        y=x/2;
        double time=0;
        for(int m=1;;m++)
        {
            double ty;
            time+=c/(f*(m-1)+2);
            ty=time+x/(f*m+2);
            if(ty<y)y=ty;
            else break;

        }
        cout.precision(7);
        cout.setf(ios::fixed);
        cout<<y<<endl;

    }
  return 0;
}
