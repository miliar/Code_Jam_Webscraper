#include<iostream>
//#include<algorithm>
//#include<set>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for(int t = 0; t<T;++t)
  {	double C,F,X;    //c cost f factor v  x sum
	cin>>C>>F>>X;
	{
		double  sumCookie = 0;
		double time=0;
		double v=2;
		double danweitime;
		double vnext = 2;
		double time2 = 0;
		double time3 = 0;
		for(int factornum = 0; factornum<100000;++factornum)
			{double t1;
				t1 = (X-sumCookie)/v;
				time2 = time + t1;
				danweitime = C/v;
				
			    time = time+danweitime;

				
				

				v = v+F;
				time3 = (time+(X-sumCookie)/v);
				if (time2<time3)
				{time = time2;break;}

				
			    
				
				
			}
		

		 //����Ϊʼ�����С���������֣�����˵ a = 3����Ҳ��� 3.00000 ����
cout.precision(7); 
cout.setf(ios::fixed); 
	 cout<<"Case #"<<t+1<<":"<<" "<<time<<endl;
	}


	}
}