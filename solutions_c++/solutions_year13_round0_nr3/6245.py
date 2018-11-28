#include <fstream>
#include <iostream>
#include <conio.h>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int main()
{
    int T, flag;
    long double total;
    long long A, B, temp1, counter, num;
    ifstream fin("C.in");
    ofstream fout("C.out");
    vector<int> v1;
    fin>>T;
    for(int i=0; i<T; i++)
    {
        fin>>A>>B;
        counter=0;
    for(long long j=A; j<=B; j++)
    {
        v1.clear();
        flag = 0;
        temp1 = j;
        do
        {
            v1.push_back(temp1%10);
            temp1 /= 10;
        }while(temp1>0);
        total = v1.size();
        for(long long k=0; k<total/2; k++)
        {
            if(v1[k]!=v1[total-k-1])
            {
                flag = 1;
                break;
            }
        }
        if(flag == 0)
        {
            //it is a palindrome. now check if it perfect square of a palindrome
            num = sqrt(j);
            v1.clear();
            if(num == sqrt(j))
            {
                flag=0;
                do
                {
                    v1.push_back(num%10);
                    num /= 10;
                }while(num>0);
                total = v1.size();
                for(long long k=0; k<total/2; k++)
                {
                    if(v1[k]!=v1[total-k-1])
                    {
                        flag = 1;
                        break;
                    }
                }
                if(flag==0)
                {
                    counter++;
                }
            }
        }
    }
    fout<<"Case #"<<i+1<<": "<<counter<<endl;
    }
}
