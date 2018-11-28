#include <iostream>
#include <string.h>
#include <sstream>
#include <math.h>

using namespace std;

template <typename T>
string NumberToString ( T Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}

template <typename T>
T StringToNumber ( const string &Text )
{
	stringstream ss(Text);
	T result;
	return ss >> result ? result : 0;
}

int isSquare(int x)
{
    if(x==1 || x==4)
        return 1;
    for(int i=2; i<x/2; i++)
        if(x%i==0)
            if(i*i==x)
                return 1;
    return 0;
}

int main()
{
    int t,a,b,count,yes1,yes2,y,squareof;
    string one,two;

    cin >> t;
    for(int i=0; i<t; i++)
    {
        cin >> a >> b;

        y=0;
        for(int j=a; j<=b; j++)
        {
            yes1=yes2=0;

            if(isSquare(j))
            {
                one = NumberToString(j);
                count=0;
                for(int k=0; k<one.size()/2; k++)
                    if(one[k]==one[one.size()-1-k])
                        count++;
                if(count==(one.size()/2))
                    yes1=1;

                squareof = sqrt(j);

                two = NumberToString(squareof);
                count=0;
                for(int k=0; k<two.size()/2; k++)
                    if(two[k]==two[two.size()-1-k])
                        count++;
                if(count==(two.size()/2))
                    yes2=1;
            }
            if(yes1 && yes2)
                y++;
        }
        cout << "Case #" << i+1 << ": " << y << endl;
    }
    return 0;
}
