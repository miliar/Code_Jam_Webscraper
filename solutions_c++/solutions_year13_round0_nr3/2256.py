#include <cstdlib>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;
bool is_palindrome(int n)
{
     if(n%10==0){return false;}
     int i;
     vector <int> L;
     while(n!=0)
     {
           L.push_back(n%10);
           n/=10;
     }
     n=L.size();
     for(i=0;i<n/2;i++)
     {
         if(L[i]!=L[n-1-i])
         {
            return false;
         }
     }
     return true;
}

int main(int argc, char *argv[])
{
    ofstream fout("answers3.out");
    ifstream fin("C-small-attempt0.in");
    vector <int> results;
    int i,j,t,T,m,result;
    float A,B;
    fin>>T;
    for(t=0;t<T;t++)
    {
    fin>>A>>B;
    i=sqrt(A);
    m=sqrt(B);
    result=0;
    for(i=i;i<=m;i++)
    {
        if(is_palindrome(i) && is_palindrome(i*i) && i*i>=A)
        {
           result++;
        }
    }
    results.push_back(result);
    }
    for(t=0;t<T;t++)
    {
        fout<<"Case #"<<t+1<<": "<<results[t]<<endl;
    }   
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
