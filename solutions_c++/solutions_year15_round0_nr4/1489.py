#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

void Solve(int t)
{
    int answer = 1;
    int x,r,c;
    cin>>x>>r>>c;
    if(((r*c) % x) !=0)
        answer = 0;
    else if((x > r ) && (x > c))
        answer = 0;
    else if((x == 1) || (x == 2) )
        answer = 1;
    else if( x == 3)
    {
        answer = (min(r,c)>= 2);
    }
    else if(x == 4)
        answer = (min(r,c) > 2 );
    printf("Case #%d:",t);
    if(answer == 1)
        printf(" GABRIEL\n");
    else
        printf(" RICHARD\n");

}
int main()
{

    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        Solve(i);
    }

}
