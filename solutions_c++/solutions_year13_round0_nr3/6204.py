#include <iostream>
#include <vector>
#include <cstdio>
#include <sstream>
#include <cmath>
#include <stdio.h>
#include <cstring>
#include <stdlib.h>

using namespace std;

bool plaindrome(int n)
{
        stringstream s;
        s<<n;
        string num = s.str();
        string numrev = num;

        int j=0;
        for(int i =(num.size())-1 ; i>=0;i--)
        {
            numrev[j]=num[i];
            j++;
        }
        int integer = atoi(numrev.c_str());


        if(integer == n )
            {
                return 1;
            }
            else
            return 0;
}

bool have_square(int n)
{

    if( (int)sqrt(n) * (int)sqrt(n) == n)
        return 1;
    else
        return 0;
}

int main()
{
    freopen("cinput.in", "rt", stdin); // change in.txt to ur input file name, doesn't have to end with .txt
    freopen("output.txt", "wt", stdout); // same for out.txt

    int T;
    cin>>T;
    //cout<<plaindrome(T)<<" "<<have_square(T)<<" "<<sqrt(T);

    //cout<<plaindrome();
    for(int n=0;n<T;n++)
    {
       int A;
       int B;
       int count =0;
       cin>>A>>B;
       for(int i=A;i<=B;i++)
       {
           double d = sqrt(i);

           if(plaindrome(i)== true && have_square(i) == true && plaindrome(d) == true)
            count++;
       }
       cout<<"Case #"<<n+1<<": "<<count<<endl;
    }
    return 0;
}
