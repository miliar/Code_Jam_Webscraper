#include<fstream>
#include<math.h>
#include<conio.h>

using namespace std;

int palin(int n)
{
    int r=0,k=n;
    while(n!=0)
    {
     r=r*10+(n%10);
     n/=10;
    }
    if(r==k)
    return 1;
    else
    return 0;
}
int main()
{
    int t,a,b,s;
    ifstream ifile;
    ofstream ofile;
    ifile.open("C-small-attempt0.IN");
    ofile.open("output1.txt");
    ifile>>t;
    
    for(int k=0;k<t;k++)
    {
     s=0;
     ifile>>a>>b;
     for(int i=a;i<=b;i++)
     {
     int sq=sqrt(i);
     if(sq*sq==i&&palin(i)&&palin(sq))
     {
      s++;
     }
     }
     ofile<<"Case #"<<k+1<<": "<<s<<endl;
    }
    ifile.close();
    ofile.close();
    getch();
}
