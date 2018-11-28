#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
int squared=0;
string convertInt(int number)
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0;i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}
int is_palyndrom(string chaine)
{
    for(int i=0;i<chaine.size()/2;i++)
    {
        if(chaine[i]!=chaine[chaine.size()-i-1])
            return 0;
    }
    cout<<"Palyndrome "<<chaine<<endl;;
    return 1;
}
int is_square(int nbr)
{
    for(int i=1;i<=nbr;i++)
    {
        if(i*i==nbr)
        {
            cout<<"Square: "<<nbr<<endl;
            squared=i;
            return 1;
        }
    }
    return 0;
}
int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    int Test_case;
    input>>Test_case;
    for(int i=1;i<=Test_case;i++)
    {
        cout<<"Case: "<<i<<endl;
        int a;
        int b;
        int res=0;
        input>>a>>b;
        for(int k=a;k<=b;k++)
        {
            if(is_palyndrom(convertInt(k))&&is_square(k))
            {
                if(is_palyndrom(convertInt(squared)))
                res++;
            }
        }
        output<<"Case #"<<i<<": "<<res<<endl;
    }
}
