// the stream extraction operator variation of cin
#include <iostream>
using namespace std;
 


int main(void)
{
  double  c,f,x,time=0;
  double s=2;
  int y;
  int i=0;
  cin>>y;

  while (i<y){
	time=0;
    i++;
    s=2;
    cin >> c;
    cin>>f;
    cin>>x;
    while((x/s+time)>(c/s+x/(f+s)+time)){
		time+=c/s;
		//cout<<"c"<<c<<"s"<<s<<"time"<<time<<endl;
		s+=f;
	//	cout<<"s"<<s<<endl;
		
	}
	time+=(x/s);
	//cout<<"x"<<x<<"s"<<s<<"time"<<time<<endl;

	   cout.precision(20);
	   cout<<"Case #"<<i<<": "<<time<<endl;
		  
  }
  
  return 1;
}
