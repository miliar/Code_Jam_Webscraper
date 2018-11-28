#include<fstream>
#include<string>
#include<math.h>
using namespace std;
main()
{
	ifstream in("D-small-attempt1.in");
	ofstream out("output.txt");
	int test;
	in>>test;

	for(int t=1;t<=test;t++)
	{
        int dom,len,wid;
        in>>dom>>len>>wid;
        int sp=len*wid,flag=0;
        int ma=max(len,wid);
        int min1=min(len,wid);
        int ha1f;
        if(dom%2==0)
            ha1f=dom/2;
        else
            ha1f=dom/2+1;
        if(sp%dom!=0||dom>ma||ha1f>min1||(dom==4&&3>min1))
            flag=1;
        if(flag==1)
            out<<"Case #"<<t<<": RICHARD"<<endl;
        else
            out<<"Case #"<<t<<": GABRIEL"<<endl;
	}

}
