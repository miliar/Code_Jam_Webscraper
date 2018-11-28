#include <iostream>

#include <math.h>

#include<sstream>
#include<fstream>


using namespace std;


bool palindrome(string a)

{

    return(a==string(a.rbegin(),a.rend()));

}


int main()

{

   

    long double a,b;

    long double j,m;

    int count,T,k;

    stringstream c,d;
	ifstream in("C-small-attempt0.in");
	ofstream out("out.txt");


    in >> T;

    

    for (k=1; k<=T; k++)

    {

        a=0;

        b=0;

        j=0;

        m=0;

        in >> a >> b;

        

        j=sqrt(a);

        m=sqrt(b);

        

        j=ceill(j);

        m=floorl(m);

        

        count=0;

        

        for(;j<=m;j++)

        {

            c<<j;

            if (palindrome(c.str() ) )

            {

                d<<(powl(j, 2));

                if (palindrome(d.str()))

                    count++;

            }

            c.str("");

            d.str("");

        }

        out << "\nCase #" << k << ": " << count ;

    }

    

    return 0;

}









