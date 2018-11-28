#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
using namespace std ;
int main()
{
    ifstream fin ;
    fin.open("A-large.in") ;
    ofstream fout ;
    fout.open("output.txt") ;
    long long T , N ;
    string str ;
    fin >> T ;
    for(long long j=1 ; j <= T ; ++j)
    {
        fin >> N ;
        fin >> str ;
        long long total = 0 , sum = 0 ;
        for(long long i=0 ; i < str.length() ; ++i)
        {
            bool flag = 0 ;
            if(sum < i)
            {
                total += 1 ;
                flag = 1 ;
            }
            if(flag == 1)
                sum += 1 ;
            sum = sum + (str[i] - 48) ;
        }
        fout << "Case #" << j << ": " << total << endl ;
    }
}
