#include<fstream>
#include<string>
#include<complex>
using namespace std;
int main(int argc, char *argv[])
{
    int i,j,k,count=0,total=0;
    int nums[39]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
    double a,b;
    ifstream iff;
    iff.open("input.in");
	ofstream off;
    off.open("output.out"); 
					   iff>>i;
						            j=i;
							        
					   while(j--)
					   {
                           total=0;
						   iff>>a>>b;
						   a=sqrt(a);
						   b=sqrt(b);
						   for(k=0;k<39;k++)
						   {
                                           if(a<=nums[k] && nums[k]<=b)
						                   {
                                                               total++;
                                           }
                           }
                           count++; 
                           if(j>0)
                                  {
                                           off<<"Case #"<<count<<": "<<total<<endl;
                                  }
                           else
                                  {
                                           off<<"Case #"<<count<<": "<<total;
                                  }
					   }
      iff.close();
      off.close();  
      return 0;
}
