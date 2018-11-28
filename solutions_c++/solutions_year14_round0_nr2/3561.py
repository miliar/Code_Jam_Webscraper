#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
using namespace std;
ifstream in("test1.txt",ios::in);
//FILE * pfile;
ofstream out("result.txt",ios::out);

void input(double []);
void initial(double []);
void output(double []);
double algo(double []);
double rate = 2.0;


int main()
{
    //std::in.precision(6);
//std::cout.precision(6);

    char c;
    int test_cases = 0, i = 0;
    double a[3];
   in.get(c);
 //   pfile = fopen("test1.txt","r");
   // fscanf(pfile,"%d",&test_cases);
    while(c != '\n')
    {
        test_cases = (test_cases * 10) + (int)c - 48;
        in.get(c);
        //fscanf(pfile,"%d",&test_cases);
    }
    //cout<<test_cases;
    for(i = 0 ; i < test_cases ; i++)
    {
        initial(a);
        input(a);
        output(a);
        cout<<std::fixed<<std::setprecision(9)<<"Case #"<<i+1<<": "<<algo(a)<<"\n";
        out<<std::fixed<<std::setprecision(9)<<"Case #"<<i+1<<": "<<algo(a)<<"\n";
    }
    return 0;
}

void input(double a[3])
{
    /*char c;
    in.get(c);
    int i = 0;
    while(!in.eof() && c != '\n')
    {

        a[i] = (a[i] * 10.0) + (int) c - 48;
        in.get(c);
        if( c == ' ')
        {
            i++;
            in.get(c);
        }

    }
*/
in>>std::setprecision(9)>>a[0]>>a[1]>>a[2];
    //fscanf(pfile,"%f %f %f",a[0],a[1],a[2]);
}

void initial(double a[3])
{
    int i = 0;
    for(i = 0 ; i < 3 ; i++)
    {
        a[i] = 0.0;
    }
}

void output(double a[])
{
    cout<<std::setprecision(9)<<a[0]<<" "<<a[1]<<" "<<a[2]<<"\n";
}

double algo(double a[])
{
    int i = 0;
    rate = 2.0;
    double prev = 0.0 , curr = 0.0 ,prev1 = 0.0,tot = 0.0,r=0.0;
    prev = a[2]/rate;
 //   cout<<"saf"<<a[0]/rate<<"\n";        //2000/2
    do
    {
        if(i != 0)
        {
            prev = curr;
        }
        tot += a[0]/rate;        //500/2
        rate = rate + a[1];         //4

        curr = tot + a[2]/rate;
        i++;
    }while(curr < prev);
    return prev;
}
