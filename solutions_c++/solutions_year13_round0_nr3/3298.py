#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
ifstream fin("Csmall.in");
ofstream fout("Cout.txt");
char buff[33];
long long T,A,B;

bool test(long long N)
{
     itoa (N,buff,10);
     long long l = strlen(buff);
     //cout << N <<  " " << buff << endl;
     for(long long i=0;i<l/2+1;i++)
             if(buff[i]!=buff[l-1-i])return false;
     return true;
}

int main()
{
    fin >> T;
    for(long long i=0;i<T;i++)
    {
            fin >> A >> B;
            long long low = sqrt(A);
            if(low*low!=A)low++;
            long long high = sqrt(B);
            long long count = 0;
            //cout << low <<" " << high << B<<endl;
            for(long long j = low;j<=high;j++)
            {
                    if(!test(j))continue;
                    if(test(j*j))count++;
            }
            fout << "Case #" << i+1 << ": " << count << endl;
    }
    system("pause");
}
