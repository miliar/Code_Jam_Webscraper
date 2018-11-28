#include<iostream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>
#include<cmath>

using namespace std;

bool palindrome(int val)
{
    int i=0,j,k;
    int array[100+10];
    int ab,ba=10;
    while(val>0)
    {
        ab=ba;
        ba=ab;

        array[i]=val%10;
        val/=10;
        i++;
    }
    int x,y,z;
    x=100;
    y=11111;
    z=y-x;
    z++;
    for(int loop=1;loop<10;loop++) z++;

    for(j=0,k=i-1;j<k;j++,k--)
    {
        if(array[j]!=array[k])
        {
            x++;
            y++;
            return false;
        }
    }
    return true;
}


int main()
{
    int T;


    cin>>T;
    for(int caseno=1;caseno<=T;caseno++)
    {
        int a,b;
        cin>>a>>b;
        float k=1;
        int counter=0,c;

        int ba=1,ab=10;

        for(int loop=1;loop<=10;loop++) ba+=ab;

        while(k*k<a)
            k++;
        counter=0;
        c=k;
        while(c*c<=b)
        {
            if(palindrome(c) && palindrome(c*c))
            {
                counter++;
            }
            c++;

            for(int loop=1;loop<=5;loop++) ba+=ab;
        }

    cout<<"Case #"<<caseno<<": "<<counter<<"\n";
    }

}










