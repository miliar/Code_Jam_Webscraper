#include<iostream>
#include<math.h>
#include<fstream>

using namespace std;

bool oneDigit(int num)
{
    return (num >= 0 && num < 10);
}

bool isPalUtil(int num, int* dupNum)
{
    if (oneDigit(num))
        return (num == (*dupNum) % 10);

    if (!isPalUtil(num/10, dupNum))
        return false;

    *dupNum /= 10;
    return (num % 10 == (*dupNum) % 10);
}

bool isPal(int num)
{
    int *dupNum = new int(num); 
    return isPalUtil(num, dupNum);
}

int main()
{
    ifstream infile;
    ofstream outfile;
    infile.open("C-small-attempt0.in");
    outfile.open("C-small-attempt0.out");    
    int T;
    infile >> T;
    
    int t = 0, l, h, cl, fh, count;
    while(t<T)
    {
               t++;
               count = 0;
               infile >> l >> h;
               cl = ceil(sqrt(l));
               fh = floor(sqrt(h));
               for(int i = cl; i <= fh; i++)
               {
                       if(isPal(i) && isPal(i*i))
                                           count++;
               }                                      
               outfile << "Case #" << t << ": " << count << endl;
    }          
    return 0;
}
