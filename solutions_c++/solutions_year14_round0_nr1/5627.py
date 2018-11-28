#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int main()
{
	int card[4][4];
    int ans1;
    int ans2;
    int cardinrow[4];
    int loocount;
    int i,j;
    int ans;
    int caseT=1;
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("out.out");
	in >> loocount;
	while(caseT<=loocount)
    {
      in >> ans1;
      for(i=0;i<4;i++)
      {
       for(j=0;j<4;j++)
       {
        in >> card[i][j];
       }
      }
      for(i=0;i<4;i++)
      {
       cardinrow[i] = card[ans1-1][i];
      }
      in >> ans2;
      for(i=0;i<4;i++)
      {
       for(j=0;j<4;j++)
       {
        in >> card[i][j];
       }
      }
      ans1=0;
      for(i=0;i<4;i++)
      {
       for(j=0;j<4;j++)
       {
        if(cardinrow[i]==card[ans2-1][j]){
        ans1++;
        ans = cardinrow[i];}
       }
      }
      if(ans1==1)
      {
       out << "Case #" << caseT << ": " << ans << endl;
       caseT++;
      }
      else if(ans1==0)
      {
       out << "Case #" << caseT << ": " << "Volunteer cheated!" << endl;
       caseT++;
      }
      else
      {
       out << "Case #" << caseT << ": " << "Bad magician!" << endl;
       caseT++;
      }
      ans = 0;
    }  
	in.close();
	out.close();
	return 0;
}
