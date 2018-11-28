#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int main()
{
    int test_case,k;
    cin>>test_case;
    for(k=0;k<test_case;k++){
    float c,f,x;
    cin>>c>>f>>x;
    float time = 0.0;
    int i,j;

    i=floor(x/c-2.0/f);
    if(i<0)
       i=0;

    for(j=0;j<i;j++)
        time = time + c/(2.0+j*f);
    time = time + x/(2.0+i*f);
    cout.precision(9);
    cout<<"Case #"<<(k+1)<<": "<<time<<"\n";
    }
    return 0;

}
