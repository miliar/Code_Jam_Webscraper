#include<iostream>
#include<fstream.h>
#include<conio.h>
using namespace std;

int numbers[10];

void reset()
{
     for(int k=0;k<10;k++)
    { numbers[k]=0; }
}
void check(int N)
{
     while (N>0)
     {
           int digit = N%10;
           N /= 10;
           numbers[digit]=1;
     }
    
}

int filled()
{
    for(int i=0;i<10;i++)
    {
            if(numbers[i]!=1)
            return 0;
    }
    return 1;
}

int main()
{
    for(int k=0;k<10;k++)
    { numbers[k]=0; }
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt2.in");
    fout.open("A-small-output2.txt");
    
    int T, N, n,found;;
    fin>>T;
   for(int m=0;m<T;m++)
    {       reset();
            found=0;
            fin>>N;
            for(int j=1;j<=200;j++)
            {      
            n= N*j;
            check(n);
            if(filled())
            {
                        fout<<"Case #"<<m+1<<": "<<n<<"\n";
                        found=1;
                        break;
            }
           
    }
    if(found==0)
    
           fout<<"Case #"<<m+1<<": INSOMNIA\n";
           }
    
}

