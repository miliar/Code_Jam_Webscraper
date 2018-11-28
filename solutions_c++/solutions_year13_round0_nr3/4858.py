#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

bool isHuiWen(int i)
{
    int weishu=1;int tempi=i;
    while(tempi/10!=0){weishu++;tempi=tempi/10;}
    int *p=new int [weishu];

    for(int j=0;j<weishu;++j)
    {
        p[j]=i%10;//cout<<p[j]<<endl;
        i=(i-p[j])/10;
    }
    //cout<<weishu<<"miao"<<endl;
    for(int k=0;k<weishu;++k)
    {
        if(p[k] != p[weishu-k-1]) return 0;
    }
    return 1;
}

int main()
{
	ifstream in("C-small-attempt0.in");
	ofstream out("outfile.out");
	int T;in>>T;
	for(int i=1;i<=T;++i)
	{
	    int A,B,a,b;
	    int n=0;
	    in>>A>>B;
	    a=ceil(sqrt(A));b=sqrt(B);//cout<<a<<b;
	    for(int j=a;j<=b;++j)
	    {
	        //cout<<j;
	        if(isHuiWen(j))
	        {
	            if(isHuiWen(j*j))n++;
	        }
	    }
	    //cout<<n;
	    out<<"Case #"<<i<<": "<<n<<endl;
	}
    in.close();
	out.close();
}
