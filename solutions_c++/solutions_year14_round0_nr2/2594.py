#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
double g_time=0;
using namespace std;
int main()
{
    int t;
    ifstream ifile("B-large.in");
    ifile>>t;
    ofstream ofile("out.txt");
    int tt=0;
    while(t--)
    {         tt++;
              g_time=0;
              double c,f,X;
              ifile>>c>>f>>X;
              double x=2;
              while(1)
              {
                  double t_x=(double)(X)/x;
                  double tn_x1=((double)(c)/x);
                  double tn_x=tn_x1+ ((double)(X)/(x+f));
                  
                  if(tn_x>t_x)
                  {
                              g_time+=t_x;
                              break;
                  }
                  else
                  {
                      g_time+=tn_x1;
                      x=x+f;
                  }
              }
              char ch[256];
              string s=string("Case #")+ +itoa(tt,ch,10)+string(": ");
              ofile<<s;
              ofile.setf(ios::fixed,ios::floatfield );
              ofile<<setprecision(7)<<g_time<<endl;
    }
}
