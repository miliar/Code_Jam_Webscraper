#include<iostream>

using namespace std;

int main()
{
  int T;
  cin>>T;
  int M,a;
  int x[4],y[4];
  for (int t = 0; t < T; t++)
    {
      cin>>M;
      for (int i = 0; i < 4; i++)
	for (int j = 0; j < 4; j++)
	  {
	    cin >>a;
	    if (i==M-1)
	      x[j]=a;
	  }
      cin>>M;
      for (int i = 0; i < 4; i++)                                                                                                                                                                                                                                                 	for (int j = 0; j < 4; j++)                                                                                                                                                                                                                                                         {
	   cin >>a;                                                                                                                                                                                                                                                              	    if (i==M-1)                                                                                                                                                                                                                                                             	      y[j]=a;                                                                                                                                                                                                                                                           
	  } 
      
      int z[4] = {0,0,0,0};
      a = 0;

      for (int i = 0; i<4; i++)
	for (int j =0; j<4; j++)
	  {
	    if (x[i] == y[j])
	      {
		z[a] = x[i];
		a++;
	      }
	  }
      if (a==1)
	cout<<"Case #"<<t+1<<": "<<z[0]<<endl;
      if (a==0)
	cout<<"Case #"<<t+1<<": Volunteer cheated!"<<endl;
      if (a > 1)
	cout<<"Case #"<<t+1<<": Bad magician!"<<endl;
    }
}