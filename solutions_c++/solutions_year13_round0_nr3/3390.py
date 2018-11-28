#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool polindrome(long long int a)
{
    long int i, z;
    vector<short int> vec;
    while(a>0)
    {
        vec.push_back(a%10);
        a=a/10;
    }
    if (vec.size()%2==1)
    {
        i=0;
        z=vec.size()-1;
        while(i!=z)
        {
            if (vec[z]!=vec[i])
            {
                return false;
            }
            i++;
            z--;
        }
    }
    else
    {
        i=0;
        z=vec.size()-1;
        while(i<z)
        {
            if (vec[z]!=vec[i])
            {
                return false;
            }
            i++;
            z--;
        }
    }
    return true;
}

int main()
{
    vector<long long int> polindromes;
    int c=0;
    ifstream input("C-small-attempt0.in");
    for(long long int i=0; i<100000000; i++)
    {
        if ((i*i)%10==1||(i*i)%10==4||(i*i)%10==9)
        {
            if (polindrome(i)==true)
            {
                if(polindrome(i*i)==true)
                {
                    polindromes.push_back(i*i);
                    c++;
                }
            }
        }
    }
    ofstream output("C-small-attempt0.out");
    int a, b, t;
    input >> t;
    int answer=0;
    for (int i=0; i<t; i++)
    {
        answer=0;
        input >> a >> b;
        for (int y=0; y<polindromes.size(); y++)
        {
            if(polindromes[y]>=a && polindromes[y]<=b)
            answer++;
        }
        output << "Case #" << i+1 << ": " << answer << endl;
    }
    input.close();
    output.close();
    return 0;
}
