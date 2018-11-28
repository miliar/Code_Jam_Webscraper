#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int main ()
{
    int t;
    scanf("%d",&t);
    for (int t1(1);t1<=t;t1++)
    {
        int x,r,c;
        scanf("%d%d%d",&x,&r,&c);
    if (r*c%x!=0||r*c-x<0){cout << "Case #" << t1 <<  ": "<< "RICHARD" << endl;continue;}
    if (c>r)swap(r,c); 
    if (r<x||c<x/2){cout << "Case #" << t1 << ": "<< "RICHARD" << endl;continue;}
    if (x>c+1){cout << "Case #" << t1 << ": "<< "RICHARD" << endl;continue;}
    cout << "Case #" << t1 << ": "<< "GABRIEL" << endl;
        
    }
    return 0;
}
